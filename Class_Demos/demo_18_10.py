from pgl import GWindow, GOval, GLine, GRect, GLabel, GArc, GPolygon, GCompound

def drawArc(d):
    gw = GWindow(500,200)
    x, y = 250 - d / 2, 100 - d / 2
    a1 = GArc(x, y, d, d, 180, -90)
    a1.set_fill_color("#111111")
    a1.set_filled(True)
    gw.add(a1)

S = "I am a string"
L = [" I am an", "egg", 34, "45", "Fred"]
if "egg" in S and L[1]<100:
    S[0] = "Fred  first"
else:
    L[0] = S[2:3]
print(L)

even_d= [i for i in range(0,20,2) if i % 3 != 0]
print(f'Even digit ={even_d}')

#if __name__ == "__main__":
    #drawArc()

