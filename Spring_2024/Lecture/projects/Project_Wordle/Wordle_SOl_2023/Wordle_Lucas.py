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

def get_random_word() -> str:
    '''
        This return a random word from the dictionary
    '''
    random_word = random.choice(ENGLISH_WORDS)
    return random_word

def is_valid_word(word: str) ->bool:
    return word in ENGLISH_WORDS

def get_users_input_from_window(gw: WordleGWindow, row: int) -> str:
    '''
        Grab the letters from the window and return them 
    '''
    users_word = ''
    for col in range(5):
        users_word = users_word + gw.get_square_letter(row, col)

    return users_word

def wordle():
    """ The main function to play the Wordle game. """

    def enter_action():
        """ What should happen when the RETURN or ENTER key is pressed. """

        users_word = get_users_input_from_window(gw, gw.get_current_row())
        users_word = users_word.lower()

        

        gw.show_message(f'You typed in: {users_word} and it is: {is_valid_word(users_word)}')

        gw.set_current_row(gw.get_current_row() + 1)


    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)




# Startup boilerplate
if __name__ == "__main__":
    wordle()
