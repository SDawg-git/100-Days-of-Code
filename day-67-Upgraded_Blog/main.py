
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, select
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, InputRequired
from flask_ckeditor import CKEditor, CKEditorField
import datetime

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get["SECRET_KEY"]
Bootstrap5(app)
ckeditor = CKEditor(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = []
    result = db.session.execute(db.select(BlogPost))
    all_posts = result.scalars().all()
    for blog in all_posts:
        post = {
            "id": blog.id,
            "title": blog.title,
            "subtitle": blog.subtitle,
            "date": blog.date,
            "body": blog.body,
            "author": blog.author,
            "img_url": blog.img_url,
        }
        posts.append(post)

    #print(posts)


    return render_template("index.html", all_posts=posts)

# TODO: Add a route so that you can click on individual posts.
@app.route('/<int:post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id

    #print(post_id)
    result = db.session.execute(select(BlogPost).where(BlogPost.id == post_id))
    requested_post = result.scalars().first()
    #or could've done it easier with   requested_post = db.get_or_404(BlogPost, post_id)

    return render_template("post.html", post=requested_post)



class BlogForm(FlaskForm):
    title = StringField('Blog Post Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    name = StringField('Your Name', validators=[DataRequired()])
    img_url = StringField('Blog Image URL', validators=[DataRequired()])
    body = CKEditorField('Blog Content', validators=[DataRequired()])
    submit = SubmitField(label='Submit Post')




# TODO: add_new_post() to create a new blog post

@app.route('/new-post', methods=["POST", "GET"])
def new_post():
    form = BlogForm()
    if form.validate_on_submit():
        title = form.title.data
        subtitle = form.subtitle.data
        name = form.name.data
        img_url = form.img_url.data
        body = form.body.data


        x = datetime.datetime.now()
        month = x.strftime("%B")
        year = x.year
        date = x.day

        current_date = f"{month} {date}, {year}"

        created_post = BlogPost(
            title =  title,
            subtitle =  subtitle,
            date = current_date,
            body = body,
            author = name,
            img_url =  img_url,
        )

        db.session.add(created_post)
        db.session.commit()

        return "Successfully added post"

    return render_template("make-post.html", form = form)

# TODO: edit_post() to change an existing blog post

@app.route('/edit-post/<int:post_id>', methods=["POST", "GET"])
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)

    edit_form = BlogForm(
        title = post.title,
        subtitle = post.subtitle,
        img_url = post.img_url,
        author = post.author,
        body = post.body
    )

    if edit_form.validate_on_submit():


        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = edit_form.name.data
        post.body = edit_form.body.data
        db.session.commit()


        return redirect(url_for("show_post", post_id=post_id))

    return render_template("make-post.html", form = edit_form, edit = True)

# TODO: delete_post() to remove a blog post from the database
@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    db.session.delete(post)
    db.session.commit()

    return redirect(url_for("get_all_posts"))



# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
