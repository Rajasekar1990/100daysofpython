# Random walk using turtle module
from turtle import Turtle, Screen
import random

t_obj = Turtle()
s_obj = Screen()
colors = ["red", "DeepSkyBlue", "green", "coral", "gray51", "SeaGreen", "azure", "BlueViolet", "gray53", "ivory",
          "MediumOrchid1"]
move_direction = [0, 90, 180, 270]

t_obj.shape("turtle")
t_obj.st()
t_obj.color(random.choice(colors))
t_obj.speed("fast")

def move_fn():
    t_obj.color(random.choice(colors))
    t_obj.pensize(random.randint(5, 10))
    t_obj.forward(50)
    t_obj.setheading(random.choice(move_direction))


for _ in range(15):
    move_fn()
