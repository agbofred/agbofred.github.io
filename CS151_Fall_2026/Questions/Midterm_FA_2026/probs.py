def func_1(x,y):
    return z + x**2
def func_2(x,y=1):
    def func_3(k):
        return (y + k) ** 2
    z = x - func_3(y)
    return z - y
z = 1
print(func_1(func_2(4),z))