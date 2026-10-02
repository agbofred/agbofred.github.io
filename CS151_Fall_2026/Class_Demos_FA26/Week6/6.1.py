def func(a, b=5, c= True): 
    if c:
        return a + c
    else:
        return a * b
print(func(5,1,False))
    
