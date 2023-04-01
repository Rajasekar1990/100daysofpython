from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-280, 280)

    def refresh_score(self):
        self.write("Level: {self.level}", True, align="left", font=FONT)

    def increment_level(self):
        self.level += 1
        self.clear()
        self.refresh_score()

    def game_over(self):
        self.write("GAME OVER", True, align="center", font=FONT)
