import csv

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from flask import Flask, render_template, url_for, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField, SubmitField, SelectField, TimeField
from wtforms.fields.numeric import IntegerField
from wtforms.validators import DataRequired, URL


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

class CafeForm(FlaskForm):
    cafe = StringField('Cafe Name', validators=[DataRequired()])
    location_url = StringField('Location URL', validators=[DataRequired(), URL()])
    open_time = TimeField('Opening Time', validators=[DataRequired()])
    closing_time = TimeField('Closing Time', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', choices=[("☕️", "☕️"), ("☕️☕️", "☕️☕️"), ("☕️☕️☕️", "☕️☕️☕️"), ("☕️☕️☕️☕️", "☕️☕️☕️☕️")], validators=[DataRequired()])
    wifi_rating = SelectField('Wifi Rating', choices=[("✘", "✘"),("💪", "💪"), ("💪💪", "💪💪"), ("💪💪💪", "💪💪💪"), ("💪💪💪💪", "💪💪💪💪")], validators=[DataRequired()])
    outlet_rating = SelectField('Outlet Rating', choices=[("✘", "✘"),("🔌", "🔌"), ("🔌🔌", "🔌🔌"), ("🔌🔌🔌", "🔌🔌🔌"), ("🔌🔌🔌🔌", "🔌🔌🔌🔌")], validators=[DataRequired()])
    submit = SubmitField('Submit')



# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Cafe TABLE Configuration
class Cafes(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    location_url: Mapped[str] = mapped_column(String(500), nullable=False)
    open_time: Mapped[str] = mapped_column(String(250), nullable=False)
    closing_time: Mapped[str] = mapped_column(String(250), nullable=False)
    coffee_rating: Mapped[str] = mapped_column(String(250), nullable=False)
    wifi_rating: Mapped[str] = mapped_column(String(250), nullable=False)
    outlet_rating: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()






@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/cafes")
def show_cafes():

    # with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:      #open and read cafes in CSV
    #     csv_data = csv.reader(csv_file, delimiter=',')
    #     list_of_rows = []
    #     for row in csv_data:
    #         list_of_rows.append(row)

    result = db.session.execute(db.select(Cafes))
    all_cafes = result.scalars().all()
    print(all_cafes[0].name)
    cafes_list = []
    for cafe in all_cafes:
        cafe_dict = {
            "id": cafe.id,
            "name": cafe.name,
            "location_url": cafe.location_url,
            "open_time": cafe.open_time,
            "closing_time": cafe.closing_time,
            "coffee_rating": cafe.coffee_rating,
            "wifi_rating": cafe.wifi_rating,
            "outlet_rating": cafe.outlet_rating,

        }
        cafes_list.append(cafe_dict)

    return render_template("cafes.html", cafes_list = cafes_list)


@app.route("/add-cafe", methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()

    if request.method == "POST":
        if form.validate_on_submit():
            # new_cafe = [form.cafe.data,
            #             form.location_url.data,
            #             str(form.open_time.data),
            #             str(form.closing_time.data),
            #             form.coffee_rating.data,
            #             form.wifi_rating.data,
            #             form.outlet_rating.data]
            #
            # with open("cafe-data.csv", mode = "a", encoding="utf-8") as file:
            #     file.write("\n")
            #     for item in new_cafe:
            #         file.write(item)
            #         file.write(", ")

            new_cafe = Cafes(
                name=form.cafe.data,
                location_url=form.location_url.data,
                open_time = str(form.open_time.data),
                closing_time = str(form.closing_time.data),
                coffee_rating = form.coffee_rating.data,
                wifi_rating = form.wifi_rating.data,
                outlet_rating = form.outlet_rating.data
            )
            db.session.add(new_cafe)
            db.session.commit()

            return redirect(url_for("show_cafes"))

    return render_template("add.html", form=form)


@app.route("/delete-cafe/<int:del_id>")
def delete_cafe(del_id):

    cafe = db.session.get(Cafes, del_id)
    db.session.delete(cafe)
    db.session.commit()

    return redirect("cafes.html")

if __name__ == '__main__':
    app.run(debug=True)

