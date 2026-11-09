from pgl import GWindow, GImage, GRect

GW_WIDTH = 900
GW_HEIGHT = 650

gw = GWindow(GW_WIDTH, GW_HEIGHT)


def quad_swap(pixel_array):
    """Returns a new pixel array with the quadrants swapped across the diagonals.

    Inputs:
        pixel_array (list): a 2D list of pixels (rows of columns)
    Outputs:
        (list): a new 2D list of the same size with the quadrants exchanged
    """
    height = len(pixel_array)
    width = len(pixel_array[0])
    half_h = height // 2
    half_w = width // 2

    result = []
    for r in range(height):
        row = []
        for c in range(width):
            src_r = (r + half_h) % height   # row in the opposite half
            src_c = (c + half_w) % width    # column in the opposite half
            row.append(pixel_array[src_r][src_c])
        result.append(row)
    return result

image = GImage("sample_image.png")
gw.add(image, GW_WIDTH/2 - image.get_width()/2, GW_HEIGHT/2 - image.get_height()/2)
pixel_array = image.get_pixel_array()
new_image= GImage(quad_swap(pixel_array))
gw.add(new_image, image.get_x(), image.get_y())