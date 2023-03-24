#Draw a line using Turtle module with 100 paces
from turtle import Turtle, Screen

turtle_object = Turtle()
turtle_object.shape("triangle")
turtle_object.color("red")
turtle_object.forward(100)
turtle_object.right(90)

screen_obj = Screen()
screen_obj.exitonclick()

