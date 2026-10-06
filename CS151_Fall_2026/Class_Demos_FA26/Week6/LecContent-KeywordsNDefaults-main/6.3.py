from pgl import GWindow, GOval, GRect
WIDTH = 400
HEIGHT = 800

    

def make_pike_tree(gw, x, y, height, is_snow= False):
    
    """
    This method creates a pike tree
    """
    UNIT_HEIGHT = height/4
    TRUNK_UNIT = UNIT_HEIGHT/4
    TRUNK_HEIGHT = UNIT_HEIGHT
    
    def mack_circ(x_cent, y_cent, width):
        """
        Create oval as leave
        """
        snow = GOval(x_cent - width/2, y_cent - UNIT_HEIGHT/2- 20, width, UNIT_HEIGHT)
        snow.set_color("skyblue")
        snow.set_filled(True)
        gw.add(snow)
        
        circ= GOval(x_cent - width/2, y_cent - UNIT_HEIGHT/2, width, UNIT_HEIGHT)
        circ.set_color("green")
        circ.set_filled(True)
        gw.add(circ)
        
    
    trunk = GRect(x - TRUNK_UNIT/2, y-UNIT_HEIGHT, TRUNK_UNIT, TRUNK_HEIGHT)
    trunk.set_fill_color("grey")
    trunk.set_filled(True)
    
    gw.add(trunk)
    mack_circ(x, y-UNIT_HEIGHT - 0.5* UNIT_HEIGHT, UNIT_HEIGHT)
    mack_circ(x, y-UNIT_HEIGHT - 1.5* UNIT_HEIGHT, 0.66 * UNIT_HEIGHT)
    mack_circ(x, y-UNIT_HEIGHT - 2.5* UNIT_HEIGHT, 0.33* UNIT_HEIGHT)
    
if __name__ == "__main__":
    gw = GWindow(WIDTH, HEIGHT)
    make_pike_tree(gw, 200, 700, 600)
