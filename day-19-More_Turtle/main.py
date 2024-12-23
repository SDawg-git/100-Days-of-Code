from turtle import Turtle, Screen
import random

screen = Screen()
# tim = Turtle()
# tom = Turtle()


# def move_forwards():
#     tim.forward(10)
#
# def move_backwards():
#     tim.back(10)
#
# def turn_left():
#     tim.left(10)
#
# def turn_right():
#     tim.right(10)
#
# def clear():
#     tim.home()
#     tim.clear()
#
#
# screen.listen()
# screen.onkey(fun= move_forwards, key= "w")
# screen.onkey(fun= move_backwards, key= "s")
# screen.onkey(fun= turn_left, key= "a")
# screen.onkey(fun= turn_right, key= "d")
# screen.onkey(fun= clear, key= "space")

screen.setup(500, 400)
user_input = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color (red, green, blue, orange, purple): ")

is_race_on = False
redTurtle = Turtle(shape = "turtle")                    ##could've done all turtle shapes with shape="turtle"
greenTurtle = Turtle()
blueTurtle = Turtle()
orangeTurtle = Turtle()
purpleTurtle = Turtle()

turtles = [redTurtle, greenTurtle, blueTurtle, orangeTurtle, purpleTurtle]

for i in turtles:
    i.shape("turtle")


# redTurtle.shape("turtle")              ##simplified all of this above
# greenTurtle.shape("turtle")
# blueTurtle.shape("turtle")
# orangeTurtle.shape("turtle")
# purpleTurtle.shape("turtle")

redTurtle.color("red")
greenTurtle.color("green")
blueTurtle.color("blue")
orangeTurtle.color("orange")
purpleTurtle.color("purple")

x_position = 40
for i in turtles:
    i.penup()
    i.setposition(-240, x_position)
    x_position -= 20

# redTurtle.setposition(-240, 40)
# greenTurtle.setposition(-240, 20)
# blueTurtle.setposition(-240, 0)
# orangeTurtle.setposition(-240, -20)
# purpleTurtle.setposition(-240, -40)


def random_steps():
    rng_step = random.randint(0,10)
    return rng_step


if user_input:
    is_race_on = True

while is_race_on:
    for i in turtles:
        i.forward(random_steps())
        if i.xcor() > 220.00:
            is_race_on = False
            winner = i.pencolor()

if winner == user_input:
    print(f"You won! The winner is {winner}")
else:
    print(f"You lost! The winner is {winner}")

screen.exitonclick()


