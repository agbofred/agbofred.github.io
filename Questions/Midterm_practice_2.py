def f1(x,y):
    return z + f2(x,y)
 
def f2(x,y=1):
    def f3(k):
        print(k)
        return (y + k) ** 2
    z = x - f3(y)
    return z - y
 
z = 1
print(f1(f2(4),z))

