# Name: Mia Parker
from pgl import GRect, GLabel, GOval, GCompound

#creates the help screen for the play interface
def help2(gw, compounds):
    dict = {}

    #adds the display of rules, the exit button and the hint buttom
    def display():
        gw.rules = GCompound()
        gw.done1 = False
        box = GRect(125, 156, 350, 437)
        gw.rules.add(box)
        label = GLabel("Rules", 225, 215)
        label.set_font("50px 'copperplate'")
        gw.rules.add(label)
        line1 = GLabel("The objective of hangman is to guess the secret", 135, 270)
        line1.set_font("15px 'avenir'")
        gw.rules.add(line1)
        line2 = GLabel("word before the stick figure is hung. Gameplay", 135, 290)
        line2.set_font("15px 'avenir'")
        gw.rules.add(line2)
        line3 = GLabel("continues until the player guesses the word or they", 135, 310)
        line3.set_font("15px 'avenir'")
        gw.rules.add(line3)
        line4 = GLabel("run out of guesses and the stick figure is hung. In", 135, 330)
        line4.set_font("15px 'avenir'")
        gw.rules.add(line4)
        line5 = GLabel("this game the player has 6 guesses before the", 135, 350)
        line5.set_font("15px 'avenir'")
        gw.rules.add(line5)
        line6 = GLabel("figure is fully revealed.", 135, 370)
        line6.set_font("15px 'avenir'")
        gw.rules.add(line6)
        line7 = GLabel("Hints are available and can be used to reveal one", 135, 400)
        line7.set_font("15px 'avenir'")
        gw.rules.add(line7)
        line8 = GLabel("letter from the word.", 135, 420)
        line8.set_font("15px 'avenir'")
        gw.rules.add(line8)
        hint = GLabel("Hint", 445, 171)
        hint.set_font("13px 'avenir'")
        dict[hint] = "hint"
        gw.rules.add(hint)
        box2 = GRect(442, 159, 30, 15)
        dict[box2] = "hint"
        gw.rules.add(box2)
        circle = GOval(127, 159, 15, 15)
        dict[circle] = "exit"
        gw.rules.add(circle)
        exit = GLabel("x", 130, 171)
        exit.set_font("18px 'avenir'")
        dict[exit] = "exit"
        gw.rules.add(exit)
        gw.add(gw.rules)
    display()

    #action for when the window is clicked
    def remove(event):
        y = event.get_y()
        x = event.get_x()
        element = gw.rules.get_element_at(x, y)
        if element != None:
            diff = dict.get(element)
            if diff == "exit" and gw.done1 == False:
                for i in compounds:
                    gw.add(i)
                gw.done1 = True
                gw.remove(gw.rules)
                return
            if diff == "hint" and gw.done1 == False:
                reveal = gw.not_revealed[0]
                value = gw.keyword.get(reveal)
                value.set_visible(True)
                gw.count+=1
                gw.not_revealed= gw.not_revealed[1:]
                for i in compounds:
                    gw.add(i)
                gw.done1 = True
                gw.remove(gw.rules)
                return
    
    gw.add_event_listener("click", remove)

