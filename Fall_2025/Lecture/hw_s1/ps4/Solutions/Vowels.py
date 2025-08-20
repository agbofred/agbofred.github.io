
from english import ENGLISH_WORDS

def has_single(char, word):
    count = 0
    for letter in word:
        if letter == char:
            count += 1
    return count == 1

def get_position(char, word):
    return word.find(char)

def special_word(word):
    vowels = "aeiouy"
    prev_position = -1
    for v in vowels:
        if has_single(v, word) and get_position(v, word) > prev_position:
            prev_position = get_position(v,word)
        else:
            return False
    return True

if __name__ == '__main__':
    print([x for x in ENGLISH_WORDS if special_word(x)])
