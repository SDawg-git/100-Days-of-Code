from turtle import Turtle

class Projectile(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(0.75, 0.25)



