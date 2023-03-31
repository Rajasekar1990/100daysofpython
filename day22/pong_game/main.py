# Creating Pong game

# Step 1: Breakdown the problem stmt
"""
    1. Setting up the screen 800 * 600
    2. Create paddle with up and down movement for player 1 20 * 20
    3. Create paddle with up and down movement for player 2
    4. Create the ball which can move across the screen 10 * 10
    5. Detect collision with wall and bounce
    6. Detect collision with paddle and bounce
    7. Detect ball misses the paddle
    8. Count the score
"""
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scorecard import Scorecard
import time

# Setting up the main screen
s_obj = Screen()
s_obj.setup(width=800, height=600)
s_obj.bgcolor("black")
s_obj.title("Ping Pong Game")
s_obj.tracer(0)

l_paddle_obj = Paddle((350, 0))
r_paddle_obj = Paddle((-350, 0))
l_paddle_score_obj = Scorecard()
r_paddle_score_obj = Scorecard()

ball_obj = Ball()

s_obj.listen()
s_obj.onkey(r_paddle_obj.paddle_up, "Up")
s_obj.onkey(r_paddle_obj.paddle_down, "Down")

s_obj.onkey(l_paddle_obj.paddle_up, "w")
s_obj.onkey(l_paddle_obj.paddle_down, "s")

continue_game = True  # To check the movement of the paddle from 0,0 to 350,0 completed, a while loop with update()
# is req
while continue_game:
    # time.sleep(0.25)   # introduce a sleep time of 0.25 seconds to restrict the ball movement
    s_obj.update()
    ball_obj.move()

    # Detect ball on collision with wall and bounce
    if ball_obj.ycor() > 285 or ball_obj.ycor() < -285:
        ball_obj.bounce_on_wall()

    # Detect ball on collision with paddle
    if (ball_obj.distance(r_paddle_obj) < 50 and ball_obj.xcor() > 320) or \
            (ball_obj.distance(l_paddle_obj) < 50 and ball_obj.xcor() < -320):
        ball_obj.bounce_on_paddle()

    # Detect on l_paddle misses the ball
    if ball_obj.xcor() < -380:
        ball_obj.pos_reset()
        r_paddle_score_obj.inc_r_paddle_score()
        r_paddle_score_obj.refresh_r_paddle_scorecard()

    # Detect on r_paddle misses the ball
    if ball_obj.xcor() > 380:
        ball_obj.pos_reset()
        l_paddle_score_obj.inc_l_paddle_score()
        l_paddle_score_obj.refresh_l_paddle_scorecard()

s_obj.exitonclick()
