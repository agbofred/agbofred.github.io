s="string"
print(s[1:5])
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(a[12:15:2]+a[18::5]+ a[-8]) # Answer is NOSXY

print((9 - 3) + 25%5 +3 * 4- 1*(4 - 3 ** 3 + 5) +23 // 7)
print(not (12 < 6 - 5 or 9 // 3 == 3))

def func(a, b=5, c= True):
    if c:
        return a + c
    else:
        return a * b
print(func(5,True,False))