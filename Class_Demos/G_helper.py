from pgl import GOval, GWindow, GLine, GLabel, GRect
def circle(x,y,d, c):
    cir = GOval(x-d,y-d, d/2,d/2)
    cir.set_color(c)
    cir.set_filled(True)
    return cir


