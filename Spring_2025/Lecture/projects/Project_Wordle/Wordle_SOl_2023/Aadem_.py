from WordleGraphics import WordleGWindow, N_ROWS, N_COLS
from english import ENGLISH_WORDS, is_english_word
from WordleGraphics import CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
import random

""" The main function to play the Wordle game. """
def wordle(): 

    def fiveLetterDictionary():
        """FiveLetterWords = []
        for word in ENGLISH_WORDS:
            if len(word) == 5:
                FiveLetterWords.append(word)
        wordleWord = random.choice(FiveLetterWords)
        return wordleWord"""
        FiveLetterWords = random.choice(ENGLISH_WORDS)
        while len(FiveLetterWords)!=5:
            FiveLetterWords = random.choice(ENGLISH_WORDS)
        return FiveLetterWords

    def enter_action():
        row = gw.get_current_row()
        word = readWord(row)
        if not is_english_word(word):
            gw.show_message("Not in word List") 
        else:
            colorBoxes(row)
            if check_winner(row):
                gw.show_message("Yaahh! You win")
                gw.set_current_row(N_ROWS)
            elif row == N_ROWS - 1:
                gw.show_message("Oh No! You Lose")
                gw.set_current_row(N_ROWS)
            else:
                gw.set_current_row(row+1)

        #Milestone 3
    def colorBoxes(rowNumber):
        word = readWord(rowNumber)
        availableLetters = secretW
        # for Green color
        for i in range(N_COLS):
            if word[i] == availableLetters[i]:
                gw.set_square_color(rowNumber, i, CORRECT_COLOR)
                availableLetters = availableLetters.replace(word[i], "_", 1)
                gw.set_key_color(word[i], CORRECT_COLOR)
        # for yellow and grey
        for i in range(N_COLS):
            if gw.get_square_color(rowNumber, i) == UNKNOWN_COLOR:  
                if word[i] in availableLetters:
                    gw.set_square_color(rowNumber, i, PRESENT_COLOR)
                    availableLetters = availableLetters.replace(word[i], "_", 1)
                    if gw.get_key_color(word[i]) == UNKNOWN_COLOR:
                        gw.set_key_color(word[i], PRESENT_COLOR)
                else:
                    gw.set_square_color(rowNumber, i, MISSING_COLOR)
                    if gw.get_key_color(word[i]) == UNKNOWN_COLOR:
                        gw.set_key_color(word[i], MISSING_COLOR)

        """for i in range (N_COLS):
            if gw.get_square_color(rowNumber, i) == UNKNOWN_COLOR:
                if word[i] in availableLetters:
                    if word[i] == availableLetters[i]:
                        gw.set_square_color(rowNumber, i, CORRECT_COLOR)
                        availableLetters.replace(word[i])
                    else:
                        gw.set_square_color(rowNumber, i, PRESENT_COLOR)
                        availableLetters.replace(word[i])
        for i in range(N_COLS):
            if gw.get_square_color(rowNumber, i) == UNKNOWN_COLOR:
                if word[i] not in availableLetters:
                    gw.set_square_color(rowNumber, i, MISSING_COLOR)"""

    def readWord(rowNumber):
        string = ""
        for i in range (N_COLS):
            string += gw.get_square_letter(rowNumber, i)
        return string.lower()
    
    def check_winner(row):
        counter = 0
        for i in range(N_COLS):
            if gw.get_square_color(row, i)== CORRECT_COLOR:
                counter +=1
        return counter ==5

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    secretW= fiveLetterDictionary()


if __name__ == "__main__":
    wordle()