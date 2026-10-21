from pgl import GWindow, GImage, GRect

GW_WIDTH = 900
GW_HEIGHT = 650

gw = GWindow(GW_WIDTH, GW_HEIGHT)

rect = GRect(0,0,GW_WIDTH, GW_HEIGHT)
rect.set_fill_color("darkblue")
rect.set_filled(True)
gw.add(rect)

image = GImage("Moon.png")
gw.add(image, GW_WIDTH/2 - image.get_width()/2, GW_HEIGHT/2 - image.get_height()/2)

pixel_array = image.get_pixel_array()
image_height = len(pixel_array)
image_width = len(pixel_array[0])

count =0 
for r in range(image_height):
    for c in range(image_width):
        value = pixel_array[r][c]
        brightness = GImage.get_red(value)
     
        if brightness < 100:
            # count +=1
            # print(count)
            pixel_array[r][c] = GImage.create_rgb_pixel(1,2,1)
        else:
            pixel_array[r][c] = GImage.create_rgb_pixel(255,255,255)
new_image= GImage(pixel_array)
gw.add(new_image, image.get_y(), image.get_y())