from pgl import GWindow, GLine, GRect, GOval
from G_helper import circle, create_filled_rect
import random
	
WIDTH = 500
HEIGHT = 500

##
def rev_q():
    def act_A(e):
        sq.set_filled(True)
    def act_B(e):
        sq.set_size(
            sq.get_width() - 10,
            sq.get_height() - 10
        )
    gw = GWindow(500, 500)
    sq = GRect(200, 200, 100, 100)
    sq.set_color("blue")
    gw.add(sq)
    gw.add_event_listener("mousedown", act_B)
    gw.add_event_listener("click", act_A)

##
def draw_lines():
    def mousedown_event(e):
        x = e.get_x()
        y = e.get_y()
        gw.line = GLine(x,y,x,y)
        gw.add(gw.line)
 
    def drag_action(e):
        gw.line.set_end_point(e.get_x(), e.get_y())
 
    gw = GWindow(WIDTH, HEIGHT)
    gw.line = None
    gw.add_event_listener("mousedown", mousedown_event)
    gw.add_event_listener("drag", drag_action)


###
def moving_square():
    def step():
        square.move(dx, dy)
        if square.get_x() > 500:
            timer.stop()

    gw = GWindow(500, 200)
    dx = 1
    dy = 0
    square = create_filled_rect(12, 100, 24, 24, "red")
    gw.add(square)
    timer = gw.set_interval(step, 20)

####
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

######

def two_body():
    def step():
        # Compute forces and accelerations
        dx = planet1.get_x() - planet2.get_x()
        dy = planet1.get_y() - planet2.get_y()
        r3 = (dx ** 2 + dy ** 2) ** (3 / 2)
        ax = 1000 / r3 * dx
        ay = 1000 / r3 * dy

        # Update velocities
        gw.vx1 += -ax
        gw.vy1 += -ay
        gw.vx2 += ax
        gw.vy2 += ay

        # Augment history paths
        path1 = GLine(
            planet1.get_x() + 10,
            planet1.get_y() + 10,
            planet1.get_x() + 10 + gw.vx1,
            planet1.get_y() + 10 + gw.vy1,
        )
        path1.set_color("red")
        path1.set_line_width(3)

        path2 = GLine(
            planet2.get_x() + 10,
            planet2.get_y() + 10,
            planet2.get_x() + 10 + gw.vx2,
            planet2.get_y() + 10 + gw.vy2,
        )
        path2.set_color("cyan")
        path2.set_line_width(3)

        # Move planets
        planet1.move(gw.vx1, gw.vy1)
        planet2.move(gw.vx2, gw.vy2)

        gw.add(path1)
        gw.add(path2)

    gw = GWindow(600, 600)
    # Defining state variables
    gw.vx1, gw.vy1 = 0, 1
    gw.vx2, gw.vy2 = 0, -1

    planet1 = create_filled_circle(200, 200, 10, "red")
    planet2 = create_filled_circle(400, 200, 10, "cyan")

    gw.add(planet1)
    gw.add(planet2)

    gw.set_interval(step, 30)



if __name__ =="__main__":
    #rev_q()
    #draw_lines()
    #moving_square()
    #growing_circles()
    two_body()