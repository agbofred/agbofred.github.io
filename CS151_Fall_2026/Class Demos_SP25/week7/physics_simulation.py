from pgl import GWindow, GOval, GLine
#from pgl_tools import create_filled_circle

def two_body():
    def create_filled_circle(x, y, r, color="black"):
        circ = GOval(x-r, y-r, 2*r, 2*r)
        circ.set_filled(True)
        circ.set_color(color)
        return circ
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

    gw.set_interval(step, 10)

if __name__ == '__main__':
    two_body()