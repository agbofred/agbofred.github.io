def mystery (x):
    va = "add"
    def enigma (s, t):
        t -= 2
        return s [::6] + s[t] 
    y = len(x)
    z = x[1 - y]
    z += enigma (x, y)
    z += enigma (x, y - 2)
    print(z)

if __name__ == '__main__':
    mystery ("abcdefgh")
