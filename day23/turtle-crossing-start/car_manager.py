import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.create_car()
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        car_frequency = random.randint(1, 100)  # restricting the creation of car frequency using random logic
        if car_frequency < 25:
            car_obj = Turtle()
            car_obj.shape("square")
            car_obj.color(random.choice(COLORS))  # pick a random color from colors list for cars
            car_obj.shapesize(stretch_len=2, stretch_wid=1)  # make the car obj as rectangle 40 * 20 px
            car_obj.penup()
            car_y_pos = random.randint(-260, 260)
            car_obj.goto(300, car_y_pos)
            self.cars.append(car_obj)

    def move_car(self):
        for car in self.cars:
            car.setheading(270)  # set the heading of car to 270 degree i.e. west
            car.forward(self.car_speed)  # moves the car by 5 paces at level 1

    def increase_car_speed(self):
        self.car_speed += MOVE_INCREMENT
