from turtle import Turtle

TURTLE_START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
RIGHT = 0
LEFT = 180
UP = 90
DOWN = 270


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        """remember to put this self.head
           after self.create_snake() otherwise segment list carry empty values """

    def create_snake(self):
        for pos in TURTLE_START_POS:
            self.add_new_segment(pos)

    def add_new_segment(self, pos):
        t_obj = Turtle(shape="square")
        t_obj.color("white")
        t_obj.penup()
        t_obj.goto(pos)
        self.segments.append(t_obj)

    def grow_snake(self):
        self.add_new_segment(self.segments[-1].position())

    def move_snake(self):
        for segment in range((len(self.segments) - 1), 0, -1):
            new_xcor = self.segments[segment - 1].xcor()
            new_ycor = self.segments[segment - 1].ycor()
            self.segments[segment].goto(x=new_xcor, y=new_ycor)

        self.head.forward(MOVE_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)
