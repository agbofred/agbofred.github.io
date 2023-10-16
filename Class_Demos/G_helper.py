from pgl import GOval, GWindow, GLine, GLabel, GRect

def circle(x,y,d, c): # Creating circles
    cir = GOval(x-d,y-d, d/2,d/2)
    cir.set_color(c)
    cir.set_filled(True)
    return cir


def create_filled_rect(x,y,w,h,color="blue"):
    rec = GRect(x, y, w,h)
    rec.set_fill_color(color)
    rec.set_filled(True)
    return rec
