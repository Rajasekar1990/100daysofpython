from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(x=0, y=0)
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        new_x_cor = self.xcor() + self.x_move  # if we want to slow down the movement then increment by 1,
        # alternatively use time()
        new_y_cor = self.ycor() + self.y_move
        self.goto(new_x_cor, new_y_cor)

    def bounce_on_wall(self):
        self.y_move *= -1  # bounce will happen by changing the direction opposite to move() direction i.e. up down

    def bounce_on_paddle(self):
        self.x_move *= -1  # bounce will happen by changing the direction opp to move() direction i.e. left right
        self.ball_speed *= 0.9  # Manage to increase the speed by 0.9 times on every single bounce from the paddle

    def pos_reset(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
