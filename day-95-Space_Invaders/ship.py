from turtle import Turtle
from projectile import Projectile

class Ship(Turtle):
    def __init__(self):
        super().__init__()


        self.penup()
        self.shape("triangle")
        self.color("white")
        self.tiltangle(90)
        self.setposition(x=0, y=-220)
        self.projectiles = []

    def move_left(self):
        if self.xcor() > -200:  # bounds so the paddle can't move outside of the screen
            self.back(20)

    def move_right(self):
        if self.xcor() < 200:
            self.forward(20)

    def shoot(self):
        projectile = Projectile(self.xcor(), self.ycor())
        self.projectiles.append(projectile)
