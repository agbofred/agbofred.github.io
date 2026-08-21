def greatest_factor(num):
    """Finds the greatest factor of a number."""
    for i in range(num-1,0,-1):
        if num % i == 0:
            return i
        
if __name__ =='__main__':
    print(greatest_factor(46))
    #print(71*2)