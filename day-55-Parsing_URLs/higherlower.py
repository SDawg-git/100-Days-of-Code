# save this as app.py
import random
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return ("<h1 style = 'text-align:center'> Guess a number between 0 and 9</h1>"
            "<img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExcjBpanJ4Nm1va2g3bjRiZm9mZXU3MHd3NjR5cXIxeThpZDhmdzdwOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/VbnUQpnihPSIgIXuZv/giphy.webp'>")

picked_number = random.randint(0,9)

@app.route("/<int:user_choice>")          #can add more paths after the variable and specify data types
def higherlower(user_choice):

    if user_choice == picked_number:
        return ("<h1 style='text-align:center'> YIPPEEEE </h1>"
                "<img src='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ3g3bzV4bGVzejYxOWZ5aWN1MmxybnFsNXIxczBpN2RiZjg5ZHJrZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/GeimqsH0TLDt4tScGw/giphy.webp'>")
    elif user_choice > picked_number:
        return ("<h1 style='text-align:center'> TOO HIGH </h1>"
                "<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExcGp1bGl1dDl4ZGR2bjZiZzdsd3I3dHViM29icmRoaXJoaHU1b2lzdiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/z835RsRqQHOlC4rsBr/giphy.webp'>")
    elif user_choice < picked_number:
        return ("<h1 style='text-align:center'> TOO LOW </h1>"
                "<img src='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExNTg4bHRhcmkzcHA1a3JwM2JybzAwMm5lenc5a3Fyam5pNDBldTU0ZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/zihFgY0dbmlB6UOzpi/giphy.webp'>")




if __name__ == "__main__":
    app.run(debug=True)
