def Vegas(x):
    y = 2
    for i in range(5):
        x += y
    return x

x = 3
z = Vegas(x)
print('z =', z)
print('x =', x)
