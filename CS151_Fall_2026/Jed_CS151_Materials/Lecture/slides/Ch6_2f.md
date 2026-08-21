---
title: "Stringing Together Methods"
author: Jed Rembold
date: "February 6, 2026"
slideNumber: true
theme: python_catppuccin
highlightjs-theme: catppuccin-mocha
width: 1920
height: 1080
transition: slide
hash: true
history: false
---
## Happy Friday!!!
::::::{.cols style='font-size:.8em'}

::::col
- Scan the QR code or go to [https://tools.jedrembold.prof/daily](https://tools.jedrembold.prof/daily)
- Introduce yourselves! Fun question: What is your favorite 6-letter word? Keep it in mind...

![](../images/group_seating_locs_Ford102.png){width=50%}
::::
::::col
![](https://barcode.orcascan.com/?text=GBxByg&data=https://tools.jedrembold.prof/daily?code=GBxByg){width=60%}
::::
::::::

<!-- Comments
-->


## Quick Announcements
- Problem Set 3 is due on Monday
- I'm aiming to get feedback to you on PS2 by end of tomorrow
- Project 1 starts next week!!


# Group Problems

## Problem 1: Fruit Ninja
- Take all the favorite 6-letter words from your group and concatenate them into a single string (you can choose the order)
- Your goal is to then create as many fruit strings as possible, using only concatenation, selection, and slicing.
- One point for each selection statement, 2 points for each slice of at least 2 characters!
- Example:
	- If my single string was: `s = "DANGERBOTTLECHANCEBRIGHT"`
	- I could get `"BANANA"` with `s[6] + s[1:3] + s[-10:-8] + s[1]` for 6 points
- How many points can your group get in the time allotted? What is your highest scoring fruit?




## Problem 2: Clean Up Time
- Consider the starting string
  ```python
  s = " --- ERROR_USER: jAnE.dOe@mAiL_sErVeR.CoM !!! "
  ```
- Your task is to systematically clean up and transform that string into something that just looks like
  ```python
  s = "jane.doe@mailserver.com"
  ```
  using introduced string methods, slicing, and variable assignment.

## The `english.py` Library
- To facilitate working with English words, we can take advantage of the pre-written `english` module
	- This will be highly useful in the Wordle project!
- The `english` module exports two resources:
	- `ENGLISH_WORDS`: a constant sequence which contains all the valid English words in alphabetical order and lowercase format
	- `is_english_word()`: a predicate function which takes a string as input and returns `True` or `False` depending on if that string is a valid English word


## Problem 3: Look Ma, No Vowels!
- Write a function which, when called, prints out all the words in the English language which do not contain vowels.
- Your function should _return_ the length of the longest word in the English language which doesn't contain a vowel
- Note that `ENGLISH_WORDS` is a sequence! So you can loop directly over it to get each word one at a time

# Live-Coding

## Igpay Atinlay
- Suppose we wanted to write a script that converted English to Pig Latin
- Rules of Pig Latin:
	- If the word begins with a consonant, move everything up to the first vowel to the end and append on "ay" at the end
	<center>
		`fleet` ⟶  `eetflay`
	</center>
	- If the word starts with a vowel, just append "way" to the end
	<center>
		`orange` ⟶  `orangeway`
	</center>
	- If the word has no vowels, do nothing
- Bonus: What English words, when "Pig-Latin-ified" are still valid English words?

## A Solution
```{.python style='max-height: 800px; font-size:.8em;'}
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
        if is_english_word(platin) and word != platin:
            print(word, platin))
```
