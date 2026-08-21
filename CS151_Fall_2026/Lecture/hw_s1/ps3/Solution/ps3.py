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



"""PROBLEM 3"""

def to_obenglobish(word):
    """ Converts an English word into its Obenglobish equivalent.

    Inputs:
        word (string): word to be translated to Obenglobish
    Outputs:
        (string): the Obenglobish translation of the word
    """
    #pass # Add your code below and remove this pass!
    start_w = word[:1]
    end_w = word[-1]
    string =""
    # If both start and end are vowel letters 
    if(check_vowel(start_w) and check_vowel(end_w)):
        sub_str= word[:len(word)-1]
        ch =start_w
        string = ""
        for i in range(len(sub_str)):
            if ch == sub_str[i] and i==0:
                string = string + "ob" + ch
            elif ch == sub_str[i]:
                if(check_vowel(sub_str[i])):
                    string = string + ch
                else:
                    string = string + ch
            else:
                if(check_vowel(sub_str[i])):
                    ch = sub_str[i]
                    string = string + "ob" + sub_str[i]
                else:
                    ch = sub_str[i]
                    string = string + sub_str[i]
        string = string+end_w

    # If only the start word is vowel 
    elif(check_vowel(start_w)):
        ch =start_w
        string = ""
        for i in range(len(word)):
            if ch == word[i] and i==0:
                string = string + "ob" + ch
            elif ch == word[i]:
                if(check_vowel(word[i])):
                    string = string + ch
                else:
                    string = string + ch
            else:
                if(check_vowel(word[i])):
                    ch = word[i]
                    string = string + "ob" + word[i]
                else:
                    ch = word[i]
                    string = string + word[i]
    # When only the end character is vowel                
    elif(check_vowel(end_w)):
        sub_str= word[:len(word)-1]
        ch =""
        string = ""
        for i in range(len(sub_str)):
            if ch == sub_str[i]:
                if(check_vowel(sub_str[i])):
                    string = string + sub_str[i]
                else:
                    ch = sub_str[i]
                    string = string + sub_str[i]
            else:
                if(check_vowel(sub_str[i])):
                    string = string + "ob" +sub_str[i]
                else:
                    ch = sub_str[i]
                    string = string + sub_str[i]
        string = string + end_w
    #When neighter the first or last character is vowel
    else:
        ch =start_w
        string = ""
        for i in range(len(word)):
            if ch == word[i] and word[i]==0:
                string = string + word[i]
                #ch = word[i]
            elif ch == word[i]:
                if(check_vowel(word[i])):
                    string = string + word[i] 
                    ch = word[i]
                else:
                    string = string + word[i] 
                    ch = word[i]
            elif(check_vowel(word[i])): 
                if (check_vowel(ch)):
                    string = string  + word[i]
                    ch = word[i]
                else:
                    string = string + "ob" + word[i]
                    ch = word[i]
            else:
                string = string + word[i]
        
    return string


def check_vowel(w):
    if "AEIOUaeoiu".find(w)!=-1:
        return True

   
#################################
#Boiler Plat to run the codes 

if __name__ =="__main__":
    #print(longest_no_repeats())
    print(f"to_obenglobish('english') gives {to_obenglobish('english')}.")
    print(f"to_obenglobish('gooiest') gives {to_obenglobish('gooiest')}.")
    print(f"to_obenglobish('amaze')   gives {to_obenglobish('amaze')}.")
    print(f"to_obenglobish('rot')     gives {to_obenglobish('rot')}.")