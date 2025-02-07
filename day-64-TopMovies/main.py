from http.client import responses
import tmdbsimple as tmdb

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests


movies_API = os.environ.get["MOVIES_API"]
movies_access_token = os.environ.get["API_TOKEN"]
movies_URL = "https://api.themoviedb.org/3/search/movie"

tmdb.API_KEY = os.environ.get["TMDB_KEY"]

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get["SECRET_KEY"]
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)


all_movies = []

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top-movies.db"
# initialize the app with the extension
db.init_app(app)



# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[str] = mapped_column(String(250), nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


    def __repr__(self):
        return f'<Movie {self.title}>'

with app.app_context():
    db.create_all()

    # new_movie = Movie(
    #     title="Phone Booth",
    #     year=2002,
    #     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    #     rating=7.3,
    #     ranking=10,
    #     review="My favourite character was the caller.",
    #     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
    # )
    #
    # second_movie = Movie(
    #     title="Avatar The Way of Water",
    #     year=2022,
    #     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
    #     rating=7.3,
    #     ranking=9,
    #     review="I liked the water.",
    #     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
    # )
    #
    # db.session.add(new_movie)
    # db.session.add(second_movie)
    # db.session.commit()


class ReviewForm(FlaskForm):
    rating = StringField('Your Rating Out of 10', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Submit')

class AddMovie(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')



@app.route("/")
def home():
    
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all()
    # for movie in all_movies:
    #     print(movie.title)

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()



    return render_template("index.html", movies = all_movies)






@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = ReviewForm()
    movie_id = request.args.get("movie_id")
    movie = db.get_or_404(Movie, movie_id)

    if form.validate_on_submit():
        new_rating = form.rating.data
        new_review = form.review.data


        if request.method == "POST":


            movie.rating = new_rating
            movie.review = new_review
            db.session.commit()

            return redirect(url_for("home"))

    return render_template("edit.html", form=form, movie = movie)


@app.route("/delete")
def delete():

    with app.app_context():
        movie_id = request.args.get("movie_id")
        movie_to_delete = db.get_or_404(Movie, movie_id)
        db.session.delete(movie_to_delete)
        db.session.commit()


    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovie()

    if form.validate_on_submit():
        movie_name = form.title.data
        #print(movie_name)

        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {movies_access_token}",
        }

        #response = requests.get(url=movies_URL, headers=header)
        endpoint = "https://api.themoviedb.org/3/authentication"
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()
        print(response.text)
        # data = response.json()
        # print(data)


        search = tmdb.Search()
        result = search.movie(query=movie_name)
        # for instance in search.results:
        #     print(instance)
        #     print(instance['original_title'])
        #     print(instance['overview'])
        #     print(instance['poster_path'])
        #     print(instance['release_date'])



        return render_template("select.html", results = search.results)

    return render_template("add.html", form = form)

@app.route("/addmovie", methods=["GET", "POST"])
def add_specific_movie():
    movie_id = request.args.get("id")

    identity = tmdb.Movies(movie_id)   #can search up movie through ID
    response = identity.info()

    # print(response['original_title'])
    # print(response['poster_path'])
    # print(response['release_date'])
    # print(response['overview'])
    image_url = f"https://image.tmdb.org/t/p/original/{response['poster_path']}"

    #could've done it this way but was too tired to realise lmao

    # url = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    # headers = {
    #     "accept": "application/json",
    #     "Authorization": f"Bearer {movies_access_token}"
    # }
    # response = requests.get(url, headers=headers)
    # print(response.text)

    new_movie = Movie(
        title=response['original_title'],
        year=response['release_date'],
        description=response['overview'],
        rating=None,
        ranking=None,
        review=None,
        img_url=image_url
    )
    db.session.add(new_movie)
    db.session.commit()

    result = db.session.execute(db.select(Movie).order_by(Movie.id))
    all_movies = result.scalars().all()

    return redirect(url_for("edit", movie_id=len(all_movies)))


if __name__ == '__main__':
    app.run(debug=True)
