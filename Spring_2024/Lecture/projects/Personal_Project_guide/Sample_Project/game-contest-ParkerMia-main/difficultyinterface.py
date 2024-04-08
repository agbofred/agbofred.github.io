# Name: Mia Parker
from pgl import GLabel, GRect, GOval, GCompound
from help1interface import help_screen
from custominterface import custom
from playinterface import play

#the starting screen where the player chooses the difficulty level or custom
def start_screen(gw, W_WIDTH, W_HEIGHT):
    gw.clickable = True
    difficulty = {}
    chooses = GCompound()
    ready = False
    difficulties = ["EASY", "MEDIUM", "HARD"]
    #creates title, difficulty level buttons, custom button and help button
    def starting():
        background = GRect(0, 0, 600, 750)
        background.set_color("white")
        background.set_filled(True)
        chooses.add(background)
        box = GRect(125, 156, 350, 437)
        chooses.add(box)
        name = GLabel("Hangman", 185, 215)
        name.set_font("50px 'copperplate'")
        chooses.add(name)
        diff = GLabel("Choose your", 195, 305)
        diff.set_font("30px 'copperplate'")
        chooses.add(diff)
        diff = GLabel("difficulty", 213, 325)
        diff.set_font("30px 'copperplate'")
        chooses.add(diff)
        square1 = GRect(158, 375, 125, 40)
        chooses.add(square1)
        difficulty[square1] = "EASY"
        square2 = GRect(317, 375, 125, 40)
        chooses.add(square2)
        difficulty[square2] = "MEDIUM"
        square3 = GRect(158, 475, 125, 40)
        chooses.add(square3)
        difficulty[square3] = "HARD"
        square4 = GRect(317, 477, 125, 40)
        chooses.add(square4)
        difficulty[square4] = "custom"
        easy = GLabel("Easy", 190, 405)
        easy.set_font("30px 'avenir'")
        chooses.add(easy)
        difficulty[easy] = "EASY"
        medium = GLabel("Medium", 325, 405)
        medium.set_font("30px 'avenir'")
        chooses.add(medium)
        difficulty[medium] = "MEDIUM"
        hard = GLabel("Hard", 187, 505)
        hard.set_font("30px 'avenir'")
        chooses.add(hard)
        difficulty[hard] = "HARD"
        customlabel = GLabel("Custom", 328, 505)
        customlabel.set_font("30px 'avenir'")
        chooses.add(customlabel)
        difficulty[customlabel] = "custom"
        circle = GOval(456, 160, 15, 15)
        chooses.add(circle)
        difficulty[circle] = "help"
        help = GLabel("?", 460, 173)
        help.set_font("15px 'avenir'")
        chooses.add(help)
        difficulty[help] = "help"
        gw.add(chooses)
    starting()

    #action for when the window is clicked
    def prints(event):
        if gw.clickable == True:
            y = event.get_y()
            x = event.get_x()
            element = chooses.get_element_at(x, y)
            if element != None:
                diff = difficulty.get(element)
                if diff == "help":
                    gw.clickable = False
                    #gw.remove(chooses)
                    chooses.set_visible(False)
                    gw.done2 = False
                    help_screen(gw, chooses)
                elif diff == "custom":
                    gw.remove(chooses)
                    gw.clickable = False
                    custom(gw, W_WIDTH)
                elif diff in difficulties:
                    gw.remove(chooses)
                    gw.clickable = False
                    play(gw, W_WIDTH, diff)
    
    gw.add_event_listener("click", prints)