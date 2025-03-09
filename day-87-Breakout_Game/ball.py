import math
from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(1)
        self.x_move = 10
        self.y_move = 10
        self.setposition(0, -180)


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def bounce_wall(self):
        self.x_move *= -1

    def bounce_paddle(self):
        self.y_move *= -1           #change direction
        angle_offset = random.randint(-30, 30)  #adds variety
        speed = (self.x_move ** 2 + self.y_move ** 2) ** 0.5  #keeps speed constant

        new_angle = math.atan2(self.y_move, self.x_move) + math.radians(angle_offset)
        self.x_move = math.cos(new_angle) * speed
        self.y_move = math.sin(new_angle) * speed

        #print("bounce")


    def bounce_top(self):
        self.y_move *= -1
