from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.setposition(x=-180, y=225)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE = {self.score}", False, align = "center", font=("Arial", 12, "normal"))

    def update_score(self):
        self.score += 1
        self.update_scoreboard()

    def win(self):
        self.clear()
        self.setposition(0,0)
        self.write(f"YOU WIN! SCORE = {self.score}", False, align = "center", font=("Arial", 12, "normal"))
