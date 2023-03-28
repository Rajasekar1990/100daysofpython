# Building Snake Game, creating snake class and moving it to OOP
import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

"""     1. Create Snake Body
        2. Move the Snake
        3. Control the Snake
        4. Detect Collision with Food
        5. Create a Scorecard
        6. Detect Collision with Wall
        7. Detect Collision with Tail       """

s_obj = Screen()
s_obj.tracer(0)  # tracer() is to remove the trace of movement of segments across the screen
s_obj.setup(width=600, height=600)
s_obj.bgcolor("black")
s_obj.title("Snake Game")

is_game_on = True
# Create the snake using Snake Class
snake_obj = Snake()
food_obj = Food()
scoreboard_obj = Scoreboard()

s_obj.listen()
s_obj.onkey(snake_obj.up, "Up")
s_obj.onkey(snake_obj.down, "Down")
s_obj.onkey(snake_obj.left, "Left")
s_obj.onkey(snake_obj.right, "Right")

while is_game_on:
    s_obj.update()
    time.sleep(0.5)

    # move the snake using arrow keys using move method
    snake_obj.move_snake()

    # Detect on collision with food:
    if snake_obj.head.distance(food_obj) < 15:
        food_obj.refresh()  # Change the coordinate of food on collision with snake
        snake_obj.grow_snake()  # extend the length of the snake by 1 unit i.e. 1 segment which is of size 10*10 pixel
        scoreboard_obj.increment_score()  # increment the score by 1 on collision with snake

    # Detect on collision with wall:
    if snake_obj.head.xcor() > 285 or snake_obj.head.xcor() < -285 or snake_obj.head.ycor() > 285 or snake_obj.head.ycor() < -285:
        is_game_on = False
        scoreboard_obj.game_over()

    # Detect on collision with tail:
    for segment in snake_obj.segments:
        if snake_obj.head == segment:
            pass
            # this if stmt is to pass through the exceptional condn i.e snake head when checking on the
            # first segment which cant get a hit by its head

        if snake_obj.head.distance(segment) < 10:
            # This if stmt is to check all current segment from for loop while looping through all of the segments where
            # its distance of head and the segment is at a distance of < 10 pixel
            is_game_on = False
            scoreboard_obj.game_over()

s_obj.exitonclick()
