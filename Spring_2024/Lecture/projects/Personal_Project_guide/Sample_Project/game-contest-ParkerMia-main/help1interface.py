# Name: Mia Parker
from pgl import GRect, GOval, GLabel, GCompound

#describes the choices available on the start screen
def help_screen(gw, chooses):
    helps = GCompound()
    items = {}
    #creates the explanation for difficulties and exit button
    def format():
        box = GRect(125, 156, 350, 437)
        helps.add(box)
        label = GLabel("Help", 235, 215)
        label.set_font("50px 'copperplate'")
        helps.add(label)
        easy = GLabel("Easy: plays with words with 3 letters", 135, 300)
        easy.set_font("20px 'avenir'")
        helps.add(easy)
        easy = GLabel("or fewer", 150, 330)
        easy.set_font("20px 'avenir'")
        helps.add(easy)
        medium = GLabel("Medium: plays with words with 4 to 6", 135, 380)
        medium.set_font("20px 'avenir'")
        helps.add(medium)
        medium = GLabel("letters", 150, 410)
        medium.set_font("20px 'avenir'")
        helps.add(medium)
        hard = GLabel("Hard: plays with words with 7 letters", 135, 460)
        hard.set_font("20px 'avenir'")
        helps.add(hard)
        hard = GLabel("or more", 150, 490)
        hard.set_font("20px 'avenir'")
        helps.add(hard)
        custom = GLabel("Custom: play with 2 or more players", 135, 540)
        custom.set_font("20px 'avenir'")
        helps.add(custom)
        custom = GLabel("by using a word of your choosing", 150, 570)
        custom.set_font("20px 'avenir'")
        helps.add(custom)
        circle = GOval(127, 159, 15, 15)
        items[circle] = "exit"
        helps.add(circle)
        exit = GLabel("x", 130, 171)
        exit.set_font("18px 'avenir'")
        items[exit] = "exit"
        helps.add(exit)
        gw.add(helps)
    format()

    #action for when the window is clicked
    def remove(event):
        y = event.get_y()
        x = event.get_x()
        element = helps.get_element_at(x, y)
        if element != None:
            diff = items.get(element)
            if diff == "exit":
                gw.clickable = True
                chooses.set_visible(True)
                gw.remove(helps)
                gw.done2 = True
                return
    gw.add_event_listener("click", remove)
