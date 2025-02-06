from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


app = Flask(__name__)

all_books = []


class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)


# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
# initialize the app with the extension
db.init_app(app)

##CREATE TABLE
class Book(db.Model):
  id: Mapped[int] = mapped_column(Integer, primary_key=True)
  title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
  author: Mapped[str] = mapped_column(String(250), nullable=False)
  rating: Mapped[float] = mapped_column(Float, nullable=False)

  def __repr__(self):
    return f'<Book {self.title}>'

with app.app_context():
  db.create_all()







@app.route('/')
def home():
    with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.title))
        all_books = result.scalars().all()


    return render_template("index.html", books=all_books)



@app.route("/delete")
def delete():
    book_id = request.args.get("book_id")

    with app.app_context():
        book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        # or book_to_delete = db.get_or_404(Book, book_id)
        db.session.delete(book_to_delete)
        db.session.commit()

    return redirect(url_for("home"))

@app.route("/add", methods=["GET", "POST"])
def add():

    if request.method == "POST":
    #     new_book = {
    #         "title": request.form.get("title"),
    #         "author": request.form.get("author"),
    #         "rating": request.form.get("rating")
    #     }
    #     all_books.append(new_book)
    #     print(all_books)


        with app.app_context():
            new_book = Book(title=request.form.get("title"), author=request.form.get("author"), rating=request.form.get("rating"))
            db.session.add(new_book)
            db.session.commit()


        return redirect(url_for("home"))

    elif request.method == "GET":

        return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():


    if request.method == "POST":
        book_id = request.form["id"]
        book_to_update = db.get_or_404(Book, book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()

        return redirect(url_for("home"))

    book_id = request.args.get("book_id")
    print(book_id)
    book_selected = db.get_or_404(Book, book_id)
    return render_template("edit.html", book=book_selected)


if __name__ == "__main__":
    app.run(debug=True)

