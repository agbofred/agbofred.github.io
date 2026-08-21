######################################################################
# Name:
# Collaborators (if any):
# Section leader's name:
# List of extensions made (if any):
######################################################################

"""
This program is the starter file for the ImageShop application, which
implements the "Load" and "Flip Vertical" buttons.
"""

from filechooser import choose_input_file
from pgl import GWindow, GImage, GRect
from button import GButton
from GrayscaleImage import grayscale_image, create_grayscale_image

# Constants

GWINDOW_WIDTH = 900
GWINDOW_HEIGHT = 500
BUTTON_WIDTH = 125
BUTTON_HEIGHT = 20
BUTTON_MARGIN = 10
BUTTON_BACKGROUND = "#CCCCCC"

# Derived constants

BUTTON_AREA_WIDTH = 2 * BUTTON_MARGIN + BUTTON_WIDTH
IMAGE_AREA_WIDTH = GWINDOW_WIDTH - BUTTON_AREA_WIDTH

# The image_shop application

def image_shop():
    def add_button(label, action):
        """
        Adds a button to the region on the left side of the window
        label is the text that will be displayed on the button and
        action is the callback function that will be run when the
        button is clicked.
        """
        x = BUTTON_MARGIN
        y = gw.next_button_y
        button = GButton(label, action)
        button.set_size(BUTTON_WIDTH, BUTTON_HEIGHT)
        gw.add(button, x, y)
        gw.next_button_y += BUTTON_HEIGHT + BUTTON_MARGIN

    def set_image(image):
        """
        Sets image as the current image after removing the old one.
        """
        if gw.current_image is not None:
            gw.remove(gw.current_image)
        gw.current_image = image
        x = BUTTON_AREA_WIDTH + (IMAGE_AREA_WIDTH - image.get_width()) / 2
        y = (gw.get_height() - image.get_height()) / 2
        gw.add(image, x, y)

    def load_button_action():
        """Callback function for the Load button"""
        filename = choose_input_file()
        if filename != "":
            set_image(GImage(filename))

    def flip_vertical_action():
        """Callback function for the Flip Vertical button"""
        if gw.current_image is not None:
            set_image(flip_vertical(gw.current_image))
    
    # Flip Horizontal call back function
    def flip_horizontal_action():
        """Callback function for the Flip Vertical button"""
        if gw.current_image is not None:
            set_image(flip_horizontal(gw.current_image))
            
    # Rotate right call back function
    def rotate_right_action():
        """Callback function for the Flip Vertical button"""
        if gw.current_image is not None:
            set_image(rotate_right(gw.current_image))
            
    # Rotate right call back function
    def rotate_left_action():
        """Callback function for the Flip Vertical button"""
        if gw.current_image is not None:
            set_image(rotate_left(gw.current_image))
            
    # Rotate right call back function
    def grayscale_action():
        """Callback function for the Flip Vertical button"""
        if gw.current_image is not None:
            set_image(create_grayscale_image(gw.current_image))
    
        
    gw = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT)
    button_area = GRect(0, 0, BUTTON_AREA_WIDTH, GWINDOW_HEIGHT)    
    button_area.set_filled(True)
    button_area.set_color(BUTTON_BACKGROUND)
    gw.add(button_area)
    gw.next_button_y = BUTTON_MARGIN
    gw.current_image = None
    add_button("Load", load_button_action)
    add_button("Flip Vertical", flip_vertical_action)
    add_button("Flip Horizontal", flip_horizontal_action)
    add_button("Rotate Left", rotate_left_action)
    add_button("Rotate right", rotate_right_action)
    add_button("Grayscale", grayscale_action)

# Creates a new GImage from the original one by flipping it vertically.

def flip_vertical(image):
    array = image.get_pixel_array()
    return GImage(array[::-1])

def flip_horizontal(image): # Flip horinzontal method
    array= image.get_pixel_array()
    for r in range(len(array)):
        array[r]= array[r][::-1]
    return GImage(array)

def rotate_right(image):  # Rotate right function
    array = image.get_pixel_array()
    row = len(array)
    col = len(array[0])
   
    #new_arr_right= [[array[i][col-1-j] for i in range(row)] for j in range(col)]
    new_arr_right= [[array[j][i] for j in range(row-1,-1,-1)] for i in range(col)]
    
    #Line 131 - 134 is an alternative was to do the same thing on line 28
    # new_arr= [[0 for _ in range(row)] for _ in range(col)]
    # for j in range(row - 1, -1, -1):
    #     for i in range(col):
    #         new_arr[j][i] = array[i][j]
    return GImage(new_arr_right)


def rotate_left(image):  # Rotate left function
    array = image.get_pixel_array()
    row = len(array)
    col = len(array[0])
    #new_arrleft= [[array[j][i] for j in range(row-1,-1,-1)] for i in range(col)]
    new_arrleft= [[array[j][i] for j in range(row)] for i in range(col-1,-1,-1)]
    
    # new_arr= [[0 for _ in range(row)] for _ in range(col)]
    # for i in range(row):
    #     for j in range(col):
    #         new_arr[i][col - 1 - j] = array[i][j]
    return GImage(new_arrleft)
# Startup code

if __name__ == "__main__":
    image_shop()
