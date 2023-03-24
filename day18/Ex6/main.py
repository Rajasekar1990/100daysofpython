# Random walk using turtle module with random color
# Tuple intro
import turtle
from turtle import Turtle
import random

t_obj = Turtle()
turtle.colormode(255)
move_direction = [0, 90, 180, 270]
t_obj.speed("fast")


def random_color():
    r = (random.randint(0, 255))
    g = (random.randint(0, 255))
    b = (random.randint(0, 255))
    color_tup = (r, g, b)
    return color_tup


def move_fn():
    t_obj.color(random_color())
    t_obj.pensize(random.randint(5, 10))
    t_obj.forward(100)
    t_obj.setheading(random.choice(move_direction))


for _ in range(15):
    move_fn()
