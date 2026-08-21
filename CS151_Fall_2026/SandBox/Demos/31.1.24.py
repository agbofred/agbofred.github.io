NUM_ODDS = 100 # Constant, so using all caps

def print_odds():
    """
    Prints the first NUM_ODDS odd numbers 
    starting at 1.
    """
    value = 1
    for i in range(NUM_ODDS):
        print(value)
        value += 2

if __name__ == '__main__':
    print_odds()