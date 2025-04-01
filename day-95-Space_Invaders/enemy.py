from turtle import Turtle

class Enemy(Turtle):
    def __init__(self, start_x, start_y):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("white")
        self.tiltangle(270)
        self.goto(start_x, start_y)
        self.direction = 1
        self.speed = 4
        self.left_wall = -180
        self.right_wall = 180
        self.move_down_distance = 20

    def move(self):
        new_x = self.xcor() + (self.direction * self.speed)  #calculating new X is better than using self.forward due to movement direction complicating the game

        if new_x > self.right_wall or new_x < self.left_wall: #changes on wall detection
            self.change_direction()
        else:
            self.goto(new_x, self.ycor())

    def change_direction(self):
        self.direction *= -1  #flip direction
        self.goto(self.xcor(), self.ycor() - self.move_down_distance)  #moves down
