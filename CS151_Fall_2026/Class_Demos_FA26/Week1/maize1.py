import karel

def main():
    while front_is_blocked():
        turn_left()
        move()