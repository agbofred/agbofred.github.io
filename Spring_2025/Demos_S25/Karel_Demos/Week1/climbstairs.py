import karel

def main():
    while left_is_clear():
        while front_is_blocked():
            turn_left()
            step_up()
            
def step_up():
    move()
    turn_right()
    move()
    put_beeper()
    
def turn_right():
    for i in range(3):
        turn_left()