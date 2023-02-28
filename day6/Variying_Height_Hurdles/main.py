variying height in hurdles
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
def hurdle1():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    move
    while front_is_clear():
        move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
       hurdle1()
    else:
        move()