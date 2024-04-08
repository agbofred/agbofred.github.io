# Name: Mia Parker
import random
from english import ENGLISH_WORDS, EASY, MEDIUM, HARD
from pgl import GLabel, GRect, GOval, GCompound
from help2interface import help2


KEY_LABELS = [
    [ "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P" ],
    [ "A", "S", "D", "F", "G", "H", "J", "K", "L" ],
    [ "Z", "X", "C", "V", "B", "N", "M" ]]

#This is the play screen that has the game itself
def play(gw, W_WIDTH, diff):
    gw.keys_dict = {} #key is GLabel, value is letter
    gw.keyword = {} #key is letter, value is GLabel
    gw.compounds = [] #contains all compounds
    compound1 = GCompound() #contains keys
    compound2 = GCompound() #contains structure
    compound3 = GCompound() #contains keyword
    gw.compound4 = GCompound() #contains win, lose and reveal word
    difficulties = {"EASY": EASY, "MEDIUM": MEDIUM, "HARD": HARD}
    body = []
    gw.not_revealed = []
    gw.start = 0
    gw.letters = 0
    gw.count = 0
    gw.done = False
    
    #creates the display for the word, chooses a random word, and creates a dictionary and list
    def create_word():
        if diff not in difficulties:
            gw.word = diff
        else:
            d = difficulties.get(diff)
            lowerword = random.choice(d)
            gw.word = lowerword.upper()   
        y=580
        x=50
        width = 30
        for letter in gw.word:
            let = GLabel(letter)
            let.set_font("40px 'helvetica'")
            width+=(let.get_width()+20)
        x = (W_WIDTH/2)-(width/2)    
        for letter in gw.word:
            let = GLabel(letter, x, y)
            let.set_font("40px 'helvetica'")
            let.set_visible(False)
            compound3.add(let)
            underx =(x+(let.get_width()/2))-20 
            underscore = GRect(underx, y+10, 40, 5)
            underscore.set_filled(True)
            compound3.add(underscore)
            x+=(let.get_width()+30)
            gw.keyword[f"{letter} {gw.letters}"] = let
            gw.not_revealed.append(f"{letter} {gw.letters}")
            gw.letters+=1

    #creates the structure and the stick figure, and adds the stickfigure pieces to dictionary
    def structure():
        floor = GRect(100, 500, 400, 30)
        floor.set_filled(True)
        compound2.add(floor)
        post = GRect(120, 50, 30, 450)
        post.set_filled(True)
        compound2.add(post)
        post = GRect(120, 50, 275, 30)
        post.set_filled(True)
        compound2.add(post)
        noose = GRect(380, 80, 5, 40)
        noose.set_filled(True)
        compound2.add(noose)
        head = GOval(345, 120, 75, 75)
        head.set_filled(True)
        head.set_visible(False)
        compound2.add(head)
        body.append(head)
        base = GRect(377.5, 195, 10, 120)
        base.set_filled(True)
        base.set_visible(False)
        compound2.add(base)
        body.append(base)
        arm1 = GRect(377.5, 210, 10, 70)
        arm1.rotate(40)
        arm1.set_filled(True)
        arm1.set_visible(False)
        compound2.add(arm1)
        body.append(arm1)
        arm2 = GRect(377.5, 208, 10, 65)
        arm2.rotate(-40)
        arm2.set_filled(True)
        arm2.set_visible(False)
        compound2.add(arm2)
        body.append(arm2)
        leg1 = GRect(377.5, 315, 10, 80)
        leg1.rotate(35)
        leg1.set_filled(True)
        leg1.set_visible(False)
        compound2.add(leg1)
        body.append(leg1)
        leg2 = GRect(377.5, 313, 10, 75)
        leg2.rotate(-35)
        leg2.set_filled(True)
        leg2.set_visible(False)
        compound2.add(leg2)
        body.append(leg2)
    
    #creates the interactive keyboard, help button and adds the keys to a dictionary
    def keys():
        y=650
        for row in KEY_LABELS:
            width=-10
            for letter in row:
                key = GLabel(letter)
                key.set_font("30px 'helvetica'")
                width+=(key.get_width()+10)
            x = (W_WIDTH/2)-(width/2)    
            for letter in row:
                key = GLabel(letter, x, y)
                key.set_font("30px 'helvetica'")
                gw.keys_dict[key] = letter
                compound1.add(key)
                x+=(key.get_width()+10)
            y+=40
            circle = GOval(576, 4, 20, 20)
            compound1.add(circle)
            gw.keys_dict[circle] = "help"
            help = GLabel("?", 582, 21)
            help.set_font("20px 'avenir'")
            compound1.add(help)
            gw.keys_dict[help] = "help"
    
    create_word()
    structure()
    keys()
    gw.compounds.append(compound1)
    gw.compounds.append(compound2)
    gw.compounds.append(compound3)
    gw.current_compound = compound1
    for i in gw.compounds:
        gw.add(i)
    
    #action for when the window is clicked
    def printer(event):
        y = event.get_y()
        x = event.get_x()
        inword=False
        element = gw.current_compound.get_element_at(x, y)
        if element != None and gw.done != True:
            letter = gw.keys_dict.get(element)
            if letter == "help":
                for i in gw.compounds:
                    gw.remove(i)
                help2(gw, gw.compounds)
            else:
                element.set_color("grey")
                for i in range(len(gw.keyword)): #0, 1, 2
                    letter2 = f"{letter} {i}"
                    if letter2 in gw.keyword:
                        value = gw.keyword.get(letter2)
                        value.set_visible(True)
                        inword = True
                        if letter2 in gw.not_revealed:
                            gw.not_revealed.remove(letter2)
                            gw.count+=1
                if inword == False:
                        part = body[gw.start]
                        part.set_visible(True)
                        gw.start+=1 
        if gw.start ==6 and gw.done == False:
            lose = GLabel("You Lose!", 230, 420)
            lose.set_font("40px 'copperplate'")
            gw.compound4.add(lose)
            word = f"Your word was {gw.word}"
            reveal = GLabel(word, 190, 450)
            reveal.set_font("30px 'copperplate'")
            gw.compound4.add(reveal)
            gw.add(gw.compound4)
            gw.current_compound = gw.compound4
            gw.done = True
        if gw.count == len(gw.keyword) and gw.done == False:
            win = GLabel("You Win!", 230, 420)
            win.set_font("40px 'copperplate'")
            gw.compound4.add(win)
            gw.add(gw.compound4)
            gw.current_compound = gw.compound4
            gw.done = True
    
    gw.add_event_listener("click", printer)