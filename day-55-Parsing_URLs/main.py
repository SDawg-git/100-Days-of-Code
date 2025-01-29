# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return ("<h1 style = 'text-align:center'> Hello, World!</h1>"
            "<p>Zinger</p>"
            "<p>Zanger</p>"
            "<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExa3RhN3U1eHNrOXczejR5MzJnYnl4aHZ2Zmxsc3FudzFkbms4OXNndyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o85xoi6nNqJQJ95Qc/giphy.webp'width=200 height=200>"
            )

def make_bold(function):
    def wrapper(*args, **kwargs):
        return f"<b>{function()}</b>"
    return wrapper


def make_emphasis(function):
    def wrapper(*args, **kwargs):
        return f"<em>{function()}</em>"
    return wrapper

def make_underlined(function):
    def wrapper(*args, **kwargs):
        return f"<u>{function()}</u>"
    return wrapper


@app.route("/bye")
@make_bold
@make_underlined
@make_emphasis
def bye():
    return "Bye!"




@app.route("/username/<name>/<int:number>")          #can add more paths after the variable and specify data types
def greet(name, number):
    return f"Hello {name}, your number is {number}!"



if __name__ == "__main__":
    app.run(debug=True)
