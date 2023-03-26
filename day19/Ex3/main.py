from turtle import Turtle, Screen
import random
t_obj = Turtle
continue_flag = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []

screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Make your bet", prompt="Which turtle will win the race, Enter the color: ")
y = -100
# y_pos = ["-70", "-50", "-30", "-10", "30", "50"]

for i in range(0, len(colors)):
    t_obj = Turtle(shape="turtle")
    t_obj.penup()
    t_obj.color(colors[i])
    t_obj.goto(x=-240, y=y)
    y += 25
    turtle_list.append(t_obj)

if user_input:
    continue_flag = True

while continue_flag:
    for j in turtle_list:
        t_obj.forward(random.randint(0, 10))
        if j.xcor() > 230:
            winner_color = j.pencolor()
            if winner_color == user_input:
                print(f"You won; {winner_color} turtle is the winner")
            else:
                print(f"You lost; {winner_color} turtle is the winner")
            continue_flag = False
screen.exitonclick()
