from turtle import Turtle




class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.high_score = self.read_highscore_file()
        self.score = 0
        self.penup()
        self.color("white")
        self.setposition(x=0, y=280)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE = {self.score}, HIGH SCORE = {self.high_score}", False, align = "center", font=("Arial", 12, "normal"))

    def update_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("G:\PyCharm Projects 2.0\day-20-snake_game\highscores.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()


    def read_highscore_file(self):
        with open("G:\PyCharm Projects 2.0\day-20-snake_game\highscores.txt") as file:
            current_highscore = file.read()
            return int(current_highscore)

    # def game_over_func(self):
    #     self.setposition(0, 0)
    #     self.clear()
    #     self.write(f"GAME OVER! Score = {self.score}", False, align="center", font=("Arial", 12, "normal"))
