
from pgl import GWindow, GLabel, GRect
import random
from english import ENGLISH_WORDS

WIDTH = 500
HEIGHT = 200

gw = GWindow(WIDTH, HEIGHT)

word = random.choice(ENGLISH_WORDS).capitalize()
size = random.randint(10, 100)

Label = GLabel(word, WIDTH/2, HEIGHT/2)
Label.set_font(f"{size}pt serif")


box = GRect(Label.get_x(), Label.get_y() - Label.get_ascent(), Label.get_width(), Label.get_ascent()+ Label.get_descent())
box.set_fill_color('red')
box.set_filled(True)
gw.add(box)
gw.add(Label)