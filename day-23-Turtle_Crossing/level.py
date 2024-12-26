from turtle import Turtle


class Level(Turtle):
    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.level = 1
        self.penup()
        self.color("Black")
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", font=('Arial', 20, 'normal'))


    def next_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", font=('Arial', 20, 'normal'))


    def game_over(self):
        self.goto(-40,0)
        self.write("GAME OVER", font=('Arial', 20, 'normal'))
