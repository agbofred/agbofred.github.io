---
title: "Formatting String"
author: Fred Agbo
date: "September 21, 2026"
slideNumber: true
theme: "python_monokai"
highlightjs-theme: monokai
width: 1920
height: 1080
transition: fade
hash: true
history: false

---

## Happy Week 5!
::::{style='font-size:.8em'}
- Class grouping today: Scan the QR code or go to [https://tools.jedrembold.prof/daily](https://tools.jedrembold.prof/daily)
- Class code is `TD9RC0`
- Introduce yourselves! What is your favorite word?
::::

::::::cols

::::col
![](../images/group_arrangement.png){width=60%}
::::
::::col
![](https://barcode.orcascan.com/?data=https://tools.jedrembold.prof/daily?code=lcjjHj){width=60%}
::::
::::::


## Quick Announcements
- __Problem set 3 is due today at 10 pm__
	- I encourage you to visit QUAD if you need more help
- Our first Project - `Wordle` is published today! 
	- Wordle is due next week Monday

---

## Review!{data-notes="Solution: x[-6:-1]"}
Suppose you have the string `x = "consternation"` and you'd like to just extract and print the word `"nation"`. Which expression below will **not** give you the string `"nation"`?


:::{.poll}
#. `x[7:len(x)]`
#. `x[7:]`
#. `x[-6:len(x)]`
#. `x[-6:-1]`
:::

---

## Learn Pig Latin: Igpay Atinlay
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

---

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
            print(word, platin)
```

---

## Learning English
- When working with sequences of characters, it is often useful or desirable to determine if they form actual valid English words
- This class provides for you a new library, through the file `english.py`
- The `english` library provides two objects you can import into your programs:
	- The constant `ENGLISH_WORDS`, which is a list of all the valid words in the English dictionary
	- The function `is_english_word()`, which accepts a single string as an argument and returns `True` if the string represents a valid English word.
- This library will be particularly useful for Wordle!

---

## Example: How many 2 letter words?
- Before we start writing code, let's pause. Give a physical English dictionary, how could you go about figuring out the number of two letter words?

::::::cols
::::{.col .fragment}
:::{.block name="Check valid words for right length"}
```{.python style='width: 100%' .fragment}
from english import ENGLISH_WORDS

count = 0
for word in ENGLISH_WORDS:
	if len(word) == 2:
		count += 1
print(count)
```
:::
::::

::::{.col style='flex-grow:1.15' .fragment}
:::{.block name="Check all two letter combinations"}
```{.python style='width:100%' .fragment}
from english import is_english_word

count = 0
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for letter1 in alphabet:
	for letter2 in alphabet:
		word = letter1 + letter2
		if is_english_word(word):
			count += 1
print(count)
```
:::
::::
::::::

----

# Formatting Strings 

---


## Understanding Check! {data-notes="The 32//8 option"}
Which of the provided formatted string options below would evaluate to appear as:

<center>
`101,234.98   & 4000`
</center>

when printed?

:::{.poll}
#. `f"{101234.984:<12,.2f} & {3200//8:<4d}"`
#. `f"{101234.984:>12,.2f} & {32000//8:0>3d}"`
#. `f"{101234.984:<12,f} & {320//8:0>4d}"`
#. `f"{101234.984:<12,.2f} & {32//8:0<4d}"`
:::

---

## Live Code: Tabulated Birthdays
- You want a program that prompts a user for 3 pieces of information:
	- Name
	- Birth month name
	- Birth year
- It should do this for each member of your group 
- It should then print off a table with:
	- Columns of Name, Birth month, and Age (approximate)
	- Each members information below, nicely aligned

---

## Problem 3 Example Output
```text
Enter your name: Joe
Enter your birth month: April
Enter your birth year: 1985

Enter your name: Rick
Enter your birth month: June
Enter your birth year: 1952

Name   Birth Month  Age
Joe    April        41
Rick   June         74

```

---

# Project 1: Wordle

---

## Introduction to Wordle
::::::cols
::::col
- Our first project is recreating Wordle
- Guide is posted now and available!
- Due next Monday (Feb 16)
- Section questions will relate to common Wordle issues this week
- Aiming to be done with Milestone 3 by end-of-day Friday would be a good target
::::

::::col
![The game of Wordle](../images/wordle.png)
::::
::::::

---

## Your Responsibilities
- We provide you with a custom data type that handles all the graphics and user interaction
	- Don't worry, you'll have a chance to implement your own GUIs later in the semester!
- Your responsibilities will include:
	- Displaying and reading letters from boxes
	- Evaluating whether a word is valid
	- Determining what color each letter of a word should be
    - Selecting a secret five letter word for guessing
	- Determining when victory or defeat occurs
    - Coloring the keys according to the guesses so far

---

## Interacting with the Window
- The `WordleGWindow` object contains its own information about what is happening in the window at any given point
- You **must** interact with it to:
	- Get information you need
	- Update information in the window
- A general algorithm/pattern that will be frequently used is to:
	- Get some information from the window
	- Use that information in your program to make a decision about something
	- Update the new information back to the window

---

## Your Toolbox
- Utilize the special functions/methods provided by the graphics data type: `WordleGWindow`
	- These are documented in the guide, and include, but are not limited to, things like
		- Getting or setting a letter in a particular box
		- Getting or changing the color of a given box
		- Changing which row is used when characters are typed in
- Variables and functions
- Control statements
	- Good use of loops and if statements will be very useful
- String functions and operations

---

## An Approach to Success
- Each project is accompanied by a highly detailed guide: **read it!**
	- Explains background ideas so that you can understand the big picture of what you are needing to do
	- Also included a breakdown of individual _milestones_
		- A _milestone_ is a discrete checkpoint that you should ensure is working (and that you understand!) before moving on
        - Whenever you complete a milestone, **you should upload your current code to GitHub.**
- Projects are all about managing complexity. If you start trying to implement milestones out of order, you are asking for disaster
- Don't let yourself get overwhelmed by scale. Focus on one particular milestone at a time, which should involve focusing only on a small part of your overall code

---

## A Few Other Hints
- Despite there being multiple files in the starting repository, you only need to edit one yourself: `wordle.py`
- You will have an easier time here if you define all your helper functions _inside_ the main `wordle` function that is defined in the starting template
- TEST TEST TEST!
	- Beyond just not doing something that the guide requests, the most common reason student's lose points is because they didn't test their code well
- If you want the possibility of a 100%, then you need to do at least one extension. But do not start **any** extensions until you are confident you have achieved everything the guide required, and have TESTED IT

---