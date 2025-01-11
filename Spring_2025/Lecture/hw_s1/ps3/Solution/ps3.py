# PROBLEM 1:
def draw_complex_pyramid(height, style ="solid", symbol ="*"):
    for row in range(height):
        star = 2*row + 1
        space = height - row - 1
        line = " " * space + symbol * star
        hollow = 2*row - 1
        if style =='solid':
            print(line)
        elif style =='hollow':
            if((hollow<0 ) or (hollow > (height*2-4))):
                print(line)
            else:
                linehole = " " * space + symbol + " " * hollow + symbol
                print(linehole)
        elif style == "alternate":
            if (row % 2 == 0):
                print(line)
            else:
                sym ="#"
                line2 = " " * space + sym * (star) ## Notice the new variable sym instead of symbole
                print(line2)


#if __name__ == '__main__':
    #draw_complex_pyramid(8)
    #draw_complex_pyramid(8, "hollow", "#")
    #draw_complex_pyramid(8,"alternate")


## PROBLEM 2

#A Part
def contains_repeated_letters(word):
    subword = ""
    count = 0
    word = str.lower(word)
    for row in range(len(word)):
        for col in range(row+1,len(word)):
            if  word[row] == word[col]:
                count +=1
                return True
    return False 
#if __name__ == '__main__':
   #print(contains_repeated_letters("MreomOE"))

#B Part
## Ensure you import english_words from english.py (file must be in the project directory)
from english import ENGLISH_WORDS
def longest_no_repeats():
    longest = ""
    for word in ENGLISH_WORDS:
        if not contains_repeated_letters(word):
            if len(word) > len(longest):
                longest = word
    return longest

if __name__ =="__main__":
    print(longest_no_repeats())