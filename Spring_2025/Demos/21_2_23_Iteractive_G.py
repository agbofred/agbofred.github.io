from pgl import GWindow, GOval, GLine, GRect, GLabel
import random
WIDTH = 500
HEIGHT = 500
def draw_dots():
    def click_action(event):
        c = create_filled_rect(
            event.get_x(), event.get_y(), 
            50,50, random_color())
        gw.add(c)

    def create_filled_rect(x,y,w,h,color):
        rec = GRect(x,y,w,h)
        rec.set_color(color)
        rec.set_filled(True)
        return rec
    def random_color():
        color ="#"
        for i in range(6):
            color += random.choice("123456789ABCDEF")
        return color
    
    gw = GWindow(WIDTH, HEIGHT)
    gw.add_event_listener("click", click_action)


#---------------- Drawing a line---------------
def draw_lines():
    def mousedown_event(e):
        x = e.get_x()
        y = e.get_y()
        gw.line = GLine(x,y,x,y)
        gw.line.set_line_width(20)
        gw.add(gw.line)

    def drag_action(e):
        gw.line.set_end_point(e.get_x(), e.get_y())

    gw = GWindow(WIDTH, HEIGHT)
    gw.line = None
    gw.add_event_listener("mousedown", mousedown_event)
    gw.add_event_listener("drag", drag_action)

#---------------- Moving Sqaure---------------
    
def moving_square():
    def step():
        square.move(dx, dy)
        if square.get_x() > 490:
            timer.stop()
    
    def create_filled_rect(x,y,w,h,color):
        rec = GRect(x,y,w,h)
        rec.set_color(color)
        rec.set_filled(True)
        return rec
    
    gw = GWindow(WIDTH, HEIGHT)
    dx = 1
    dy = 0
    square = create_filled_rect(12, 100, 100, 100, "red")
    gw.add(square)
    timer = gw.set_interval(step, 5)
    

if __name__ =="__main__":
    #draw_dots()
    #draw_lines()
    moving_square()