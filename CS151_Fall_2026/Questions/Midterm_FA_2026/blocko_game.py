from pgl import GWindow, GRect, GLine, GLabel
import random

WIDTH = 800
HEIGHT = 600
p_width = 50
p_height = 50
OBSTACLE_X = WIDTH//2 - p_width//2
OBSTACLE_Y = HEIGHT//2 - p_height


def create_game():
    
    def make_color():
        c ="#"
        for i in range(6):
            value = random.choice("0123456789ABCDEF")
            c +=value
        return c
    
    def add_player():
        gw.block = GRect(p_width//2, HEIGHT//2 - p_height//2, p_width, p_height)
        gw.block.set_fill_color(make_color())
        gw.block.set_filled(True)
        gw.add(gw.block)
        
    def add_obstacle():
            gw.obstacle = GRect(OBSTACLE_X, OBSTACLE_Y, p_width//2, p_height + p_height//2)
            gw.obstacle.set_fill_color(make_color())
            gw.obstacle.set_filled(True)
            gw.add(gw.obstacle)
    def run():
        
        if gw.block.get_x() <= WIDTH:
            gw.block.move(1,0)
        else:
            add_player()
        
    def fall():
        if gw.obstacle.get_y() < OBSTACLE_Y:
            gw.obstacle.move(0, 10)
        else:
            gw.obstacle.set_location(OBSTACLE_X, OBSTACLE_Y)
            gw.fall_timer.stop()

    def on_key_release(tke):
        gw.fall_timer = gw.set_interval(fall, 10)
    
    def on_key(e):
        if e.get_key() == "<UP>":
            gw.obstacle.set_location(OBSTACLE_X, OBSTACLE_Y - 80)

    def on_key_release(tke):
        gw.obstacle.set_location(OBSTACLE_X, OBSTACLE_Y)

    add_player()
    add_obstacle()
    gw.add_event_listener("key", on_key)
    gw._canvas.bind("<KeyRelease-Up>", on_key_release)
    timer = gw.set_interval(run, 2)
        
   
    

if __name__ == '__main__':
    gw = GWindow(WIDTH, HEIGHT)
    gw.block = None
    gw.obstacle = None
    create_game()
