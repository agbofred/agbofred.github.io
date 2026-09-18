from english import ENGLISH_WORDS, is_english_word

def find_first_vowel(word):
    """ 
    Finds the first vowel index in a string

    Algorithm:
        Loop through all letters
        Check if that letter is in aeiou
        If it is, immediately return the index
    """
    for i in range(len(word)):
        if word[i].lower() in "aeiou":
            return i
    return -1

def pig_latin(word):
    """
    Converts a word to its Pig Latin form

    Algorithm:
        Check the first letter to see if vowel
            Task 1 if is not vowel
                Figure out where first vowel is
                Slice and rearrange
            Task 2
                Concatenate on a way
    """
    first_vowel = find_first_vowel(word)
    if first_vowel == 0:
        # Easy tack on way
        word += "way"
    elif first_vowel > 0:
        # Find first vowel and rearrange
        first_part = word[:first_vowel]
        second_part = word[first_vowel:]
        word = second_part + first_part + "ay"
    return word

if __name__ == '__main__':
    for word in ENGLISH_WORDS:
        platin = pig_latin(word)
        if (is_english_word(platin)) and (word != platin):
            print(word, platin)