"""
Playing around with Problem 1 creating cubes.
"""

from pgl import GWindow, GPolygon, GCompound

def create_cube():
    def create_poly(ang1, ang2, ang3, color="black"):
        p = GPolygon()
        p.add_vertex(0,0)
        p.add_polar_edge(L,ang1)
        p.add_polar_edge(L,ang2)
        p.add_polar_edge(L,ang3)
        p.set_filled(True)
        p.set_fill_color(color)
        p.set_line_width(2)
        return p

    L = 40
    left = create_poly(-90,30,90,"gray")
    right = create_poly(150,-90,-30,"black")
    top = create_poly(30,150,210,"white")

    cube = GCompound()
    cube.add(left)
    cube.add(right)
    cube.add(top)

    return cube


def main():
    def cube_move(e):
        mouse_cube.set_location(e.get_x(), e.get_y())

    def cube_add(e):
        new_cube = create_cube()
        gw.add(new_cube, e.get_x(), e.get_y())

    gw = GWindow(500,500)
    mouse_cube = create_cube()
    gw.add(mouse_cube, 250, 250)
    gw.add_event_listener("mousemove", cube_move)
    gw.add_event_listener("mousedown", cube_add)


if __name__ == '__main__':
    main()

