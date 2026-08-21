from pgl import GWindow, GRect, GOval
import random

def draw_dots():
    def click_action(event):
        c = create_filled_rect(
            event.get_x(), event.get_y(), 
            20,20, random_color())
        gw.add(c)

    gw = GWindow(500, 500)
    gw.add_event_listener("click", click_action)

def create_filled_rect(x,y,w,h,color):
    rec = GRect(x,y,w,h)
    rec.set_fill_color(color)
    rec.set_filled(True)
    return rec

def random_color():
    color_string = "#"
    for i in range(6):
        color_string += random.choice("0123456789ABCDEF")
    return color_string

if __name__ =="__main__":
    draw_dots()