def do_buble():
    def make_circle(x,y,r):
        c = GOval(x-r, y-r, 2*r, 2*r)
        c.set_filled(True)
        if random.randint(1, 100) > 75:
            c.set_color("#F92672") #pink
        else:
            c.set_color("#66D9EF") #blue
        return c
    def make_buble_action(e):
        for i in range(50):
            gw.add(make_circle(
                    random.randint(50,450), 
                    random.randint(50,450), 
                    random.randint(5,50)
                    )
                )
    gw = GWindow(500, 500)
    
    gw.add_event_listener("dblclick",make_buble_action)

do_buble()