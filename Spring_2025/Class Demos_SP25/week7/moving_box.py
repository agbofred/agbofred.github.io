from pgl import GWindow, GRect
def move_box():
    def create_box():
        rec= GRect(10,200,50,50)
        rec.set_fill_color("green")
        rec.set_filled(True)
        return rec
    
    def move_action():
        square.move(1,-1)
        if(square.get_x()>=400):
            timer.stop()

    gw = GWindow(500,500)
    square= create_box()
    gw.add(square)
    timer =gw.set_interval(move_action, 20)
move_box()