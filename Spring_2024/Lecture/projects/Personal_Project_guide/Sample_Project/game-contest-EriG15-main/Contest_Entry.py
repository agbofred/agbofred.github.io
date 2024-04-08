# Name: Erik Griswold
# File: Contest_Entry.py
# Uses: pgl.py & sudoku_logo.png

"""
This file creates a game of Sudoku. When Sudoku window is opened, the player can select their difficulty 
mode. The goal of the game is to fill in all of the numbers without having any repeating numbers in any 
columns, rows, or blocks (3 x 3 sections of the grid). To play, click on any unfilled square and enter 
a number. If you want to make a square blank again, click the space or backspace key. When you think you
have won the game, click the enter key to check your entries. Good luck!
"""

from pgl import GWindow, GRect, GLabel, GImage
import random

# constants

GLABEL_GRID = [[] for i in range(9)]       # 2 dimensional array for storing variables

GWINDOW_SIZE = 901                         # size of the window
INSET = 50                                 # size of the board's inset

GRID_SIZE = GWINDOW_SIZE - INSET * 2       # size of the entire grid
SQUARE_SIZE = GRID_SIZE // 9               # size of each square
BLOCK_SIZE = GRID_SIZE // 3                # size of each block

GRID_COLOR = "#959595"                     # color for all boarders on the gameboard
FILLED_SQUARE_COLOR = "#E1E1E1"            # color for a square that has its number pre-defined
SELECT_COLOR = "#E8C8FF"                   # color for a selected square that does not have its number pre-defined
FILLED_SELECT_COLOR = "#B9A0CC"            # color for a selected square that has its number pre-defined

EASY_MODE = 38                             # number of filled in squares for easy mode
MEDIUM_MODE = 30                           # number of filled in squares for medium mode
HARD_MODE = 23                             # number of filled in squares for hard mode

# gw variables

gw = GWindow(GWINDOW_SIZE,GWINDOW_SIZE)    # creating the application window

gw.first_action = True                     # changed to false later to begin the game
gw.highlighted = GRect(1,1,0,0)            # refers to the highlighted square
gw.selected_is_const = True                # boolean on if the currently selected square is a constant
gw.click_col = 0                           # currently clicked square's column index
gw.click_row = 0                           # currently clicked square's row index


