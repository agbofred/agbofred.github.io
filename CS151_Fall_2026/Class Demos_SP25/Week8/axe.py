from pgl import GArc, GPolygon, GWindow, GCompound, GRect

def my_axe():
    def create_axe():
        gw.axe = GCompound()
        shaft = GRect(-15, 0, 30, 300)
        shaft.set_filled(True)
        shaft.set_color("brown")
        gw.axe.add(shaft)

        blade = GPolygon()
        blade.add_vertex(0, 0)
        blade.add_vertex(200, -50)
        blade.add_vertex(200, 50)
        blade.set_filled(True)
        blade.set_color("gray")
        gw.axe.add(blade, -80, 50)
        return gw.axe
    def movement():
              gw.axe.move(1,0)
    gw = GWindow(500, 500)
    gw.axe = create_axe()
    gw.add(gw.axe, 250, 100)
  
    gw.set_interval(movement, 10)
    

my_axe()