from pgl import GRect, GLabel, GOval
import random


def create_filled_rect(x_cent, y_cent, width, height, fill="black", border=None):
    """
    Created a filled, centered, rectangle.
    """
    rect = GRect(x_cent - width / 2, y_cent - height / 2, width, height)
    rect.set_filled(True)
    if border is None:
        rect.set_color(fill)
    else:
        rect.set_color(border)
        rect.set_fill_color(fill)
    return rect


def random_color():
    """
    Returns a random color as a hex string.
    """
    color = "#"
    for _ in range(6):
        color += random.choice("0123456789ABCDEF")
    return color


def create_centered_label(x_cent, y_cent, text, font=None):
    label = GLabel(text)
    if font is not None:
        label.set_font(font)
    label.set_location(x_cent - label.get_width() / 2, y_cent + label.get_ascent() / 2)
    return label


def create_filled_circle(x_cent, y_cent, radius, color="Black"):
    circle = GOval(x_cent - radius, y_cent - radius, 2 * radius, 2 * radius)
    circle.set_filled(True)
    circle.set_color(color)
    return circle
