# Hirst Painting - Drawing dots
import turtle as t
import random
import colorgram

color_list = []
colors = colorgram.extract('image.jpg', 30)
print(colors)

for i in colors:
    # color_list.append(i.rgb)
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    color_tup = (r, g, b)
    color_list.append(color_tup)

# print(color_list)
t.colormode(255)
t_obj = t.Turtle()
t_obj.shape("triangle")
t_obj.speed("fastest")
t_obj.penup()
t_obj.hideturtle()

t_obj.setheading(225)
t_obj.forward(300)
t_obj.setheading(0)


def dot_fn(num_of_dots):
    for dot_count in range(1, num_of_dots + 1):
        t.dot(10, random.choice(color_list))
        t.forward(30)

        if dot_count % 10 == 0:
            t_obj.setheading(90)
            t_obj.forward(50)
            t_obj.setheading(180)
            t_obj.forward(500)
            t_obj.setheading(0)


dot_fn(100)
s_obj = t.Screen()
s_obj.exitonclick()
