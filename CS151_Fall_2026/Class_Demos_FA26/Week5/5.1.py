from english import ENGLISH_WORDS, is_english_word

def find_first_vowel(word):
    """
    Returns the index of first vowel found
    """
    for i in range(len(word)):
        if word[i] in "aeiou":
            return i
    return -1

    """
    if aeiou.find(word[i])
    """

def pig_latin(word):
    """
    This function translate word to piglatin

    Algorithms:
       For every given word:
       1. Search through each character 
        1.1 if found vowel 
            apply rules
             
    """
    first_vowel = find_first_vowel(word)
    if first_vowel > 0:
        first_part = word[:first_vowel]
        second_part = word[first_vowel:]
        word = second_part + first_part +"ay"
    elif first_vowel == 0:
        word +=  "way"
        
    return word

if __name__ == "__main__":
    
    for word in ENGLISH_WORDS:
        if is_english_word(pig_latin(word)) and word != pig_latin(word):
           # print(word, pig_latin(word))
           pass
    
    print(len(ENGLISH_WORDS))