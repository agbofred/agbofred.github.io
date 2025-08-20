from pgl import GWindow, GRect

WIDTH = 800
HEIGHT = 600

BRICK_WIDTH = 40
BRICK_HEIGHT = 20
BRICKS_IN_BASE = 5

TOT_HEIGHT = BRICKS_IN_BASE * BRICK_HEIGHT
TOT_WIDTH = BRICKS_IN_BASE * BRICK_WIDTH

CX = WIDTH / 2
CY = HEIGHT / 2



def for_method():
    for row in range(BRICKS_IN_BASE):
        for col in range(row + 1):
            b = GRect(
                CX - TOT_WIDTH / 2 + row * BRICK_WIDTH - col * BRICK_WIDTH / 2,
                CY + TOT_HEIGHT / 2 - BRICK_HEIGHT - col * BRICK_HEIGHT,
                BRICK_WIDTH,
                BRICK_HEIGHT,
            )
            b.set_line_width(2)
            gw.add(b)


def while_method():
    xstart = CX - BRICK_WIDTH / 2
    ystart = CY - TOT_HEIGHT / 2
    nrows = 0
    ncols = 0
    while nrows < BRICKS_IN_BASE:
        x = xstart
        y = ystart
        while ncols <= nrows:
            b = GRect(x,y,BRICK_WIDTH, BRICK_HEIGHT)
            b.set_color('red')
            gw.add(b)
            ncols += 1
            x += BRICK_WIDTH
        nrows += 1
        ncols = 0
        xstart -= BRICK_WIDTH / 2
        ystart += BRICK_HEIGHT

gw = GWindow(WIDTH, HEIGHT)
#for_method()
while_method()
