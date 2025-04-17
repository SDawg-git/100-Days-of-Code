from datetime import date

import requests
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, user_logged_in
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column, foreign
from sqlalchemy import Integer, String, Text
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegisterForm, LoginForm


client_id = os.environ.get['CLIENT_ID']


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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE USER TABLE
class User(db.Model, UserMixin):
    __tablename__ = "User"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(250), nullable=False)

    cart_items = db.relationship("Cart", back_populates="user", cascade="all, delete-orphan")

# CONFIGURE PRODUCT TABLE
class Product(db.Model):
    __tablename__ = "Product"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    item_name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    item_description = db.Column(db.Text, nullable=True)
    item_price: Mapped[float] = mapped_column(Integer, nullable=False)
    item_picture: Mapped[str] = mapped_column(String(250), nullable=False)

# CONFIGURE CART TABLE
class Cart(db.Model):
    __tablename__ = "Cart"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("User.id"))
    product_id = db.Column(db.Integer, db.ForeignKey("Product.id"))
    quantity = db.Column(db.Integer, default=1)

    user = db.relationship("User", back_populates="cart_items")
    product = db.relationship("Product")


with app.app_context():
    db.create_all()

# CREATE TEST PRODUCTS
# product1 = Product(
#     item_name = "1 Pence",
#     item_description = "Self Explanatory",
#     item_price = 0.01,
#     item_picture = "https://blog.changechecker.org/umbraco/ImageGen.ashx?pad=true&constrain=false&height=500&width=500&image=/coin-images/215/Change-Checker-App-1p-2.png"
# )
#
# product2 = Product(
#     item_name = "Shoe",
#     item_description = "Shoe for left foot",
#     item_price = 16.99,
#     item_picture = "https://www.legendfootwear.co.uk/cdn/shop/files/7358-1-1.jpg?v=1714140788"
# )
#
# product3 = Product(
#     item_name = "Sword",
#     item_description = "Long and sharp",
#     item_price = 299.99,
#     item_picture = "https://cdn11.bigcommerce.com/s-97i9gwv/images/stencil/960w/products/8964/129604/3fmyyejhh4m__67956.1706520889.jpg?c=2"
# )
#
# with app.app_context():
#     db.session.add(product1)
#     db.session.add(product2)
#     db.session.add(product3)
#     db.session.commit()

@app.route('/')
def home():

    result = db.session.execute(db.select(Product))
    all_products = result.scalars().all()



    return render_template("index.html", user = current_user, products = all_products)




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
                username = username,
            )

            db.session.add(new_user)
            db.session.commit()

            login_user(new_user)
            return redirect(url_for("home"))

    return render_template("register.html", form = form, user=current_user)



@app.route('/login', methods=["GET", "POST"])
def login():

    form = LoginForm()

    if request.method == "POST":

        entered_email = request.form["email"]
        entered_pass = request.form["password"]

        result = db.session.execute(db.select(User).where(User.email == entered_email))
        user = result.scalar()

        if not user:
            flash("Email does not exist.")
            return redirect(url_for("login"))
        else:

            if check_password_hash(pwhash=user.password, password=entered_pass):

                login_user(user)
                flash("Logged in Successfully")

                return redirect(url_for("home", user = current_user))

            else:
                flash("Incorrect Password")
                return redirect(url_for("login"))


    return render_template("login.html", form=form, user=current_user)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))



@app.route('/add-to-cart', methods=["POST"])
def add_to_cart():


    if not current_user.is_authenticated:
        print("not logged in")
        return redirect(url_for('login'))
    else:
        product_id = request.form['product_id']
        quantity = request.form['quantity']
        user_id = current_user.id
        # print(product_id)
        # print(quantity)
        # print(user_id)

        result = db.get_or_404(Product, product_id)
        # print(result.item_name)

        # CODE BELOW WAS SCRAPPED, NO NEED TO CHECK FOR CARTS IT JUST ADDS A NEW ONE - ONE CART PER ITEMS OF SAME ID
        # WHEN SEARCHING THE DB WE WILL SEARCH BY USER ID TO FIND ALL THE CARTS AND DISPLAY INFO

        #checks if cart exists, if not creates it
        #user_cart = db.session.get(Cart, user_id)
        # if not user_cart:
        #     print("cart no exist")
        #     new_cart = Cart(
        #         user_id = user_id,
        #         product_id = product_id,
        #         quantity = quantity
        #     )
        #
        # else:
        #     print("exists")

        new_cart = Cart(
            user_id = user_id,
            product_id = product_id,
            quantity = quantity
        )
        db.session.add(new_cart)
        db.session.commit()

        return redirect(url_for('home'))

@app.route('/show-cart')
def show_cart():
    user_id = current_user.id

    results = db.session.execute(db.select(Cart).where(Cart.user_id == user_id))
    cart_items = results.scalars().all()

    #print(cart_items)

    # for item in cart_items:
    #     print(f"Product: {item.product.item_name}, Quantity: {item.quantity}")
    #     print(item.id)

    return render_template("cart.html", user=current_user, cart_items =  cart_items, client_id = client_id)
    #return redirect(url_for("home"))



@app.route('/remove-from-cart', methods=["POST"])
def remove_from_cart():

    cart_id = int(request.form['cart_id'])
    result = db.session.execute(db.select(Cart).where(Cart.id == cart_id)).scalar()
    db.session.delete(result)
    db.session.commit()
    #flash("Item removed from cart")



    return redirect(url_for('show_cart'))

#THIS ROUTE IS ONLY USED FOR REDIRECTING, IMPROVED THE PAYMENT METHOD
@app.route('/checkout', methods=["POST"])
def checkout():

    client_id = os.environ.get['CLIENT_ID']
    secret_key = "os.environ.get['SECRET_KEY']
    auth_url = "https://api-m.sandbox.paypal.com/v1/oauth2/token"
    data = {
        "grant_type" : "client_credentials"
            }

    headers = {
        "Accept" : "application/json",
        "Accept-Language": "en_US"
            }

    paypal_request = requests.post(url=auth_url, auth=(client_id, secret_key) ,headers=headers, data=data).json()
    access_token = paypal_request['access_token']
    print(access_token)

    cart_total = request.form['cart_total']
    print(cart_total)

    return redirect(url_for("home"))


@app.after_request
def add_header(response):
    response.headers["Cache-Control"] = "no-store"
    return response

if __name__ == "__main__":
    app.run(debug=True, port=5001)
