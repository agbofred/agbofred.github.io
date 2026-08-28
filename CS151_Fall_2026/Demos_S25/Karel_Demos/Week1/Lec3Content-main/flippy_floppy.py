import karel

def main():
    """Code to flip all the beepers!"""
    while front_is_clear():
        if no_beepers_present():
            put_beeper()
            move()
        else:
            if beepers_present():
                pick_beeper()
                move()
    if no_beepers_present():
        put_beeper()
    else:
        pick_beeper()
            