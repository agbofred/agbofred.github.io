
def largest_factor(n):
    for i in range(n - 1, 0, -1):      
        for j in range(1, n):          
            pass                       
        if n % i == 0:
            return i

# if __name__ == '__main__':
#     print(largest_factor(27))

var_A = (8, 16, 32, )
var_B = (2*var_A, ('bits', ) )
var_C = var_B , ('M_byte', 'G_byte', 'T_byte')
var_D = ("a",)
#print(var_C)
for v in var_C[1:]:
    var_D += v[:1]
#print(var_D)


# def puzzle(t): 
#     def mystery(r,x): 
#         x+=2 
#         def enigma(s=0): 
#             return r[s::x] 
#         return enigma 
#     x=1 
#     y= mystery(t,x=x) 
#     return y(x)+ y() + y(s=8)
  
# print(puzzle("phsyahdpya"))


def f(x,y):
    return x**2 + y

def g(z,n):
    x = 2
    for i in range(n):
        x += z(i,n)
    return x

print(g(f,2))

    
    
