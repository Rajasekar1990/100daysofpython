# Building Snake Game, creating snake class and moving it to OOP
import time
from turtle import Turtle, Screen
from snake import Snake

"""     1. Create Snake Body
        2. Move the Snake
        3. Control the Snake    """

"""     4. Detect Collision with Food 
        5. Create a Scorecard
        6. Detect Collision with Wall
        7. Detect Collision with Tail
"""

s_obj = Screen()
s_obj.tracer(0)  # tracer() is to remove the trace of movement of segments across the screen
# turtle_start_pos = [(0, 0), (-20, 0), (-40, 0)]
# segments = []

s_obj.setup(width=600, height=600)
s_obj.bgcolor("black")
s_obj.title("Snake Game")

# creating 3 squares with 3 diff objects
# t_seg1_obj = Turtle(shape="square")
# t_seg1_obj.color("white")
# t_seg1_obj.goto(x=0, y=0)
#
# t_seg2_obj = Turtle(shape="square")
# t_seg2_obj.color("white")
# t_seg2_obj.goto(x=-20, y=0)
#
# t_seg3_obj = Turtle(shape="square")
# t_seg3_obj.color("white")
# t_seg3_obj.goto(x=-40, y=0)

# Step 1: Creating n squares of snake body with a single obj using for loop
# for pos in turtle_start_pos:
#     t_obj = Turtle(shape="square")
#     t_obj.color("white")
#     t_obj.penup()
#     t_obj.goto(pos)
#     segments.append(t_obj)

# Step 2: Moving snake across the 600*600 window
is_game_on = True
snake_obj = Snake()

s_obj.listen()
s_obj.onkey(snake_obj.up, "Up")
s_obj.onkey(snake_obj.down, "Down")
s_obj.onkey(snake_obj.left, "Left")
s_obj.onkey(snake_obj.right, "Right")

while is_game_on:
    s_obj.update()
    time.sleep(0.5)
    # for segment in range((len(segments)-1), 0, -1):
    #     new_xcor = segments[segment - 1].xcor()
    #     new_ycor = segments[segment - 1].ycor()
    #     segments[segment].goto(x=new_xcor, y=new_ycor)
    #
    # segments[0].forward(20)
    # segments[0].left(90)
    snake_obj.move_snake()

s_obj.exitonclick()

# Step 3: Control the snake; Creating Snake, food and scoreboard class


