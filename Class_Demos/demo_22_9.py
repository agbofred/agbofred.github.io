b = 1
def f1(a):
    print(a)
    print(b)
 
    def f2():
        c = a + b
        return c * 3
    return f2 
 
f2 = f1(10) 
c = f2()