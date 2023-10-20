from pgl import GWindow, GOval, GLine, GRect, GLabel, GArc, GPolygon, GCompound
def arc(d):
    gw = GWindow(500, 200)

    x, y = 250 - d / 2, 100 - d / 2
    a1 = GArc(x, y, d, d, 90, -180)
    a1.set_fill_color("#AF34aa12")
    a1.set_filled(True)
    gw.add(a1)
    
#arc(150)
#Li= "Fred"
L1 = ["F", "r", "e", "d", 20, 2.6]
L2 = L1
L2[0] = "CHanges"
print(L2)
print(L1)
L1[2] = "Second"
L3 = L1.copy()

print(L3)