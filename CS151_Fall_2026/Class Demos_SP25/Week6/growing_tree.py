from pgl import GWindow, GRect, GOval
# from pgl_tools import create_filled_circ

def make_tree(gw, x, y, height, is_snow=False):
    """ 
    Function to make a tree and place it on the center of the canvas
    """
    UNIT_HEIGHT = height / 4
    TRUNK_WIDTH = UNIT_HEIGHT/4
    
    def make_circ(x_cent, y_cent, width):
        """ Make a circle"""
        # Snow Oval
        snow = GOval(
                x_cent - width/2,
                y_cent - UNIT_HEIGHT/2 - 20,
                width,
                UNIT_HEIGHT   
            )
        snow.set_filled(True)
        snow.set_color('sky blue')
        gw.add(snow)
       
        #Leave Oval
        circ = GOval(
            x_cent - width/2,
            y_cent - UNIT_HEIGHT/2,
            width,
            UNIT_HEIGHT   
        )
        circ.set_filled(True)
        circ.set_color('green')
        gw.add(circ)
    trunk = GRect(x - TRUNK_WIDTH / 2, y - UNIT_HEIGHT, TRUNK_WIDTH, UNIT_HEIGHT)
    trunk.set_filled(True) 
    trunk.set_color("brown")
    
    gw.add(trunk)
    make_circ(x, y - UNIT_HEIGHT - 0.5 * UNIT_HEIGHT, UNIT_HEIGHT)
    make_circ(x, y - UNIT_HEIGHT - 1.5 * UNIT_HEIGHT, 0.66 * UNIT_HEIGHT)
    make_circ(x, y - UNIT_HEIGHT - 2.5 * UNIT_HEIGHT, 0.33 * UNIT_HEIGHT)
    # circ= create_filled_circ(x, y-UNIT_HEIGHT - 0.5 * UNIT_HEIGHT, UNIT_HEIGHT, True, False, "green")
    # gw.add(circ)
    
if __name__ == '__main__':
    gw = GWindow(400, 800)
    make_tree(gw, 200, 700, 600)