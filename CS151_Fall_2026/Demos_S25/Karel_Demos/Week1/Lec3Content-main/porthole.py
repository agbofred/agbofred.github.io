import karel

def main():
    while front_is_clear():
        if right_is_clear():
            fill_hole()
        move()
    if right_is_clear():
        fill_hole()
            
def fill_hole():
    turn_right()
    move()
    put_beeper()
    turn_around()
    move()
    turn_right()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()
    
    