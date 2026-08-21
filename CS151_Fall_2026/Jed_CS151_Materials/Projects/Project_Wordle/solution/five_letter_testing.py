
from english import ENGLISH_WORDS
import random


def five_first():
    five_letter_words = [word for word in ENGLISH_WORDS if len(word) == 5]
    return random.choice(five_letter_words)

def five_second():
    word = random.choice(ENGLISH_WORDS)
    while len(word) != 5:
        word = random.choice(ENGLISH_WORDS)
    return word



