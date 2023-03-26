# Etch a sketch
from turtle import Turtle, Screen

t_obj = Turtle()
s_obj = Screen()


def move_forward():
    t_obj.forward(10)


def move_left():
    t_obj.left(180)


def move_backwards():
    t_obj.backward(10)


def move_right():
    t_obj.right(180)


def move_left():
    t_obj.left(180)


def clear_drawing():
    t_obj.clear()
    t_obj.penup()  # to lift turtle cursor not to draw while settling back to original pos
    t_obj.home()


s_obj.listen()
s_obj.onkey(function=move_forward, key="w")
s_obj.onkey(function=move_backwards, key="s")
s_obj.onkey(function=move_left, key="a")
s_obj.onkey(function=move_right, key="d")
s_obj.onkey(function=clear_drawing, key="c")
s_obj.exitonclick()
