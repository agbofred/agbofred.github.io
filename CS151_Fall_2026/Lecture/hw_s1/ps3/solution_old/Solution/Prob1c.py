############################################################
# Name:
# Name(s) of anyone worked with:
# Est time spent (hr):
############################################################

from pgl import GWindow, GOval, GLabel
import random


def create_filled_circle(x, y, r, color="black"):
    """
    Draws filled circles of radius r centered at the point
    (x,y) and with specified color.
    """
    c = GOval(x - r, y - r, 2 * r, 2 * r)
    c.set_filled(True)
    c.set_color(color)
    return c


def estimate_pi(tries):
    """
    Uses random dart throws at a circular target to approximate
    the value of pi. As the number of throws gets large, pi should
    be approximately 4 times the fraction of throws that hit the
    circle.
    """

    def take_shot(n_hits):
        """
        Simulates a random "throw" toward the target, and draws
        a circle of the correct color depending on if the
        throw struck the target or not.
        """
        x = random.random() * size
        y = random.random() * size
        is_hit = (x - radius) ** 2 + (y - radius) ** 2 < radius ** 2
        if is_hit:
            color = "red"
            n_hits += 1
        else:
            color = "black"
        gw.add(create_filled_circle(x, y, 1, color))
        return n_hits

    size = 500
    radius = size / 2

    # Creates the window and adds the circular target
    gw = GWindow(size, size)
    gw.add(create_filled_circle(radius, radius, radius, "blue"))

    # Simulate tries number of throws
    num_hits = 0
    for i in range(tries):
        num_hits = take_shot(num_hits)

    # Compute pi
    pi = num_hits / tries * 4

    # Display the rounded value of pi centered pretty in window
    lab = GLabel(str(round(pi, 2)))
    lab.set_font("bold 100px 'serif'")
    lab.set_color("white")
    x = size / 2 - lab.get_width() / 2
    y = size / 2 + lab.get_ascent() / 2
    gw.add(lab, x, y)


if __name__ == "__main__":
    attempts = 5000
    estimate_pi(attempts)


# remove n_hits input and output from take_shot
# subtract ascent instead of add to center
# drop squared from radius on 38
