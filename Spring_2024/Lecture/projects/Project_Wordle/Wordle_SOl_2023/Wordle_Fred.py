########################################
# Name: Fred - with the help of Jed's version
# Collaborators (if any):
# Estimated time spent (hr):
# Description of any added extensions:
########################################

from WordleGraphics import WordleGWindow, N_ROWS, N_COLS
from english import ENGLISH_WORDS, is_english_word
from WordleGraphics import CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
import random


def wordle():
    """ The main function to play the Wordle game. """

    def enter_action():
        """ What should happen when the RETURN or ENTER key is pressed. """
        row = gw.get_current_row()
       # word = get_random_word() # This line implements MS 1
       # display_word(word,row)  # This line displays the random number MS 1
        word = read_word(row)
        if not is_english_word(word):
            gw.show_message("The word is not valid")
        else:
            color_box(row)
            if check_win(row):
                gw.show_message("Congratulations! You Win")
                gw.set_current_row(N_ROWS)
            elif row == N_ROWS -1:
                gw.show_message(f"Oh No! You lose! The word is {hidden_word}")
                gw.set_current_row(N_ROWS)
            else:
                gw.set_current_row(row +1)


            #gw.show_message("You need to implement this method -"+ word)
        
    
    def get_random_word():
        word = random.choice(ENGLISH_WORDS)
        while len(word) !=5:
            word = random.choice(ENGLISH_WORDS)
        return word


    def display_word(word, row_id): # Milestone 1
        """ Display 5 letters to a row"""
        for i in range(len(word)):
            gw.set_square_letter(row_id,i, word[i])

    def read_word(row_id): # Milestone2
        """Reading in word from the display string"""
        word =""
        for i in range(N_COLS):
            word += gw.get_square_letter(row_id,i)
        return word.lower()

    def color_box(row_id): # MS3
        """ Color the baoxes on a particular row"""
        word = read_word(row_id)
        available_letters = hidden_word
        # For Green
        for i in range(N_COLS):
            if word[i] == available_letters[i]:
                gw.set_square_color(row_id, i, CORRECT_COLOR)
                available_letters= available_letters.replace(word[i], "_", 1)
                gw.set_key_color(word[i], CORRECT_COLOR)
        # for Yellow and grey
        for i in range(N_COLS):
            if gw.get_square_color(row_id, i) == UNKNOWN_COLOR : # Meaning, has not been assigned
                if word[i] in available_letters:
                    gw.set_square_color(row_id, i, PRESENT_COLOR)
                    available_letters = available_letters.replace(word[i], "_" ,1)
                    if gw.get_key_color(word[i]) == UNKNOWN_COLOR:
                        gw.set_key_color(word[i], PRESENT_COLOR)
                else:
                    gw.set_square_color(row_id, i, MISSING_COLOR)
                    if gw.get_key_color(word[i])== UNKNOWN_COLOR:
                        gw.set_key_color(word[i], MISSING_COLOR)

    def check_win(row):
        """Checking to see everhting is green"""
        count = 0
        for i in range(N_COLS):
            if gw.get_square_color(row,i)== CORRECT_COLOR:
                count +=1
        return count ==5


    gw = WordleGWindow()
    
    gw.add_enter_listener(enter_action)
    hidden_word= get_random_word()
    print(hidden_word)


# Startup boilerplate
if __name__ == "__main__":
    wordle()
