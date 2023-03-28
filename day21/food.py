# creating food class
import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        food_x_cor = random.randint(-250, 250)
        food_y_cor = random.randint(-250, 250)
        self.goto(x=food_x_cor, y=food_y_cor)
