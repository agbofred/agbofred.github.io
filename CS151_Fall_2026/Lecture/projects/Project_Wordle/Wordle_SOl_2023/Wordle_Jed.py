########################################
# Name: Jed
# Collaborators (if any):
# Estimated time spent (hr):
# Description of any added extensions:
########################################

from WordleGraphics import WordleGWindow, N_ROWS, N_COLS
from english import ENGLISH_WORDS, is_english_word
from WordleGraphics import CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
import random


def wordle():
    """The main function to play the Wordle game."""

    def enter_action():
        """What should happen when the RETURN or ENTER key is pressed."""
        row = gw.get_current_row()
        word = read_word(row)
        if not is_english_word(word):
            gw.show_message("Not in word list")
        else:
            # gw.show_message("You know English!") #MS2
            color_boxes(row)

            if check_win(row):
                gw.show_message("You win!! Amazing!")
                gw.set_current_row(N_ROWS)
            elif row == N_ROWS - 1:
                gw.show_message(f"You lose! The word was {hidden_word}!")
                gw.set_current_row(N_ROWS)
            else:
                gw.set_current_row(row + 1)

    def pick_random_five_letter_word():  # MS1
        """
        Picks a word from the dictionary at random and then ensures that it
        has exactly 5 letters.
        """
        word = random.choice(ENGLISH_WORDS)
        while len(word) != 5:
            word = random.choice(ENGLISH_WORDS)
        return word

    def display_word(word, row_id):  # MS1
        """Displays a five letter word to a particular row"""
        for i in range(len(word)):
            gw.set_square_letter(row_id, i, word[i])

    def read_word(row_id):  # MS2
        """Reads in a word from the display to a string"""
        word = ""
        for i in range(N_COLS):
            word += gw.get_square_letter(row_id, i)
        return word.lower()

    def color_boxes(row_id):  # MS3
        """Colors in the boxes on a particular row"""
        word = read_word(row_id)
        available_letters = hidden_word  # Initializing
        # Green First
        for i in range(N_COLS):
            if word[i] == available_letters[i]:
                gw.set_square_color(row_id, i, CORRECT_COLOR)
                available_letters = available_letters.replace(word[i], "_", 1)
                gw.set_key_color(word[i], CORRECT_COLOR)
        # Then Yellow and gray
        for i in range(N_COLS):
            if gw.get_square_color(row_id, i) == UNKNOWN_COLOR:  # hasn't been assigned
                if word[i] in available_letters:
                    gw.set_square_color(row_id, i, PRESENT_COLOR)
                    available_letters = available_letters.replace(word[i], "_", 1)
                    if gw.get_key_color(word[i]) == UNKNOWN_COLOR:
                        gw.set_key_color(word[i], PRESENT_COLOR)
                else:
                    gw.set_square_color(row_id, i, MISSING_COLOR)
                    if gw.get_key_color(word[i]) == UNKNOWN_COLOR:
                        gw.set_key_color(word[i], MISSING_COLOR)

    def check_win(row):
        """Checks to see if everything is green in the row"""
        count = 0
        for i in range(N_COLS):
            if gw.get_square_color(row, i) == CORRECT_COLOR:
                count += 1
        return count == 5

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    hidden_word = pick_random_five_letter_word()
    print(hidden_word) # cheat mode activated
    # display_word(hidden_word, 0) #only needed for MS1


# Startup boilerplate
if __name__ == "__main__":
    wordle()
