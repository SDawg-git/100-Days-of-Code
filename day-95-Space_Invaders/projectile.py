from turtle import Turtle

class Projectile(Turtle):
    def __init__(self, start_x, start_y):
        super().__init__()

        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(0.75, 0.25)
        self.setposition(x=0, y=-220)
        self.goto(start_x, start_y)
        self.speed = 5
        self.active = True

    def move_projectile(self):
        if self.ycor() < 270:
            self.sety(self.ycor() + self.speed)
        else:
            self.active = False
