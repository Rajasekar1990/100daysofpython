import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player_obj = Player()
car_manager_obj = CarManager()
scoreboard_obj = Scoreboard()

screen.listen()
screen.onkey(player_obj.move_up, "Up")

# additional feature for turtle, allows to move left or right while crossing
screen.onkey(player_obj.move_left, "Left")
screen.onkey(player_obj.move_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)  # while loop runs every 10ms i.e. 0.1s and refreshes the screen at the same rate
    screen.update()
    car_manager_obj.create_car()
    car_manager_obj.move_car()

    # Detect on collision with car
    for car in car_manager_obj.cars:
        if car.distance(player_obj) < 20:
            # end the game by changing the flag of game_is_on to false
            game_is_on = False
            # End Game with a message GAME OVER
            scoreboard_obj.game_over()

    # Detect turtle crossing finish line:
    if player_obj.finish_line():
        # Reset position of turtle to 0,-280
        player_obj.reset_pos()
        # Increase the car speed by 10 paces on level completion
        car_manager_obj.increase_car_speed()
        # Increment score by 1 point on every successful crossing of finish line
        scoreboard_obj.increment_score()

screen.exitonclick()
