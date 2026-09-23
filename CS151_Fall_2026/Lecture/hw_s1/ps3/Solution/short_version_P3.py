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
    
    for i in range(len(word)):
        if word[i] == start_w:
            if check_vowel(word[i]):
                string = string + 'ob' + word[i]
            else:
                string = string + word[i]
        elif word[i] == end_w:
            if check_vowel(word[i]):
                string = string + word[i]
            else:
                string = string + word[i]
        else:
            if check_vowel(word[i]):
                if check_vowel(word[i-1]):
                    string = string + word[i]
                else:
                    string = string + 'ob' + word[i]
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