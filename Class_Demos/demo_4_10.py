def fuc(a,b,c,x):
    print(a,b,c,x)

fuc(1,2,3,4) #positional
fuc(x=2, b=3, c=1, a=4) # Keyword parameter
a,b=2,3
fuc(a,b,c=4, x=1)
