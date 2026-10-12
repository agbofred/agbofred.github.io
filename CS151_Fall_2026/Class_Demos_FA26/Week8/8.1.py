from pgl import GArc, GPolygon, GWindow, GCompound, GRect

def my_axe(d):
    x, y = 250 - d / 2, 100 - d / 2
    a1 = GArc(x, y, d, d, 180, -90)
    gw.add(a1)
gw = GWindow(500, 500)
  
    

my_axe(150)