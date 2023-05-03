# Create a paddle class to cover step2 and step3 of test.py
from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos):
        # creating Paddle with up down movement for players
        super().__init__()
        self.new_y_cor = 0
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1, outline=None)
        self.goto(pos)

    def paddle_up(self):
        new_y_cor = self.ycor() + 20  # set the limit of upward movement for every single key press by 20
        self.goto(self.xcor(), new_y_cor)  # make the paddle to move up with 0 as x cor and y as new y cor

    def paddle_down(self):
        new_y_cor = self.ycor() - 20  # set the limit of downward movement for every single key press by 20
        self.goto(self.xcor(), new_y_cor)  # make the paddle to move down with 0 as x cor and y as new y cor
