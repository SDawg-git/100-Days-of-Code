from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(x= 0, y=-280)



    def up(self):
        self.forward(10)

    def return_player(self):
        self.goto(x = 0, y = -280)
