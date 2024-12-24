from pickletools import UP_TO_NEWLINE
from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):

        self.turtles = []
        self.create_snake(3)
        self.head = self.turtles[0]





    def create_snake(self, number):
        x_position = 0
        if not len(self.turtles) >= 3:
            for turtle in range (number):
                new_turtle = Turtle()
                new_turtle.penup()                                        #mfw I do it right the first time, she does it the easier way so I do that instead then she says my code is valid ;(
                new_turtle.color("white")
                new_turtle.shape("square")
                new_turtle.setposition(x=x_position, y=0)
                self.turtles.append(new_turtle)
                x_position -= 20
        else:
            for turtle in range(number):
                new_turtle = Turtle()
                new_turtle.penup()
                new_turtle.color("white")
                new_turtle.shape("square")
                last_position_x = self.turtles[len(self.turtles)-1].xcor()
                last_position_y = self.turtles[len(self.turtles)-1].ycor()
                new_turtle.setposition(x=last_position_x, y=last_position_y)
                self.turtles.append(new_turtle)


    # def move(self):
    #
    #     for turtle_number in range(0, len(self.turtles) - 1, +1):
    #         x_coordinate = self.turtles[turtle_number].xcor()
    #         y_coordinate = self.turtles[turtle_number].ycor()
    #         self.turtles[turtle_number].forward(20)
    #         self.turtles[turtle_number + 1].setposition(x_coordinate, y_coordinate)

    def move(self):
        for seg_num in range(len(self.turtles) -1, 0, -1):
            new_x = self.turtles[seg_num-1].xcor()
            new_y = self.turtles[seg_num - 1].ycor()
            self.turtles[seg_num].goto(new_x, new_y)
        self.turtles[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def reset_snake(self):
        for i in self.turtles:
            i.hideturtle()
        self.turtles.clear()
        self.create_snake(3)
        self.head = self.turtles[0]
