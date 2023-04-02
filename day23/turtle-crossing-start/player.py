from turtle import Turtle, Screen

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP = 90
LEFT = 270
RIGHT = 0


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.reset_pos()
        # self.heading(90)  # set the heading of turtle to 90 so that it moves upwards

    def set_turtle_90_deg(self):
        self.heading(90)

    def move_up(self):
        # new_ycor = self.ycor() + MOVE_DISTANCE
        # self.goto(self.xcor(), new_ycor)

        # self.heading(90)
        self.set_turtle_90_deg()
        self.forward(MOVE_DISTANCE)

    # allows player to move left while crossing
    def move_left(self):
        if self.heading() != RIGHT:
            self.heading(270)
            self.forward(MOVE_DISTANCE)
        else:
            self.set_turtle_90_deg()
            self.heading(270)
            self.forward(MOVE_DISTANCE)

    # allows player to move right while crossing
    def move_right(self):
        if self.heading() != LEFT:
            self.heading(0)
            self.forward(MOVE_DISTANCE)
        else:
            self.set_turtle_90_deg()
            self.heading(0)
            self.forward(MOVE_DISTANCE)

    def reset_pos(self):
        self.goto(STARTING_POSITION)

    def finish_line_check(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False