
def find_first_vowel(word):
    """Finds the position of the first vowel in a word."""
    for i in range(len(word)):
        if word[i].lower() in "aeiou":
            return i
    return -1

def find_largest_contiguous_letters(word):
    """Finds and returns the largest contiguous block of purely alphabetical characters 
    that appears in a string.
    """
    for size in range(len(word), 0, -1):
        for pos in range(len(word) - size + 1):
            candidate = word[pos:pos+size]
            if candidate.isalpha():
                return candidate
    return None

def word2piglatin(word):
    """Returns the Pig Latin version of the provided word."""

    lword = find_largest_contiguous_letters(word)
    if lword is None:
        return word
    starts_w_caps = lword[0].isupper()

    first_vowel_pos = find_first_vowel(lword)
    if first_vowel_pos == 0:
        new =  lword + "way"
    elif first_vowel_pos > 0:
        new =  lword[first_vowel_pos:] + lword[:first_vowel_pos] + "ay"
    else:
        new =  lword
    
    candidate = word.replace(lword, new).lower()
    if starts_w_caps:
        return candidate.capitalize()
    return candidate







if __name__ == '__main__':
    print(word2piglatin(':messy!awfulness..'))
