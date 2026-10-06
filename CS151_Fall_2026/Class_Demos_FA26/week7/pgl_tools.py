from pgl import GOval

"""
A collection of functions to be used to facilitate quickly
creating objects in PGL
"""

def create_filled_circ(x_cent, y_cent, radius, 
                       is_filled =True, is_border = True, 
                       color = "black", ):
    circ = GOval(
        x_cent/2 - radius,
        y_cent/2 - radius,
        radius * 2, 
        radius * 2
    )
    if is_filled:
        circ.set_filled(True)
    if is_border:
        circ.set_fill_color(color)
    else:
        circ.set_color(color)
        
    return circ
        
    

