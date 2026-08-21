import arcade

import math
import random

WIDTH = 600
HEIGHT = 600


def draw_sky():
    arcade.draw_lrtb_rectangle_filled(
        0, WIDTH, HEIGHT * 4 / 5, HEIGHT * 1 / 2, (110, 59, 130)
    )
    arcade.draw_lrtb_rectangle_filled(
        0, WIDTH, HEIGHT * 3 / 4, HEIGHT * 1 / 2, (221, 108, 149)
    )
    arcade.draw_lrtb_rectangle_filled(
        0, WIDTH, HEIGHT * 2 / 3, HEIGHT * 1 / 2, (253, 128, 88)
    )


def draw_sun(t=0):
    sun_h = HEIGHT / 2 - 50*math.sin(0.1*t)
    arcade.draw_circle_filled(WIDTH * 2 / 3, sun_h, 50, (253, 157, 88))


def draw_water(t=0):
    layer1_y = 100 + 5*math.sin(2*t)
    layer2_y = 5*math.sin(3*t) + layer1_y + 50
    arcade.draw_xywh_rectangle_filled(0, layer1_y, WIDTH, 55, (110, 59, 130))
    arcade.draw_xywh_rectangle_filled(0, layer2_y, WIDTH, 75, (221, 108, 149))
    arcade.draw_xywh_rectangle_filled(0, HEIGHT * 0.5, WIDTH, -100, (253, 128, 88))
    # arcade.draw_lrtb_rectangle_filled(
    # 0, WIDTH, HEIGHT * 1 / 4, HEIGHT * 1 / 5, (110, 59, 130)
    # )
    # arcade.draw_lrtb_rectangle_filled(
    # 0, WIDTH, HEIGHT * 1 / 3, HEIGHT * 1 / 4, (221, 108, 149)
    # )
    # arcade.draw_lrtb_rectangle_filled(
    # 0, WIDTH, HEIGHT * 1 / 2, HEIGHT * 1 / 3, (253, 128, 88)
    # )
    arcade.draw_lrtb_rectangle_filled(0, WIDTH, HEIGHT / 2, 0, (0, 0, 50, 200))


def draw_shoreline():
    x = 0
    while x < WIDTH:
        step = 5
        arcade.draw_lrtb_rectangle_filled(
            x,
            x + step,
            HEIGHT / 2 + 20 * math.exp(-0.01 * x),
            HEIGHT / 2 - 30 * math.exp(-0.005 * x),
            arcade.color.BLACK,
        )
        x += step


def draw_buildings(t=0):
    rot_angle = -40 - 10*math.sin(0.1*t)
    random.seed(100)
    x = 50
    while x < 200:
        h = random.randint(25, 100)
        arcade.draw_lrtb_rectangle_filled(
            x, x + 25, HEIGHT / 2 + h, HEIGHT / 2, arcade.color.BLACK
        )
        arcade.draw_rectangle_filled(x-5-5*math.sin(0.1*t), HEIGHT / 2 - h / 3, 25, h, (0, 0, 0, 100), rot_angle)
        x += random.randint(30, 50)


def draw_boat(boat_x, boat_y, boat_w, boat_h):
    # Bottom
    arcade.draw_rectangle_filled(boat_x, boat_y, boat_w, boat_h, (0, 0, 0))
    arcade.draw_triangle_filled(
        boat_x - boat_w / 2,
        boat_y - boat_h / 2,
        boat_x - boat_w / 2,
        boat_y + boat_h / 2,
        boat_x - boat_w,
        boat_y + boat_h / 2,
        (0, 0, 0),
    )
    # Mast
    arcade.draw_lrtb_rectangle_filled(
        boat_x - 5, boat_x + 5, boat_y + 400, boat_y, (0, 0, 0)
    )
    # Sail left
    arcade.draw_triangle_filled(
        boat_x - 10,
        boat_y + 400,
        boat_x - boat_w,
        boat_y + boat_h / 2 + 10,
        boat_x - 10,
        boat_y + boat_h / 2 + 10,
        (0, 0, 0),
    )
    # Sail right
    arcade.draw_triangle_filled(
        boat_x + 10,
        boat_y + 400,
        boat_x + boat_w,
        boat_y + boat_h / 2 + 10,
        boat_x + 10,
        boat_y + boat_h / 2 + 10,
        (0, 0, 0),
    )


def draw_cloud(cloud_x, cloud_y):
    x = cloud_x - 50
    while x <= cloud_x + 50:
        dist = cloud_x - x
        arcade.draw_circle_filled(
            x, cloud_y, 20 * math.exp(-0.01 * abs(dist)), (180, 132, 174,)
        )
        x += 25


def on_draw(dt):
    arcade.start_render()
    draw_sky()
    draw_sun(on_draw.time)
    draw_water(on_draw.time)
    draw_shoreline()
    draw_cloud(on_draw.cloud_p1, 500)
    draw_cloud(on_draw.cloud_p2, 350)
    draw_buildings(on_draw.time)
    draw_boat(500, 100+10*math.sin(on_draw.time), 200, 50)
    on_draw.cloud_p1 += 20 * dt
    on_draw.cloud_p2 -= 30 * dt
    if on_draw.cloud_p1 > 700:
        on_draw.cloud_p1 = -100
    if on_draw.cloud_p2 < -100:
        on_draw.cloud_p2 = 700
    on_draw.time += dt

    alpha = int(100 + 50*math.sin(0.1 * on_draw.time))
    arcade.draw_lrtb_rectangle_filled(0, WIDTH, HEIGHT, 0, (0, 0, 0, alpha))

    # arcade.get_image().save(f'ImageDump/test_{on_draw.i:03d}.png', "PNG")
    # on_draw.i += 1


def main():
    on_draw.i = 0
    on_draw.cloud_p1 = 0
    on_draw.cloud_p2 = 600
    on_draw.time = 0
    arcade.open_window(WIDTH, HEIGHT, "Problem 4")
    arcade.set_background_color((46, 23, 105))
    arcade.schedule(on_draw, 1 / 60)
    arcade.finish_render()
    arcade.run()


main()
