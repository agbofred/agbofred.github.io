from WordleGraphics import WordleGWindow, N_ROWS, N_COLS
from english import ENGLISH_WORDS, is_english_word
from WordleGraphics import CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
import random

def wordle():
    """ The main function to play the Wordle game. """
    def enter_action():
        """ What should happen when the RETURN or ENTER key is pressed. """
        # Check each position 0-4 and color each square accordingly then go to the next line;
        # if the correct word is guessed, end the game. If the guess is less than 5 letters,
        # don't allow the guesser to keep going
        gw.show_message("You need to implement this method")
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    def word_of_the_day():
        
        def five_letter_word():
            # Filter through ENGLISH_WORDS for only 5 letter words
            def chose_random():
                pass
            # select one at random


if __name__ == "__main__":
    wordle()