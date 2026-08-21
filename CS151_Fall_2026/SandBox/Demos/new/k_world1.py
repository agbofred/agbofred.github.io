import karel

def main():
    while right_is_blocked():
        if front_is_blocked():
            turn_left()
        put_beeper()
        move()