########################################
# Name:
# Collaborators:
# Estimated time spent (hrs):
########################################

from pgl import GWindow, GRect

WIDTH = 800
HEIGHT = 600
BRICK_WIDTH = 40
BRICK_HEIGHT = 20
BRICKS_IN_BASE = 15

TOT_HEIGHT = BRICKS_IN_BASE * BRICK_HEIGHT
TOT_WIDTH = BRICKS_IN_BASE * BRICK_WIDTH
CX = WIDTH / 2
CY = HEIGHT / 2
def draw_pyramid():
    """ 
    Draws a pyramid of bricks centered on the screen with a height of BRICKS_IN_BASE. 
    """
    xstart = CX - BRICK_WIDTH / 2
    ystart = CY - TOT_HEIGHT / 2
   
    nrows = 0
    ncols = 0
    while nrows < BRICKS_IN_BASE:
        x = xstart
        y = ystart
        while ncols <= nrows:
            b = GRect(x,y,BRICK_WIDTH, BRICK_HEIGHT)
            #b.set_filled('True')
            gw.add(b)
            ncols += 1
            x += BRICK_WIDTH
        nrows += 1
        ncols = 0
        xstart -= BRICK_WIDTH / 2
        ystart += BRICK_HEIGHT



gw = GWindow(WIDTH, HEIGHT)

    # You got it from here




if __name__ == '__main__':
    draw_pyramid()
