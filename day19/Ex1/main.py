# How to use Event listeners from  turtle module
# example for higher order function --> func1 taking another func as input in this case func1 is a higher order function
from turtle import Turtle, Screen

t_obj = Turtle()
s_obj = Screen()

t_obj.shape("triangle")
t_obj.speed("fastest")


def move_fn():
    t_obj.forward(10)


s_obj.listen()
s_obj.onkey(function=move_fn, key="space")

