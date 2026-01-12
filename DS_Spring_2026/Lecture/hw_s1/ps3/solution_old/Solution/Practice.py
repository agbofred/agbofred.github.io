def calc_savings():
    payroll = int(input("Enter your monthly salary: "))
    savings_rate = float(input("Enter the percent to save (as decimal): "))
    num_months = int(input("Enter the amount of months you'd like to save for: "))

    interest_rate = 0.03

    savings = 0
    for month in range(num_months):
        savings += payroll * savings_rate + savings * interest_rate / 12
    print("Amount saved:", round(savings, 2))


def calc_rate():
    payroll = int(input("Enter the amount you are paid each month: "))
    num_months = int(input("Enter the amount of months you'd like to save for: "))
    goal_savings = int(input("Enter the amount you'd like to have in savings: "))

    epsilon = 25
    low = 0
    high = 1

    savings = 0
    interest_rate = 0.03
    savings_rate = 0.5
    step = 0

    while abs(goal_savings - savings) > epsilon and step < 100:
        savings = 0
        for month in range(num_months):
            savings += payroll * savings_rate + savings * interest_rate / 12

        if savings > goal_savings:
            high = savings_rate
        else:
            low = savings_rate
        savings_rate = (low + high) / 2
        step += 1

    print("Necessary savings rate is:", savings_rate)
    print("Steps taken to find rate:", step)


def consecutive_heads(des_num):
    import random

    num_heads = 0
    count = 0
    while num_heads < des_num:
        flip = random.choice(["Heads", "Tails"])
        print(flip)
        if flip == "Heads":
            num_heads += 1
        else:
            num_heads = 0
        count += 1
    print("It took", count, "tosses to get", des_num, "consecutive heads.")


def always_watching():
    from pgl import GWindow, GState, GOval, GRect, GLine
    import math
    import exlib

    def draw_face():
        head = GOval(300 - 150, 300 - 200, 300, 400)
        head.set_filled(True)
        head.set_color("orange")
        gw.add(head)

        # mouth
        gw.add(exlib.create_filled_rect(300, 400, 200, 20, "red"))

        # eyes
        gw.add(exlib.create_filled_circle(250, 200, 25, "white"))
        gw.add(exlib.create_filled_circle(350, 200, 25, "white"))

    def get_heading(x1, y1, x2, y2):
        return math.atan2((y2 - y1), (x2 - x1))

    def get_displacements(mx, my, px, py, d=10):
        D = ((mx-px)**2 + (my-py)**2)**0.5
        return d*(mx-px) / D, d*(my-py) / D

    def mousemove_action(e):
        mx = e.get_x()
        my = e.get_y()
        # lhead = get_heading(250, 200, mx, my)
        ldx, ldy = get_displacements(mx, my, PUPIL_LX, PUPIL_LY)
        rdx, rdy = get_displacements(mx, my, PUPIL_RX, PUPIL_RY)
        gs.l_pupil.set_location(PUPIL_LX+ldx-10, PUPIL_LY+ldy-10)
        gs.r_pupil.set_location(PUPIL_RX+rdx-10, PUPIL_RY+rdy-10)

    gw = GWindow(600, 600)
    gs = GState
    PUPIL_RX, PUPIL_RY = 350, 200
    PUPIL_LX, PUPIL_LY = 250, 200
    gs.r_pupil = exlib.create_filled_circle(PUPIL_RX, PUPIL_RY, 10)
    gs.l_pupil = exlib.create_filled_circle(PUPIL_LX, PUPIL_LY, 10)
    draw_face()
    gw.add(gs.r_pupil)
    gw.add(gs.l_pupil)

    gw.add_event_listener("mousemove", mousemove_action)


def estimate_pi():
    from pgl import GWindow, GOval, GLabel
    from exlib import create_centered_label, create_filled_circle
    import random

    SIZE = 500
    RADIUS = SIZE / 2
    TRIES = 10000

    def take_shot(hits):
        x = random.random()*SIZE
        y = random.random()*SIZE
        is_hit = (x-RADIUS)**2 + (y-RADIUS)**2 < (RADIUS)**2
        if is_hit:
            color = "red"
            hits += 1
        else:
            color = "black"
        gw.add(create_filled_circle(x,y,1,color))
        return hits


    gw = GWindow(SIZE, SIZE)
    hits = 0
    target = create_filled_circle(RADIUS,RADIUS,RADIUS,"#63acbe")
    gw.add(target)


    for i in range(TRIES):
        hits = take_shot(hits)
    print(hits/TRIES*4)

    lab = GLabel(str(round(hits/TRIES*4,2)),0,0)
    lab.set_font("bold 100px 'serif'")
    lab.set_color("white")
    x = SIZE / 2 - lab.get_width() / 2
    y = SIZE / 2 + lab.get_ascent() / 2
    gw.add(lab, x, y)


if __name__ == "__main__":
    # calc_rate()
    # calc_savings()
    # consecutive_heads(3)
    always_watching()
    # estimate_pi()
