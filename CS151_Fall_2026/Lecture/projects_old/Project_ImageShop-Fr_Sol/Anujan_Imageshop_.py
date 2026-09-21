######################################################################
# Name: Anujan Tennathur 
# Collaborators (if any): Aadem Isai
# Section leader's name: Saul
# List of extensions made (if any):
######################################################################

"""
This program is the starter file for the ImageShop application, which
implements the "Load" and "Flip Vertical" buttons.
"""

from GrayscaleImage import create_grayscale_image
from filechooser import choose_input_file, chooseInputFile
from pgl import GWindow, GImage, GRect
from button import GButton

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
    
    def flip_horizontal_action():
        if gw.current_image is not None:
            set_image(flip_horizontal(gw.current_image))

    def remove_red_action():
        if gw.current_image is not None:
            set_image(remove_red(gw.current_image))
        
    def flip_right_action():
        if gw.current_image is not None:
            set_image(flip_right(gw.current_image))

    def flip_left_action():
        if gw.current_image is not None:
            set_image(flip_left(gw.current_image))
    
    def convert_to_grayscale_action():
        if gw.current_image is not None:
            set_image(create_grayscale_image(gw.current_image))

    def green_screen_action():
        if gw.current_image is None:
            print("Error: No image loaded. Please load an image first.")
            return
        
        new_image_filename = chooseInputFile()
        background_image = gw.current_image
        green_screen_image = GImage(new_image_filename)

        bg_array = background_image.get_pixel_array()
        gs_array = green_screen_image.get_pixel_array()

        min_height = min(len(bg_array), len(gs_array))
        min_width = min(len(bg_array[0]), len(gs_array[0]))

        for r in range(background_image.get_height()):
            for c in range(background_image.get_width()):
                if r < green_screen_image.get_height() and c < green_screen_image.get_width():
                    pix = gs_array[r][c]
                r, g, b = GImage.get_red(pix), GImage.get_green(pix), GImage.get_blue(pix)
                if not ((g > 2 * r) and (g > 2 * b)):
                    bg_array[r][c] = gs_array[r][c]

        """for r in range(min_height):
            for c in range(min_width):
                bg_pixel = bg_array[r][c]
                gs_pixel = gs_array[r][c]
                
                bg_red = GImage.get_red(bg_pixel)
                bg_green = GImage.get_green(bg_pixel)
                bg_blue = GImage.get_blue(bg_pixel)

                gs_red = GImage.get_red(gs_pixel)
                gs_green = GImage.get_green(gs_pixel)
                gs_blue = GImage.get_blue(gs_pixel)

                if gs_green >= 2 * max(gs_red, gs_blue):
                    new_red = gs_red
                    new_green = gs_green
                    new_blue = gs_blue
                    bg_array[r][c] = GImage.create_rgb_pixel(new_red, new_green, new_blue)
"""
        result_image = GImage(bg_array)
        set_image(result_image)





        
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
    add_button("Remove Red", remove_red_action)
    add_button("Rotate Right", flip_right_action)
    add_button("Rotate Left", flip_left_action)
    add_button("Convert to Grayscale", convert_to_grayscale_action)
    add_button("Green Screen", green_screen_action)



# Creates a new GImage from the original one by flipping it vertically.

def flip_vertical(image):
    array = image.get_pixel_array()
    return GImage(array[::-1])

# Creates a new GImage from the original one by flipping it horizontally.

def flip_horizontal(image):
    array = image.get_pixel_array()
    flipped_array = [row[::-1] for row in array]
    return GImage(flipped_array)

def remove_red(image):
    array = image.get_pixel_array()
    height = len(array)
    width = len(array[0])
    for r in range(height):
        for c in range(width):
            pixel = array[r][c]
            green = GImage.get_green(pixel)
            blue = GImage.get_blue(pixel)
            red = GImage.get_red(pixel)
            if red >= 2 * max(green, blue):
                red = max(green, blue)
            array[r][c] = GImage.create_rgb_pixel(red, green, blue)
    return GImage(array)

def flip_right(image):
    array = image.get_pixel_array()
    rows, cols = len(array), len(array[0])
    rotated_right = [[array[i][cols - 1 - j] for i in range(rows)] for j in range(cols)]
    return GImage(rotated_right)
    
def flip_left(image):
    array = image.get_pixel_array()
    rows, cols = len(array), len(array[0])
    rotated_left = [[array[j][i] for j in range(rows - 1, -1, -1)] for i in range(cols)]
    return GImage(rotated_left)


# Startup code

if __name__ == "__main__":
    image_shop()
