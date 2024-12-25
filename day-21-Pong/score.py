from turtle import Turtle

class Score(Turtle):
    def __init__(self, x_coord, y_coord):
        super().__init__()

        self.hideturtle()
        self.setposition(x_coord, y_coord)
        self.color("white")
        self.penup()
        self.score = 0
        self.write(f"Score: {self.score}")

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}")
