from pgl import GWindow, GOval
import random
 
GWIDTH = 500
GHEIGHT = 400
N_CIRCLES = 20
MIN_RADIUS = 15
MAX_RADIUS = 100
DELTA_TIME = 10
DELTA_SIZE = 1
 
def random_color():
    color = "#"
    for i in range(6):
        color += random.choice("0123456789ABCDEF")
    return color
 
def create_filled_circle(x, y, r, color="black"):
    circ = GOval(x-r, y-r, 2*r, 2*r)
    circ.set_filled(True)
    circ.set_color(color)
    return circ
 
def growing_circles():
    def start_new_circle():
        r = random.uniform(MIN_RADIUS, MAX_RADIUS)
        x = random.uniform(r, GWIDTH - r)
        y = random.uniform(r, GHEIGHT - r)
        gw.circle = create_filled_circle(
                            x, y, 
                            0, random_color()
                        )
        gw.desired_size = 2 * r
        gw.current_size = 0
        gw.circles_created += 1
        return gw.circle
 
    def step():
        # Grow a circle if needed
        if gw.current_size < gw.desired_size:
            gw.current_size += DELTA_SIZE
            x = gw.circle.get_x() - DELTA_SIZE / 2
            y = gw.circle.get_y() - DELTA_SIZE / 2
            gw.circle.set_bounds(
                            x, y, 
                            gw.current_size,
                            gw.current_size
                        )
        # or add a circle if you can
        elif gw.circles_created < N_CIRCLES:
            gw.add(start_new_circle())
        # or stop
        else:
            timer.stop()
 
    gw = GWindow(GWIDTH, GHEIGHT)
    gw.circles_created = 0
    gw.current_size = 0
    gw.desired_size = 0
    timer = gw.set_interval(step, DELTA_TIME)

growing_circles()