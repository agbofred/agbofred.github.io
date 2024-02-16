from pgl import GWindow, GOval, GLine, GRect, GLabel

def make_filled_circ(x_cent, y_cent, radius, color='black'):
    circle = GOval(x_cent-radius, y_cent-radius, 2*radius, 2*radius)
    circle.set_color(color)
    circle.set_filled(True)
    return circle

if __name__ =="__main__":
    gw = GWindow(800, 600)
    c1= make_filled_circ(200,200, 20,"green")
    gw.add(c1)
    c2= make_filled_circ(300,300, 40,"red")
    gw.add(c2)