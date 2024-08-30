def my_function():
    print("Hello")
    print("Bye")


my_function()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    while front_is_clear():
        move()
    if at_goal():
        break
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()