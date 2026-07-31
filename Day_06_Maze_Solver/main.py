# Note: This code is written specifically for the Reeborg's World Maze environment.
# Built-in functions like move(), turn_left(), front_is_clear(), and at_goal()
# are pre-defined in the Reeborg's World API and will throw errors in a standard IDE.

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while at_goal() == 0:
    while wall_on_right():
        if at_goal():
            break
        elif front_is_clear():
            move()
        else:
            turn_left()
            if at_goal():
                break
            elif front_is_clear():
                move()
        turn_right()
        if at_goal():
            break
        elif front_is_clear():
            move()