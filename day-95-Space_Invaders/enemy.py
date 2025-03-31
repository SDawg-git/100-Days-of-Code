from turtle import Turtle
from projectile import Projectile

class Enemy(Turtle):
    def __init__(self):
        super().__init__()


        self.penup()
        self.shape("turtle")
        self.color("white")
        self.tiltangle(270)
        self.setposition(x=0, y=0)

