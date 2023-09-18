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

def largest_factor(n):
    factor = n - 1
    while n % factor != 0:
        factor -= 1
    return factor

if __name__ == '__main__':
	fac = largest_factor(20)
	print(fac)
