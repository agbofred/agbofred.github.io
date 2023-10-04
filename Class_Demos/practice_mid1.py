"""def tracer(n):
    total = 0
    while n > 0:# start tracing here
        digit = n % 10
        total += digit
        n //= 10
    return total"""


"""def mystery (x):
    def enigma (s, t):
        t -= 1
        return s [::12] + s[t]
    y = len(x)
    z = x[3 - y]
    z += enigma (x, y)
    #z += enigma (x, 9-y)
    return z
if __name__ == "__main__":
    print(mystery("abcdefghijklmn")) # Answer damn"""

#50 % 5 + 3 * 4 - 1 * (4 - 3 ** 3 + 5) + 13 // 7  #Answer `31`
#print(2 + 2 * 2 // 2 ** 2 - 2 % 2) # Answer 3

#print(7 < 9 - 5 and 3 % 0 == 3) # Answer False

a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(a[5:15:3] * 3)
