from tkinter.font import names

from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from select import select
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get["SECRET_KEY"]

#flasks login manager config
login_manager = LoginManager()
login_manager.init_app(app)

#user callback
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


# CREATE DATABASE


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB


class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html", logged_in = current_user.is_authenticated)


@app.route('/register', methods=["POST", "GET"])
def register():

    if request.method == "POST":

        result = db.session.execute(db.select(User).where(User.email == request.form["email"]))
        user = result.scalars().first()  # should use .scalar() instead

        if user:
            flash("Email already in use")
            return redirect(url_for("register"))

        else:


            user_pass = request.form["password"]
            hashed_pass = generate_password_hash(user_pass, method="pbkdf2:sha256", salt_length=8)

            new_user = User(
                email = request.form["email"],
                password = hashed_pass,
                name = request.form["name"],
            )
            db.session.add(new_user)
            db.session.commit()

            login_user(new_user)

            return redirect(url_for("secrets", name= new_user.name, logged_in = current_user.is_authenticated))

            #return render_template("secrets.html", name= new_user.name)


    return render_template("register.html")




@app.route('/login', methods=["GET", "POST"])
def login():


    if request.method == "POST":

        entered_email = request.form["email"]
        entered_pass = request.form["password"]

        result = db.session.execute(db.select(User).where(User.email == entered_email))
        user = result.scalars().first()  # should use .scalar() instead

        if not user:
            flash("Email does not exist.")
            return redirect(url_for("login"))
        else:

            if check_password_hash(pwhash=user.password, password=entered_pass):

                login_user(user)
                flash("Logged in Successfully")

                return redirect(url_for("secrets", name=user.name))

            else:
                flash("Incorrect Password")
                return redirect(url_for("login"))


    return render_template("login.html", logged_in = current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)

    return render_template("secrets.html", name = current_user.name, logged_in = True)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/download', methods = ["POST"])
@login_required
def download():
    return send_from_directory(
        'static', path="files/cheat_sheet.pdf", as_attachment = True
    )


if __name__ == "__main__":
    app.run(host = "0.0.0.0",debug=True)
