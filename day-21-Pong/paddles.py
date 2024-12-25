from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(1, 5)
        self.left(90)


    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.back(20)