def create_starter():
    """This function creates the starting screen where the player selects a difficulty mode."""

    # adding sudoku logo
    logo = GImage("sudoku_logo.png")
    array = logo.get_pixel_array()
    gw.add(logo, GWINDOW_SIZE // 2 - len(array[0]) // 2, 200)

    # box for difficulty level general text
    difficulty_starter = GRect(650,80)
    difficulty_starter.set_line_width(5)
    gw.add(difficulty_starter, 125,350)

    # text for difficulty level general
    difficulty_text = GLabel("CHOOSE DIFFICULTY LEVEL")
    difficulty_text.set_font("bold 34pt 'serif'")
    gw.add(difficulty_text,135,405)

    # boxes for each difficulty level
    for i in range(3):
        difficulty_level = GRect(191,75)
        difficulty_level.set_line_width(5)
        gw.add(difficulty_level, 125 + i * 229, 475)

    # text for easy level
    gw.easy_text = GLabel("EASY")
    gw.easy_text.set_font("bold 35pt 'serif'")
    gw.add(gw.easy_text,157,530)

    # text for medium level
    gw.medium_text = GLabel("MEDIUM")
    gw.medium_text.set_font("bold 34.5pt 'serif'")
    gw.add(gw.medium_text,358,530)

    # text for hard level
    gw.hard_text = GLabel("HARD")
    gw.hard_text.set_font("bold 35pt 'serif'")
    gw.add(gw.hard_text,612,530)


def fill_window():
    """Creates and fills in the initial Sudoku board."""
    
    # making 9x9 grid
    for i in range(9):
        for j in range(9): 

                square_fill = GRect(INSET + j * SQUARE_SIZE, INSET + i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                square_fill.set_filled(True)      
                if gw.SUDOKU_GRID[j][i] != 0:
                    square_fill.set_color(FILLED_SQUARE_COLOR)
                else:
                    square_fill.set_color("#FFFFFF")
                gw.add(square_fill)

                square = GRect(INSET + j * SQUARE_SIZE, INSET + i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                square.set_line_width(1)
                square.set_color(GRID_COLOR)
                gw.add(square)

    # making 3x3 grid
    for i in range(3):
         for j in range(3):
                
                square = GRect(INSET + j * BLOCK_SIZE, INSET + i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                square.set_line_width(4)
                square.set_color(GRID_COLOR)
                gw.add(square)

    # making border for grid
    gw.border = GRect(INSET, INSET, GRID_SIZE, GRID_SIZE)
    gw.border.set_line_width(4)
    gw.add(gw.border)

    # displaying numbers
    for i in range(9):
        for j in range(9):
                if gw.SUDOKU_GRID[j][i] != 0:
                    number = GLabel(str(gw.SUDOKU_GRID[j][i]))
                    number.set_font("bold 45pt 'serif'")
                    gw.add(number, INSET + j * SQUARE_SIZE + (SQUARE_SIZE // 2 - number.get_width() // 2), INSET + i * SQUARE_SIZE + number.get_height())
                    GLABEL_GRID[i].append(number)
                else:
                    number = GLabel("0")
                    number.set_font("bold 45pt 'serif'")
                    gw.add(number, INSET + j * SQUARE_SIZE + (SQUARE_SIZE // 2 - number.get_width() // 2), INSET + i * SQUARE_SIZE + number.get_height())
                    GLABEL_GRID[i].append(number)
                    number.set_label(" ")


def generate_numbers(GAME_MODE):
    """Function randomly generates numbers for the board without having repeats within any rows, colomns, or blocks."""

    # configuring board
    def pattern(row,col): 
        return (3 * (row % 3) + row // 3 + col ) % 9

    rows  = [ value * 3 + row for value in random.sample(range(3), len(range(3))) for row in random.sample(range(3), len(range(3))) ] 
    cols  = [ value * 3 + col for value in random.sample(range(3), len(range(3))) for col in random.sample(range(3), len(range(3))) ]
    nums  = random.sample((range(1, 10)), len((range(1, 10))))

    gw.SUDOKU_GRID = [ [nums[pattern(row, col)] for col in cols] for row in rows ]


    # removing numbers
    to_remove = 81 - GAME_MODE # CAN BE CHANGED TO GET MORE OR LESS STARTING BLOCKS

    i = 0
    while i < to_remove:
        r_col = random.randint(0,8)
        r_row = random.randint(0,8)

        if gw.SUDOKU_GRID[r_col][r_row] != 0:
            gw.SUDOKU_GRID[r_col][r_row] = 0
            i += 1

    gw.USER_GRID = gw.SUDOKU_GRID


def find_square(x,y):
    """Returns what square a GRect is in."""

    return (x-INSET)//SQUARE_SIZE, (y-INSET)//SQUARE_SIZE


def highlight(x,y):
    """Algorithm for selecting and highlighting a square."""

    # removing last highlighted square
    if gw.selected_is_const == False:
        gw.highlighted.set_fill_color("#FFFFFF")
    else:
        gw.highlighted.set_fill_color(FILLED_SQUARE_COLOR)
    
    # getting to current square (inneficient method, but does not affect performance significantly)
    gw.remove(gw.border)

    block = gw.get_element_at(INSET + x * SQUARE_SIZE, INSET + y * SQUARE_SIZE)
    gw.remove(block)

    square_outline = gw.get_element_at(INSET + x * SQUARE_SIZE, INSET + y * SQUARE_SIZE)
    gw.remove(square_outline)

    square = gw.get_element_at(INSET + x * SQUARE_SIZE, INSET + y * SQUARE_SIZE)

    gw.add(square_outline)
    gw.add(block)
    gw.add(gw.border)

    # highlighting square
    if square.get_color() == "#FFFFFF":
        square.set_fill_color(SELECT_COLOR)
        gw.selected_is_const = False
    else:
        square.set_fill_color(FILLED_SELECT_COLOR)
        gw.selected_is_const = True
        
    
    gw.highlighted = square


def check_game():
    """Returns a boolean for if the game has been successfully completed"""

    sudoku_completed = True

    for i in range(9):
        for j in range(9):
            for k in range(9):
                if (gw.USER_GRID[i][j] == gw.USER_GRID[k][j] and i != k) or (gw.USER_GRID[i][j] == gw.USER_GRID[i][k] and j != k) or gw.USER_GRID[i][j] == 0:
                    sudoku_completed = False
                    
    return sudoku_completed


def you_win():
    """Runs code for when game is successfully completed"""

    try:
        gw.remove(gw.winning_message)
    except:
        pass
    try:
        gw.remove(gw.persistence_message)
    except:
        pass
    gw.winning_message = GLabel("You win!")
    gw.winning_message.set_font("bold 30pt 'serif'")
    gw.add(gw.winning_message,370,38)


def try_again():
    """Runs code for if game is not yet successfully completed"""

    def remove_persistence():
        gw.remove(gw.persistence_message)
    try:
        gw.remove(gw.winning_message)
    except:
        pass
    try:
        gw.remove(gw.persistence_message)
    except:
        pass
    gw.persistence_message = GLabel("Try again!")
    gw.persistence_message.set_font("bold 30pt 'serif'")
    gw.add(gw.persistence_message,350,38)
    gw.set_timeout(remove_persistence, 1000)


def click_action(click):
    """Determines what to do based on where mouse is clicked."""
    
    # determining difficulty mode at beginning of game.
    if gw.first_action == True:
        
        # if any of the three conditions below are activated, could will be carried out to initialize game based on difficulty mode.

        if gw.easy_text.contains(click.get_x(),click.get_y()):
            gw.first_action = False
            gw.clear()
            generate_numbers(EASY_MODE)
            fill_window()

        elif gw.medium_text.contains(click.get_x(),click.get_y()):
            gw.first_action = False
            gw.clear()
            generate_numbers(MEDIUM_MODE)
            fill_window()

        elif gw.hard_text.contains(click.get_x(),click.get_y()):
            gw.first_action = False
            gw.clear()
            generate_numbers(HARD_MODE)
            fill_window()

    # determining click action for when in the game
    elif gw.get_element_at(click.get_x(),click.get_y()) != None:
        gw.click_col, gw.click_row = find_square(click.get_x(),click.get_y())
        highlight(gw.click_col,gw.click_row)
        

def key_action(key):
    """Function for determining action based on key press once in the game."""

    if gw.first_action == False:

        # if key is a non-zero number and selected square is mutable.
        if key.get_key().isnumeric() == True and gw.selected_is_const == False and key.get_key() != "0":
            GLABEL_GRID[gw.click_row][gw.click_col].set_label(key.get_key())
            GLABEL_GRID[gw.click_row][gw.click_col].send_to_front()
            gw.USER_GRID[gw.click_col][gw.click_row] = int(key.get_key())
        
        # if key is space or backspace
        elif key.get_key() == "<SPACE>" or key.get_key() == "<BACKSPACE>":
            GLABEL_GRID[gw.click_row][gw.click_col].set_label(" ")
            GLABEL_GRID[gw.click_row][gw.click_col].send_to_front()
            gw.USER_GRID[gw.click_col][gw.click_row] = 0
        
        elif key.get_key() == "<RETURN>":
            if check_game() == True: 
                you_win()
            else:
                try_again()


def play_sudoku():
    """This function will begin the game."""
    
    create_starter()
    gw.add_event_listener("click",click_action)
    gw.add_event_listener("key",key_action)


play_sudoku()