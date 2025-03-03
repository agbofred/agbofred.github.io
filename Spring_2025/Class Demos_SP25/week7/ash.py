############################################################
# Name: Ashton Bentley
# Name(s) of anyone worked with:
# Est time spent (hr):
############################################################

from pgl import GPoint, GPolygon, GWindow, GRect, GOval, GLabel

# Setting up initial window dimensions. 
# You can change these if you want. They are in number of pixels.
WIDTH = 600
HEIGHT = 600

GW_WIDTH = 600
GW_HEIGHT = GW_WIDTH
RADIUS_L = 0.4 * GW_WIDTH
RADIUS_M = 0.3 * RADIUS_L
RADIUS_S = 0.25 * RADIUS_M

def draw_background():
    """This function draws a background."""
    gw = GWindow(WIDTH, HEIGHT)
    cx = WIDTH / 2
    cy = HEIGHT / 2

    # base background color
    r1 = GRect(WIDTH, 90)
    r1.set_filled(True)
    r1.set_color("indigo")
    gw.add(r1)

    # Medium black upper circle
    r2 = GRect(WIDTH, 50)
    r2.set_filled(True)
    r2.set_color("purple")
    gw.add(r2, 0, 90)

    # Medium white lower circle
    r3 = GRect(WIDTH, 80)
    r3.set_filled(True)
    r3.set_color("PaleVioletRed")
    gw.add(r3, 0, 140)

    # Small white upper circle
    r4 = GRect(WIDTH, 170)
    r4.set_filled(True)
    r4.set_color("Darkorange")
    gw.add(r4, 0, 220)

    # Sun
    c5 = GOval(2 * RADIUS_M, 2 * RADIUS_M)
    c5.set_filled(True)
    c5.set_color("Orange")
    gw.add(c5, RADIUS_L+50, 230)

    # ground
    r6 = GRect(WIDTH, 210)
    r6.set_filled(True)
    r6.set_color("DimGray")
    gw.add(r6, 0, 390)


    # Draw cactus
    draw_cactus(gw, cx-150, HEIGHT - 450)  # Move cactus up from the bottom

    # Draw a title
    title = GLabel("Desert Sunset")
    title.set_font("24px 'Arial'")
    title.set_color("White")
    gw.add(title, (WIDTH - title.get_width()) / 2, 30)  # Center the title

def draw_cactus(gw, x, y):
    """This function draws a cactus with arms at the specified coordinates."""
    # Trunk
    trunk_width = 60
    trunk_height = 450  # Increased height for the trunk
    trunk = GRect(trunk_width, trunk_height)
    trunk.set_filled(True)
    trunk.set_color("DarkSlateGrey")
    gw.add(trunk, x - trunk_width / 2, y)

    # Rounded top of the trunk
    top_trunk = GOval(trunk_width, trunk_width * 0.5)
    top_trunk.set_filled(True)
    top_trunk.set_color("DarkSlateGrey")
    gw.add(top_trunk, x - trunk_width / 2, y - trunk_width * 0.25)

    # Gap between trunk and arms
    arm_gap = 40  # Distance from trunk to arms

    # Left Arm
    arm_width = 40
    arm_height = 150
    left_arm = GRect(arm_width, arm_height)
    left_arm.set_filled(True)
    left_arm.set_color("DarkSlateGrey")
    gw.add(left_arm, x - trunk_width / 2 - arm_width - arm_gap, y + trunk_height / 2 - arm_height)

    # Rounded top of the left arm
    top_left_arm = GOval(arm_width, arm_width * 0.5)
    top_left_arm.set_filled(True)
    top_left_arm.set_color("DarkSlateGrey")
    gw.add(top_left_arm, x - trunk_width / 2 - arm_width - arm_gap, y + trunk_height / 2 - arm_height - arm_width * 0.25)

    # Rounded bottom of the left arm
    bottom_left_arm = GOval(arm_width, arm_width * 0.5)
    bottom_left_arm.set_filled(True)
    bottom_left_arm.set_color("DarkSlateGrey")
    gw.add(bottom_left_arm, x - trunk_width / 2 - arm_width - arm_gap, y + trunk_height / 2)

    # Right Arm
    right_arm = GRect(arm_width, arm_height)
    right_arm.set_filled(True)
    right_arm.set_color("DarkSlateGrey")
    gw.add(right_arm, x + trunk_width / 2 + arm_gap, y + trunk_height / 2 - arm_height)

    # Rounded top of the right arm
    top_right_arm = GOval(arm_width, arm_width * 0.5)
    top_right_arm.set_filled(True)
    top_right_arm.set_color("DarkSlateGrey")
    gw.add(top_right_arm, x + trunk_width / 2 + arm_gap, y + trunk_height / 2 - arm_height - arm_width * 0.25)

    # Rounded bottom of the right arm
    bottom_right_arm = GOval(arm_width, arm_width * 0.5)
    bottom_right_arm.set_filled(True)
    bottom_right_arm.set_color("DarkSlateGrey")
    gw.add(bottom_right_arm, x + trunk_width / 2 + arm_gap, y + trunk_height / 2)

if __name__ == "__main__":
    draw_background()

