from pgl import GWindow, GOval, GRect

WIDTH = 800
HEIGHT = 800

def make_interactive_circle(x, y, gw,diameter):

    background = GRect(0,0,WIDTH,HEIGHT)
    background.set_fill_color("black")
    background.set_filled(True)

    circle = GOval(WIDTH / 2 - diameter /2, HEIGHT / 2 - diameter /2, diameter, diameter)
    circle.set_fill_color("green")
    circle.set_filled(True)
    gw = GWindow(WIDTH, HEIGHT)
    gw.add(circle)
    
    def new_background(e):
        background.set_filled(True)
        background.set_fill_color("grey")
        gw.add(background)
    gw.add_event_listener("click", new_background)

if __name__ == "__main__":
    # gw = GWindow(WIDTH, HEIGHT)
    make_interactive_circle(0,0, 800, 800)
   