#Draw a Square using Turtle module
from turtle import Turtle, Screen

turtle_obj = Turtle()
turtle_obj.shape("circle")
turtle_obj.color("red")


def square():
    turtle_obj.right(90)
    turtle_obj.forward(100)


screen_obj = Screen()
screen_obj.exitonclick()

for _ in range(4):
    square()

