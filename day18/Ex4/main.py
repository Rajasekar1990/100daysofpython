# Draw different shapes using Turtle module
import turtle as t
import random

t_obj = t.Turtle()
t_obj.shape("triangle")

# sides = float(input("Enter the number of sides for your shape "))
colors = ["red", "blue", "green", "coral", "gray51", "black", "azure", "BlueViolet", "gray53", "ivory", "MediumOrchid1"]


def shape_fn(num_side, degree):
    for _ in range(num_side):
        t_obj.forward(100)
        t_obj.right(round(degree))


for side in range(3, 11):
    angle = 360 / side
    #print(round(angle))
    t_obj.color(random.choice(colors))
    shape_fn(num_side=side, degree=angle)
