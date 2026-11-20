
from pgl import GWindow, GImage

GW_WIDTH = 900
GW_HEIGHT = 650

gw = GWindow(GW_WIDTH, GW_HEIGHT)



def quad_swap(pixel_array):
    #Find the length and width of the image
    height = len(pixel_array)
    width = len(pixel_array[0])
    #Find the new height and width
    new_height = height // 2
    new_width = width // 2
    #Create a new array
    new_array = [row[:] for row in pixel_array]
    #Go through the rows and collumns of the top left
    for r in range(new_height):
        for c in range(new_width):
        #Switch the top left and the bottom right
            new_array[r][c] = pixel_array[r + new_height][c + new_width]
            new_array[r + new_height][c + new_width] = pixel_array[r][c]
        #Switch the top right and the bottom left
            new_array[r][c + new_width] = pixel_array[r + new_height][c]
            new_array[r + new_height][c] = pixel_array[r][c + new_width]
    return new_array

   #there is no way any of this works

   #[Figure C:]

image = GImage("sample_image.png")
gw.add(image, GW_WIDTH/2 - image.get_width()/2, GW_HEIGHT/2 - image.get_height()/2)
pixel_array = image.get_pixel_array()
new_image = GImage(quad_swap(pixel_array))
gw.add(new_image, image.get_x(), image.get_y())