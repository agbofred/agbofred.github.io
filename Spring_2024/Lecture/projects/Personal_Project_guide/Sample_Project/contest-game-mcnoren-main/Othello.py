# Name: Matthew Noren

"""
Othello is a board game where you compete with another player to flip over the most tiles to your designated color.
Feel free to change the number of tiles on the board with the 'size' variable defined in this file.
Run this file to run the Othello game.
"""

# Now you are free to import whatever you need and take it from here!
# I'm excited to play these!

from OthelloGame import OthelloGame

def othello():
    size = 8 # this variable represents the number of tiles across the length and width of the board
    game = OthelloGame(size)
    game.run()

if __name__ == "__main__":
    othello()
