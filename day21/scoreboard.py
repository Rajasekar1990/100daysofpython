from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")
FONT_COLOR = "white"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color(FONT_COLOR)  # change the color to white as the bgcolor is set to black already.
        self.penup()  # remove the line on movement from 0,0 to 0,285 co-ordinate
        self.goto(x=0, y=285)  # move the scoreboard to top from 0,0 coord to 0,285
        # self.write("Score = {self.score} ", True, align="center", font=("Arial", 15, "normal"))
        self.refresh_scoreboard()
        self.hideturtle()  # post writing score on the screen, hide turtle so that only score gets displayed

    def refresh_scoreboard(self):
        self.write(f"Score = {self.score}", True, align=ALIGNMENT,
                   font=FONT)  # Update scoreboard

    def increment_score(self):
        self.score += 1  # incrementing the score by 1 when it gets called on colliding with food
        self.clear()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", True, align=ALIGNMENT, font=FONT)
