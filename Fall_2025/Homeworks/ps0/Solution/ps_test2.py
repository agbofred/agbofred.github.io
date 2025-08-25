import karel

def main():
    for i in range(4):
        while front_is_clear():
            put_beeper()
            move()
        turn_left()
    