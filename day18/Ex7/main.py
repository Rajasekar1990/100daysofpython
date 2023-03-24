# Draw spirograph using turtle module
import random
import turtle
from turtle import Turtle, Screen

s_obj = Turtle()
s_obj.shape("triangle")
s_obj.pensize(10)

radius = 50
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tup = (r, g, b)
    return color_tup


def spirograph(degree_of_rotation):
    for _ in range(int(360/degree_of_rotation)):
        s_obj.speed("fast")
        s_obj.color(random_color())
        turtle.circle(radius)
        current_pos = turtle.heading()
        new_pos = current_pos + degree_of_rotation
        turtle.setheading(new_pos)
        # turtle.done()


spirograph(5)

screen_obj = Screen()
screen_obj.exitonclick()

