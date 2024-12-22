from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("green4")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color



#t = timmy_the_turtle         can change it like this, or go into refactor -> rename


# for i in range (1,5):                         #draws a square
#     tim.forward(100)
#     tim.left(90)
# tim.forward(100)


# for i in range(10):           #dotted line
#     tim.up()
#     tim.forward(20)
#     tim.down()
#     tim.forward(20)


# for i in range (3):
#     tim.pencolor("blue")
#     tim.forward(100)
#     tim.left(120)
# for i in range(4):
#     tim.pencolor("red")
#     tim.forward(100)
#     tim.left(90)
# for i in range(5):
#     tim.pencolor("green")
#     tim.forward(100)
#     tim.left(72)
# for i in range(6):
#     tim.pencolor("yellow")
#     tim.forward(100)
#     tim.left(60)
# for i in range(7):
#     tim.pencolor("brown")
#     tim.forward(100)
#     tim.left(360/7)
# for i in range(8):
#     tim.pencolor("orange")
#     tim.forward(100)
#     tim.left(45)
# for i in range(9):
#     tim.pencolor("purple")
#     tim.forward(100)
#     tim.left(40)
# for i in range(10):
#     tim.pencolor("lime")
#     tim.forward(100)
#     tim.left(36)




# sides = [3, 4, 5, 6 ,7 ,8 ,9 ,10]
# colours = ["blue", "green", "red", "black", "brown", "orange", "purple", "lime"]                   ##nicer way to do same code as above
#
# for position in range (0,8):
#     current_color = colours[position]
#     tim.pencolor(current_color)
#     for i in range (sides[position]):
#         angle = 360/sides[position]
#         tim.forward(100)
#         tim.left(angle)


screen = Screen()
screen.colormode(255)             ##had to change colormode to 255 for it to work?


# colours = ["royal blue", "orange", "maroon","dark violet","lime","teal","dark turquoise","tomato","blue violet","indigo","navajo white","dark olive green"]
# angles = [0, 90, 180, 270]
#
# tim.pensize(10)
# tim.speed(15)
# while 5 > 3:       #easy way to loop forever
#     angle = random.choice(angles)
#     #current_color = random.choice(colours)
#     #current_color = random.choice(colours)
#     tim.pencolor(random_color())
#     tim.forward(50)
#     tim.left(angle)

tim.speed(100)
for i in range (90):
    tim.pencolor(random_color())
    tim.circle(100)
    tim.right(4)





screen.exitonclick()
