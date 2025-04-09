# File: PigLatin.py

"""
This file converts from English to Pig Latin using the following rules:
1. If the word begins with a vowel, add "way" to the end of the word.
2. If the word begins with a consonant, extract the leading consonants 
   up to the first vowel, move them to the end, and then add "ay".
3. If the word contains no vowels, return the word unchanged.
"""

def to_pig_latin(line):
    """Converts a multi-word string from English to Pig Latin."""
    result = ""
    start = -1
    for i in range(len(line)):
        ch = line[i]
        if ch.isalpha():
            if start == -1:
                start = i
        else:
            if start >= 0:
                result += word_to_pig_latin(line[start:i])
                start = -1
            result += ch
    if start >= 0:
        result += word_to_pig_latin(line[start:])
    return result

def word_to_pig_latin(word):
    """Translates a word to Pig Latin."""
    vp = find_first_vowel(word)
    if vp == -1:
        return word
    elif vp == 0:
        return word + "way"
    else:
        head = word[0:vp]
        tail = word[vp:]
        return tail + head + "ay"

def find_first_vowel(word):
    """Returns the index of the first vowel in the word, or -1 if none."""
    for i in range(len(word)):
        if is_english_vowel(word[i]):
            return i
    return -1
def is_english_vowel(ch):
    """Returns True if ch is an English vowel (A, E, I, O, or U)."""
    return len(ch) == 1 and "AEIOUaeiou".find(ch) != -1

# Main program

def pig_latin():
    finished = False
    while not finished:
        line = input("Enter a string: ")
        if line == "":
            finished = True
        else:
            print("Pig Latin form: " + to_pig_latin(line))

# Startup code

if __name__ == "__main__":
    pig_latin()

