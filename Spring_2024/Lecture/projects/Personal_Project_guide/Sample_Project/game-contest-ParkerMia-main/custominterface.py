# Name: Mia Parker
from pgl import GLabel, GRect, GCompound
from playinterface import play

KEY_LABELS = [
    [ "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P" ],
    [ "A", "S", "D", "F", "G", "H", "J", "K", "L" ],
    [ "Enter ", "Z", "X", "C", "V", "B", "N", "M", " Delete" ]]

#creates the custom interface which allows the player to choose their own word
def custom(gw, W_WIDTH):
    keys_dict = {} #key is GLabel, value is letter
    gw.start = 0
    gw.count = 0
    gw.word_compound = GCompound()
    key_com = GCompound()
    gw.add(gw.word_compound)
    gw.word1 = ""
    ycor = 500
    gw.display = False
    Display = GLabel("You have not chosen any letters yet.", 65, 400)
    Display.set_font("30px 'helvetica'")
    gw.display2 = False
    Display2 = GLabel("Your word cannot be any longer.", 85, 400)
    Display2.set_font("30px 'helvetica'")
    gw.click = True

    #creates the interactive keyboard and adds the keys to a dictionary
    def keys():
        y=600
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
                keys_dict[key] = letter
                key_com.add(key)
                
                x+=(key.get_width()+10)
            y+=40
    gw.add(key_com)

    #action for when the window is clicked
    def printer(event):
            if gw.click == True:
                y = event.get_y()
                x = event.get_x()
                if gw.display == True:
                    gw.remove(Display)
                    gw.display = False
                if gw.display2 == True:
                    gw.remove(Display2)
                    gw.display2 = False
                element = key_com.get_element_at(x, y)
                if element != None:
                    letter = keys_dict.get(element)
                    if letter == " Delete":
                        if gw.word1 == "":
                            gw.add(Display)
                            gw.display = True
                        else:
                            length = len(gw.word1)
                            gw.word1=gw.word1[:length-1]
                            width = 30
                            gw.remove(gw.word_compound)
                            gw.word_compound = GCompound()
                            for i in range(len(gw.word1)):
                                let = GLabel(gw.word1[i])
                                let.set_font("40px 'helvetica'")
                                width+=(let.get_width()+20)
                            xcor = (W_WIDTH/2)-(width/2)    
                            for i in range(len(gw.word1)):
                                let = GLabel(gw.word1[i], xcor, ycor)
                                let.set_font("40px 'helvetica'")
                                gw.word_compound.add(let)
                                underx =(xcor + (let.get_width()/2))-20 
                                underscore = GRect(underx, ycor+10, 40, 5)
                                underscore.set_filled(True)
                                gw.word_compound.add(underscore)
                                xcor+=(let.get_width()+30)
                            gw.add(gw.word_compound)
                    elif len(gw.word1)>9 and letter != "Enter " and letter != " Delete":
                        gw.add(Display2)
                        gw.display2 = True
                    elif letter != "Enter ":
                        width = 30
                        gw.remove(gw.word_compound)
                        gw.word_compound = GCompound()
                        gw.word1 +=letter
                        for i in range(len(gw.word1)):
                            let = GLabel(gw.word1[i])
                            let.set_font("40px 'helvetica'")
                            width+=(let.get_width()+20)
                        xcor = (W_WIDTH/2)-(width/2)    
                        for i in range(len(gw.word1)):
                            let = GLabel(gw.word1[i], xcor, ycor)
                            let.set_font("40px 'helvetica'")
                            gw.word_compound.add(let)
                            underx =(xcor + (let.get_width()/2))-20 
                            underscore = GRect(underx, ycor+10, 40, 5)
                            underscore.set_filled(True)
                            gw.word_compound.add(underscore)
                            xcor+=(let.get_width()+30)
                        gw.add(gw.word_compound)
                    elif letter == "Enter ":
                        if gw.word1 == "":
                            gw.add(Display)
                            gw.display = True
                        else:
                            gw.remove(key_com)
                            gw.remove(gw.word_compound)
                            gw.click = False
                            play(gw, W_WIDTH, gw.word1)
                            return
                
    keys()
    gw.add_event_listener("click", printer)

