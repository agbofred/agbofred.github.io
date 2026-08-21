# File: ImageShop.py

"""
This program is the starter file for the ImageShop application, which
implements the "Load" and "Flip Vertical" buttons.
"""

from filechooser import chooseInputFile
from pgl import GWindow, GImage, GRect, GState
from GrayscaleImage import createGrayscaleImage
from ContrastStretch import stretch_contrast, create_hist_img
from button import GButton

# Constants

GWINDOW_WIDTH = 1024
GWINDOW_HEIGHT = 700
BUTTON_WIDTH = 125
BUTTON_HEIGHT = 20
BUTTON_MARGIN = 10
BUTTON_BACKGROUND = "#CCCCCC"

# Derived constants

BUTTON_AREA_WIDTH = 2 * BUTTON_MARGIN + BUTTON_WIDTH
IMAGE_AREA_WIDTH = GWINDOW_WIDTH - BUTTON_AREA_WIDTH

# The ImageShop application


def ImageShop():
    def addButton(label, action):
        """
        Adds a button to the region on the left side of the window
        """
        # nonlocal nextButtonY
        x = BUTTON_MARGIN
        y = gs.nextButtonY
        button = GButton(label, action)
        button.set_size(BUTTON_WIDTH, BUTTON_HEIGHT)
        gw.add(button, x, y)
        gs.nextButtonY += BUTTON_HEIGHT + BUTTON_MARGIN

    def setImage(image):
        """
        Sets image as the current image after removing the old one.
        """
        # nonlocal currentImage
        if gs.currentImage is not None:
            gw.remove(gs.currentImage)
        gs.currentImage = image
        x = BUTTON_AREA_WIDTH + (IMAGE_AREA_WIDTH - image.getWidth()) / 2
        y = (gw.getHeight() - image.getHeight()) / 2
        gw.add(image, x, y)

    def loadButtonAction():
        """Callback function for the Load button"""
        filename = chooseInputFile()
        if filename != "":
            setImage(GImage(filename))

    def flipVerticalAction():
        """Callback function for the FlipVertical button"""
        if gs.currentImage is not None:
            setImage(flipVertical(gs.currentImage))

    def flipHorizontalAction():
        """Callback function for the FlipHorizontal button"""
        if gs.currentImage is not None:
            setImage(flipHorizontal(gs.currentImage))

    def rotateLeftAction():
        """Callback to rotate image to the left."""
        if gs.currentImage is not None:
            setImage(rotateImage(gs.currentImage, "left"))

    def rotateRightAction():
        """Callback to rotate image to the left."""
        if gs.currentImage is not None:
            setImage(rotateImage(gs.currentImage, "right"))

    def createGrayscaleAction():
        """Callback to create grayscale image."""
        if gs.currentImage is not None:
            setImage(createGrayscaleImage(gs.currentImage))

    def greenScreenAction():
        """Callback to create green screen effect."""
        if gs.currentImage is not None:
            overlay_name = chooseInputFile()
            if overlay_name != "":
                overlay = GImage(overlay_name)
                composite = greenScreen(gs.currentImage, overlay)
                setImage(composite)

    def stretchContrastAction():
        """Callback to stretch the contrast of an image."""
        if gs.currentImage is not None:
            setImage(stretch_contrast(gs.currentImage))

    def histogramAction():
        """Callback to create a histogram image of the current image."""
        if gs.currentImage is not None:
            setImage(create_hist_img(gs.currentImage))

    def cumhistAction():
        """Callback to create a cumulative histogram image of the current image."""
        if gs.currentImage is not None:
            setImage(create_hist_img(gs.currentImage, 'cumulative'))

    gw = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT)
    gs = GState()
    buttonArea = GRect(0, 0, BUTTON_AREA_WIDTH, GWINDOW_HEIGHT)
    buttonArea.setFilled(True)
    buttonArea.setColor(BUTTON_BACKGROUND)
    gw.add(buttonArea)
    gs.nextButtonY = BUTTON_MARGIN
    gs.currentImage = None
    addButton("Load", loadButtonAction)
    addButton("Flip Vertical", flipVerticalAction)
    addButton("Flip Horizontal", flipHorizontalAction)
    addButton("Rotate Left", rotateLeftAction)
    addButton("Rotate Right", rotateRightAction)
    addButton("Turn Gray", createGrayscaleAction)
    addButton("Green Screen", greenScreenAction)
    addButton("Stretch Contrast", stretchContrastAction)
    addButton("Histogram", histogramAction)
    addButton("Cumulative Hist", cumhistAction)


# Creates a new GImage from the original one by flipping it vertically.


def flipVertical(image):
    array = image.getPixelArray()
    return GImage(array[::-1])


def flipHorizontal(image):
    array = image.getPixelArray()
    return GImage([row[::-1] for row in array])


def rotateImage(image, direction):
    old_col, old_row = image.getWidth(), image.getHeight()
    new_col, new_row = image.getHeight(), image.getWidth()
    array = image.getPixelArray()
    new_array = [[0] * new_col for _ in range(new_row)]
    for row in range(old_row):
        for col in range(old_col):
            if direction.lower() == "left":
                new_array[new_row - col - 1][row] = array[row][col]
            elif direction.lower() == "right":
                new_array[col][new_col - row - 1] = array[row][col]
    return GImage(new_array)


def greenScreen(image1, image2):
    background = image1.getPixelArray()
    foreground = image2.getPixelArray()
    for row in range(image1.getHeight()):
        for col in range(image1.getWidth()):
            if row < image2.get_height() and col < image2.get_width():
                pix = foreground[row][col]
                r, g, b = GImage.get_red(pix), GImage.get_green(pix), GImage.get_blue(pix)
                if not ((g > 2 * r) and (g > 2 * b)):
                    background[row][col] = foreground[row][col]
    return GImage(background)


# Startup code

if __name__ == "__main__":
    ImageShop()
