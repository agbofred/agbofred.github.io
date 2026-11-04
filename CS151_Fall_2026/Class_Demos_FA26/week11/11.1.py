def mystery ( x ):
    def puzzle (x , y =5):
        return x * y
    def enigma ( y ):
        return y ** x
    return enigma( puzzle( x =2)) + enigma(puzzle(3 , x ))


if __name__ == '__main__':
    print( mystery(3))
print((10**3) + (9**3))