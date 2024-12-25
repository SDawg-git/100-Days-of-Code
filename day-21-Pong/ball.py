from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(1)
        self.x_move = 10
        self.y_move = 10



    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def paddle_bounce(self):
        self.y_move *= -1
        self.x_move *= -1

    def reset_position(self):

        self.setposition(0, 0)
        self.bounce_x()

    # def starter_angle(self):
    #     direction = random.choice(["l", "r"])
    #     if direction == "l":
    #         random_angle = random.randint(145, 215)                             #couldn't figure out a random angle between 30 degrees and 330 degrees
    #     elif direction == "r":
    #         random_angle = random.choice([random.randint(0, 35), random.randint(325, 360)])        #nvm did it here lmao
    #     return random_angle                                                                                                   #now gotta re-do it like she did it because the angles are fucking with me





