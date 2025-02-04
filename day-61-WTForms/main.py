from flask import Flask, render_template, request

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap4



'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 
On Windows type:
python -m pip install -r requirements.txt
'''


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
bootstrap = Bootstrap4(app)


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(8)])
    submit = SubmitField(label='Log In')


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")

    return render_template('login_new.html', form = login_form)



if __name__ == '__main__':
    app.run(debug=True)


# denied.html just in case things don't work
# <!DOCTYPE HTML>
# <html>
# <head>
# 	<title>Access Denied</title>
# </head>
# <body>
# 	<div class="container">
# 		<h1>Access Denied </h1>
# 		<iframe src="https://giphy.com/embed/1xeVd1vr43nHO" width="480" height="271" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
# 		<p><a href="https://giphy.com/gifs/cheezburger-funny-dog-fails-1xeVd1vr43nHO">via GIPHY</a></p>
# 	</div>
# </body>
# </html>
