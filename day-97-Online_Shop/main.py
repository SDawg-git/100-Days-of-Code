from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column, foreign
from sqlalchemy import Integer, String, Text
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash




app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)


#flasks login manager config
login_manager = LoginManager()
login_manager.init_app(app)

#user callback
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

#admin only decorator
def admin_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user.is_authenticated and current_user.id == 1 :
            return func(*args, **kwargs)
        else:
            return abort(403)
    return wrapper




# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE USER TABLE
class User(db.Model):
    __tablename__ = "Users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(250), nullable=False)

# CONFIGURE PRODUCT TABLE
class Product(db.Model):
    __tablename__ = "Products"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    item_name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    item_description = db.Column(db.Text, nullable=True)
    item_price: Mapped[int] = mapped_column(Integer, nullable=False)
    item_picture: Mapped[str] = mapped_column(String(250), nullable=False)

# CONFIGURE CART TABLE
class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)
    quantity = db.Column(db.Integer, default=1)


with app.app_context():
    db.create_all()



# TODO: Use Werkzeug to hash the user's password when creating a new user.
@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        username = request.form["name"]
        usermail = request.form["email"]
        userpass = request.form["password"]

        result = db.session.execute(db.select(User).where(User.email == usermail))
        existing_mail = result.scalar()

        if existing_mail:
            flash("Email already in use. Log in instead")
            return redirect(url_for("login"))
        else:

            hashed_pass = generate_password_hash(
                password=userpass,
                salt_length=8,
                method="pbkdf2:sha256",
            )

            new_user = User(
                email = usermail,
                password = hashed_pass,
                name = username,
            )

            db.session.add(new_user)
            db.session.commit()

            login_user(new_user)
            return redirect(url_for("get_all_posts"))

    return render_template("register.html", form = form, user=current_user)
