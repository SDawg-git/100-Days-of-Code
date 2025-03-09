from turtle import Turtle
from ball import Ball

class Paddle(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(1, 5)
        self.setposition(0, -200)

    def move_left(self):
        if self.xcor() > -100:              #bounds so the paddle can't move outside of the screen
            self.back(20)

    def move_right(self):
        if self.xcor() < 100:
            self.forward(20)