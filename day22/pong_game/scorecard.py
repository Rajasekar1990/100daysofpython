from turtle import Turtle

ALIGNMENT = "center"
FONT_COLOR = "white"
FONT = ("Arial", 80, "normal")


class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color(FONT_COLOR)
        self.goto(x=0, y=290)
        self.refresh_l_paddle_scorecard()
        self.refresh_r_paddle_scorecard()
        self.hideturtle()
        self.l_paddle_score = 0
        self.r_paddle_score = 0

    def refresh_l_paddle_scorecard(self):
        self.goto(-100, 200)  # move to the top and shift x by -100 px for l_paddle score display
        self.write("Score = {self.l_paddle_score} ", True, align=ALIGNMENT, font=FONT)

    def refresh_r_paddle_scorecard(self):
        self.goto(100, 200)  # move to the top and shift x by 100 px for r_paddle score display
        self.write("Score = {self.r_paddle_score} ", True, align=ALIGNMENT, font=FONT)

    def inc_l_paddle_score(self):
        self.l_paddle_score += 1
        self.clear()

    def inc_r_paddle_score(self):
        self.r_paddle_score += 1
        self.clear()
