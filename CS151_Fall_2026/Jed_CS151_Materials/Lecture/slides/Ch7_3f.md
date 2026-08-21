---
title: "Comprehending List Methods"
author: Jed Rembold
date: "March 6, 2026"
slideNumber: true
theme: python_catppuccin
highlightjs-theme: catppuccin-mocha
width: 1920
height: 1080
transition: slide
hash: true
history: false
---
## Its Friday!
::::::{.cols style='font-size:.8em'}

::::col
- Scan the QR code or go to [https://tools.jedrembold.prof/daily](https://tools.jedrembold.prof/daily)
- Fun group question: If you had to predict, what is the most likely instance where mutability will mess you up this semester?

![](../images/group_seating_locs_Ford102.png){width=50%}
::::
::::col
![](https://barcode.orcascan.com/?text=JC4b45&data=https://tools.jedrembold.prof/daily?code=JC4b45){width=60%}
::::
::::::

<!-- Comments
-->


## Quick Announcements
:::{style='font-size: .8em'}
- Breakout due on Monday!
  - You probably should be starting or working on collisions at the moment. Otherwise you may be behind
- Next week will be the last problem set!
- I'm working on PS4 scoring and then grade reports this weekend
:::

## Daily LO's
- Correctly trace code with list methods and mutability considerations
- Work with common list methods
- Practice using lists to tabulate values

# Group Problems

## Problem 1: Tracing Clues
::::::cols
::::col
Given the code to the right, what would be the printed value of `A`?


:::{.poll}
#. `['Fox', 'Giraffe', 'Hippo', 'Iguana']`
#. `['Fox', 'Hippo', 'Iguana']`
#. `['Iguana', 'Fox']`
#. None of the above
:::

::::

::::col
```{.python style="max-height:900px"}
A = [
	 'Fox',
	 'Giraffe', 
	 'Hippo'
	]
A.append('Iguana')
A[:].reverse()
B = A
for anim in B:
	if anim[1] == 'i':
		B.remove(anim)
print(A)
```
:::::
::::::

## Problem 2a: Some Cleaning
- This is a coding problem. Work in pairs or trios on a single computer
	- Discuss your algorithm **BEFORE YOU WRITE ANY CODE**. Make sure everyone understands.
- The file `raw_data.py` contains the constant `DATA`, which is a large list of strings
- Many of those strings are numbers, but some are not
- Your first task is to use a loop and `append` to create a list of only the entries that are numbers
- Your result should be a list of numbers, so you'll need to convert them from strings

## Problem 2b: Cleaning Comprehension
- Rewrite your above code to generate the exact same list, but using a list comprehension
- Should be able to compare the lists you got from each method, and they should have identical contents

## Problem 2c: Purging
- Both the previous approaches created a _new_ list in memory with the desired traits
- What if we wanted to prune the "bad" values out of the original list?
- Write an approach that would accomplish this, ensuring that the list `id` before your code and after you code is still the same!

## A Tabulation Aside
- Lists can also be useful when you have a collection of values and you need to count how many values fall into different "bins"
	- This is commonly called _tabulation_
- You could accomplish this with multiple counting variables, but it is unreasonable to define and track 50+ variables
	- With a list, the number at each index represents a count of something
	- Instead of creating 50+ variables, you just have a list of 50+ counts
- Useful if you can equate bins to indexes directly, but sometimes you just need to define what index corresponds to what category

## Problem 2d: Tabulation
- The cleaned data list contains number values ranging from 0 to 25
- Use tabulation to count how many times each number appears in the array
- What are the top three more frequently occurring numbers?


# Demo

## Letter Frequencies
- Code breakers can often use information about how likely a letter is to appear in different languages to determine what a symbol is likely to correspond to
- We have the English dictionary at our disposal, so let's determine the 5 **least** frequently occurring letters in the English dictionary
