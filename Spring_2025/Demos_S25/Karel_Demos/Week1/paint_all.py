import karel

def main():
    while front_is_clear():
        while front_is_clear():
            put_beeper()
            move()           
        direction()
        
def direction():
    if facing_east():
        put_beeper()
        if left_is_clear():
            turn_left()
            move()
            turn_left()
    else:
        if facing_west():
            put_beeper()
            if right_is_clear():
                turn_right()
                move()
                turn_right()
        
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    