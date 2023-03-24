# Draw a dashed line using Turtle module
import turtle as t

t_obj = t.Turtle()

t_obj.shape("triangle")
t_obj.color("red")
# t_obj.pensize(5)


def dashed_line():
    t_obj.forward(10)
    t_obj.penup()
    t_obj.forward(10)
    t_obj.pendown()


for _ in range():
    dashed_line()
