from pgl import GWindow, GOval, GLine, GRect, GLabel
#print("hell0")
def mystery (x):
    def enigma (s, t):
        t -= 2
        return s [::6] + s[t]
    y = len(x)
    z = x[1 - y]
    z += enigma (x, y)
    z += enigma (x, y - 2)
    print(z)

if __name__ == '__main__':
    print(mystery ("abcdefgh"))


