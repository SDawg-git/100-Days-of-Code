from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import DATETIME
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, DateTime, Date, desc
from flask import Flask, render_template, url_for, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField, SubmitField, SelectField, TimeField, DateField, BooleanField
from wtforms.fields.numeric import IntegerField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get['SECRET_KEY']
Bootstrap5(app)


class TaskForm(FlaskForm):
    task_name = StringField('Task Name', validators=[DataRequired()])
    task_description = CKEditorField("Description", validators=[DataRequired()])
    task_deadline = DateField('Deadline', validators=[DataRequired()])
    task_difficulty = SelectField('Difficulty', choices=[("⭐", "⭐"), ("⭐⭐", "⭐⭐"), ("⭐⭐⭐", "⭐⭐⭐")], validators=[DataRequired()])
    submit = SubmitField('Submit')



# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Cafe TABLE Configuration
class Tasks(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    task_name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    task_description: Mapped[str] = mapped_column(String(500), nullable=False)
    task_deadline: Mapped[Date] = mapped_column(Date, nullable=False)
    task_difficulty: Mapped[str] = mapped_column(String(250), nullable=False)
    task_complete: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)


with app.app_context():
    db.create_all()



@app.route("/")
def home():

    #result = db.session.execute(db.select(Tasks))
    result = db.session.execute(db.select(Tasks).order_by(desc(Tasks.task_deadline)))
    tasks = result.scalars().all()

    return render_template("index.html", tasks=tasks)


@app.route("/add_task", methods=["GET","POST"])
def add():

    form = TaskForm()

    if form.validate_on_submit():
        new_task = Tasks(
            task_name = form.task_name.data,
            task_description = form.task_description.data,
            task_deadline = form.task_deadline.data,
            task_difficulty = form.task_difficulty.data,
            task_complete = False
        )

        db.session.add(new_task)
        db.session.commit()

        return redirect(url_for("home"))

    return render_template("add.html", form=form)


@app.route("/delete_task/<int:del_id>", methods=["GET","POST"])
def delete_task(del_id):

    task = db.session.get(Tasks, del_id)
    db.session.delete(task)
    db.session.commit()

    return redirect(url_for("home"))


@app.route("/change_completion/<int:task_id>", methods=["POST"])
def change_completion(task_id):

    #task = Tasks.query.get(task_id)
    task= db.session.get(Tasks, task_id)

    if task:
        task.task_complete = "task_complete" in request.form
        db.session.commit()

    return redirect(url_for("home"))


@app.route("/edit_task/<int:edit_id>", methods=["GET","POST"])
def edit_task(edit_id):

    task= db.session.get(Tasks, edit_id)
    form = TaskForm(
        task_name = task.task_name,
        task_description = task.task_description,
        task_deadline = task.task_deadline,
        task_difficulty = task.task_difficulty,
    )

    if form.validate_on_submit():
        task.task_name = form.task_name.data
        task.task_description = form.task_description.data
        task.task_deadline = form.task_deadline.data
        task.task_difficulty = form.task_difficulty.data
        db.session.commit()

        return redirect(url_for('home'))

    return render_template("edit.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
