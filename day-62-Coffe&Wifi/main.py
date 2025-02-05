from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TimeField
from wtforms.validators import DataRequired, URL
import csv


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get["SECRET_KEY_"]
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe Name', validators=[DataRequired()])
    location_url = StringField('Location', validators=[DataRequired(), URL()])
    open_time = TimeField('Opening Time', validators=[DataRequired()])
    closing_time = TimeField('Closing Time', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', choices=[("☕️", "☕️"), ("☕️☕️", "☕️☕️"), ("☕️☕️☕️", "☕️☕️☕️"), ("☕️☕️☕️☕️", "☕️☕️☕️☕️")], validators=[DataRequired()])
    wifi_rating = SelectField('Wifi Rating', choices=[("✘", "✘"),("💪", "💪"), ("💪💪", "💪💪"), ("💪💪💪", "💪💪💪"), ("💪💪💪💪", "💪💪💪💪")], validators=[DataRequired()])
    outlet_rating = SelectField('Outlet Rating', choices=[("✘", "✘"),("🔌", "🔌"), ("🔌🔌", "🔌🔌"), ("🔌🔌🔌", "🔌🔌🔌"), ("🔌🔌🔌🔌", "🔌🔌🔌🔌")], validators=[DataRequired()])
    submit = SubmitField('Submit')


# ---------------------------------------------------------------------------



# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        #print("True")
        # Exercise:
        # Make the form write a new row into cafe-data.csv
        # with   if form.validate_on_submit()
        new_cafe = []
        new_cafe.append(form.cafe.data)
        new_cafe.append(form.location_url.data)
        new_cafe.append(str(form.open_time.data))
        new_cafe.append(str(form.closing_time.data))
        new_cafe.append(form.coffee_rating.data)
        new_cafe.append(form.wifi_rating.data)
        new_cafe.append(form.outlet_rating.data)
        #print(new_cafe)

        with open("cafe-data.csv", mode = "a", encoding="utf-8") as file:
            file.write("\n")
            for item in new_cafe:
                file.write(item)
                file.write(", ")


    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
