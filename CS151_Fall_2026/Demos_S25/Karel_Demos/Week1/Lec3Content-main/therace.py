import karel

def main():
    """Code to race to the top, picking up the beeper stacks!"""
    while front_is_clear():
        while beepers_present():
            if beepers_present():
                pick_beeper()
            else:
                move()
        move()
    while beepers_present():
        pick_beeper()