########################################
# Name:
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
        #word = display_word(row) This line was displaying the selected words to fulfill Miletone 1
        word = read_word(row)

        if not is_english_word(word):
            gw.show_message(f"{word.upper()} is not a valid English word")
        else:
            #gw.show_message(f"Yea! {word.upper()} is English word ")
            help_color(row)
            if check_win(row):
                gw.show_message(f"CONGRATULATIONS!!! YOU WON!!!")
                gw.set_current_row(N_ROWS)
            elif row == N_ROWS -1:
                gw.show_message(f"Oh No! You lose! The word is {hidden_word}")
                gw.set_current_row(N_ROWS)
            else:
                gw.set_current_row(row+1)


    def get_random_word(): # Function to choose random word
        word = random.choice(ENGLISH_WORDS)
        while len(word) !=5:
            word = random.choice(ENGLISH_WORDS)
        return word
    
    #Display the random word
    def display_word(row_id): # Function to display 5 letters in a row (Milestone 1)
        word = get_random_word()
        for i in range(len(word)):
            gw.set_square_letter(row_id,i,word[i])
        return word
    
    #Build the word from what users typed into the boxes (Milestone 2)
    def read_word(row_id): 
        word =""
        for i in range(N_COLS):
            word += gw.get_square_letter(row_id, i)
        return word.lower()

    # Milestone 3. Defining function to handle the colloring
    def help_color(row_id):
        word =read_word(row_id)
        available_letters = hidden_word

        #for green collors 
        for i in range(N_COLS):
            if word[i] == available_letters[i]:
                gw.set_square_color(row_id, i, CORRECT_COLOR)
                available_letters= available_letters.replace(word[i],"_",1)
                gw.set_key_color(word[i],CORRECT_COLOR)

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
    
    # Milestone 4 (Checking when the player wins or lose)

    def check_win(row):
        count = 0
        for i in range(N_COLS):
            if gw.get_square_color(row, i) == CORRECT_COLOR:
                count += 1
        return count == 5

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    hidden_word = get_random_word()




# Startup boilerplate
if __name__ == "__main__":
    wordle()
