# Greatest Divisor using Euclid’s algorithm 
def greatest_divisor(x,y):
    stop = False
    while not stop:
        remainder = x%y
        if remainder == 0:
            gd = y
            stop = True
        else:
            x, y = y, remainder
    return gd

if __name__ == '__main__' :
       print(f'The greatest divisor is {greatest_divisor(60, 45)}')