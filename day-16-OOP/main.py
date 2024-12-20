import time
from prettytable import PrettyTable
from turtle import Turtle, Screen

timmy = Turtle()
myTable = PrettyTable()
print(myTable)

#     OR
#    import Turtle
#    timmy = turtle.Turtle()

print(timmy)
timmy.shape("turtle")

my_screen = Screen()

timmy.color("blue")
timmy.forward(500)
timmy.left(90)
timmy.color("red")
timmy.forward(100)





my_screen.exitonclick()
