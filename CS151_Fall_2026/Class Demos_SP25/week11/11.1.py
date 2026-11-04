# def enigma(x):
#     def mystery(x, y =1):
#         def puzzle(y,z = 8):
#             return len(x+y) - z
#         a =x[:puzzle("rainy")]
#         y +=2
#         return a + x[::puzzle(a,y)]
#     y = len(x)
#     print(mystery(y=2, x=x[:y-2]))
#     return mystery(y=2, x=x[:y-2]) + x[::3]
# enigma("panelist")

# Question 1

def func_1(x,y):
    return z + x**2
def func_2(x,y=1):
    def func_3(k):
        return (y + k) ** 2
    z = x - func_3(y)
    return z - y
z = 1
print(func_1(func_2(4),z))