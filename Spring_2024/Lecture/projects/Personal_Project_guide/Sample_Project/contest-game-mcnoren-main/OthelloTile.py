from pgl import GWindow, GOval, GLabel, GRect
import OthelloGame

class OthelloTile:

    def __init__(self, x, y, length, state, padding, gw):
        self._x = x
        self._y = y
        self._length = length
        self._state = state
        self._padding = padding
        self._gw = gw
        self.tile = GRect(x, y, self._length, self._length)
        self.tile.set_fill_color("green")
        self.tile.set_filled(True)
        self._gw.add(self.tile)
        self.token = None
        self.getting_smaller = True
        self.flipping = False
    
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y

    def get_length(self):
        return self._length

    def get_state(self):
        return self._state
    
    def is_flipping(self):
        return self.flipping
    
    # True is Black
    # False is White
    def add_token(self, state):
        self.token = GOval(self.get_x() + self._padding, self.get_y() + self._padding, self.get_length() - self._padding * 2, self.get_length() - self._padding * 2)
        self.token.set_filled(True)
        if state: # Black
            self._state = True
            self.token.set_color("black")
        else: # White
            self._state = False
            self.token.set_color("white")
        self._gw.add(self.token)
    
    def flip(self):
        if self._state is not None:
            self.flipping = True
            self.flip_animation()
            self._state = not self._state
    
    def flip_animation(self):
        self.getting_smaller = True
        self.timer = self._gw.set_interval(self.move, 1)
    
    def move(self):
        speed = self.get_length() / 25
        if self.getting_smaller:
            self.token.set_bounds(self.token.get_x(), self.token.get_y() + speed, self.token.get_width(), self.token.get_height() - speed * 2)
        else:
            self.token.set_bounds(self.token.get_x(), self.token.get_y() - speed, self.token.get_width(), self.token.get_height() + speed * 2)
        if self.token.get_y() > self.get_y() + self._length / 2:
            if self.get_state(): # Black
                self.token.set_color("black")
            else: # White
                self.token.set_color("white")
            self.getting_smaller = False
            self.token.set_bounds(self.token.get_x(), self.get_y() + self.get_length() / 2, self.token.get_width(), 0)
        if self.token.get_width() <= self.token.get_height():
            self.token.set_bounds(self.get_x() + self._padding, self.get_y() + self._padding, self.get_length() - self._padding * 2, self.get_length() - self._padding * 2)
            self.stop_moving()
        
    def stop_moving(self):
        self.timer.stop()
        self.flipping = False
        

            
        
    
