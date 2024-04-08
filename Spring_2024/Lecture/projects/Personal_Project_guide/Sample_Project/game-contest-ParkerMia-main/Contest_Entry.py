# Name: Mia Parker
from pgl import GWindow
from difficultyinterface import start_screen

W_WIDTH = 600
W_HEIGHT = 750

#This is the screen that plays everything and opens the GWindow
def hangman():
    gw = GWindow(W_WIDTH, W_HEIGHT)
    start_screen(gw, W_WIDTH, W_HEIGHT)

if __name__ == "__main__":
    hangman()

# Now you are free to import whatever you need and take it from here!
# I'm excited to play these!
