---
title: "Returning to Functions"
author: Jed Rembold
date: "February 16, 2026"
slideNumber: true
theme: python_catppuccin
highlightjs-theme: catppuccin-mocha
width: 1920
height: 1080
transition: slide
hash: true
history: false
---
## Welcome Back!!!
::::::{.cols style='font-size:.8em'}

::::col
- Scan the QR code or go to [https://tools.jedrembold.prof/daily](https://tools.jedrembold.prof/daily)
- Introduce yourselves! Fun question: What is your favorite sandwich?

![](../images/group_seating_locs_Ford102.png){width=50%}
::::
::::col
![](https://barcode.orcascan.com/?text=kdxOup&data=https://tools.jedrembold.prof/daily?code=kdxOup){width=60%}
::::
::::::

<!-- Comments
-->


## Quick Announcements
- Project 1 due tonight!
- PS2 feedback went out. I'm working on PS3 feedback now
- Our first exam is Friday!
	- Study exams are out
		- Solutions to Exam 1 posted tonight
        - Solutions to Exam 2 posted Wednesday
	- Sections this week will be for reviewing and studying
    - Friday weirdness:
        - You will be in Collins 323, since the BoT takes over this room
        - I will not be there. Prof Deutschbein will be proctoring

# Virtual Proctor

## Testing
- You are allowed to access a wide variety of digital materials on the exam, which is good
- Giving you that access makes it difficult for me to verify the integrity of the exam though, which is less good
- Enter the virtual proctor tool, which takes periodic snapshots of your screen during an exam
- Let's test it now, to see if it holds up to an entire class sharing

# Group Problems

## Problem 1: Predicate Refactoring
- `Prob1.py` in today's contents contains four different poorly constructed predicate functions
- Your task is to clean them up!
    - Add docstrings as necessary
    - Reduce each function to a 1-liner (2 with the function header) using boolean operations
    - The literals `True` and `False` should not show up in the function _anywhere_


## Problem 2: Sandwich Making
- `Prob2.py` contains a basic function definition to create and print a sandwich to the screen
- At the bottom you can specify the arguments to craft a particular sandwich. Enter arguments to create a:
    - Non-toasted turkey sandwich on sourdough with mustard and swiss. Cut in two.

## Problem 2: Sandwich Defaults
- You may have made a mistake entering in the ingredients, or just lamented how much you had to type
- Let's provide some good defaults.
- Decide with your group what a reasonable default would be for each of the initial parameters, and adjust the `make_sandwich` function header to create those defaults

## Problem 2: More Sandwiches
- Create and print the following sandwiches, typing as little into the function call as possible (use your defaults where you can!)
    - A beef sandwich on white bread with swiss cheese and mustard. Toasted and cut.
    - A bologna sandwich on rye with cheddar cheese and mustard. Untoasted and uncut.
    - A ham sandwich on white bread with cheddar cheese and mayo. Untoasted and cut.


## Problem 3: Utility Functions
- Write one function that could become part of a PGL utility library
- It should create a GObject, position it, customize it, and return it
- Should include many parameters (with sane defaults) to customize, detailed on next slide

## Problem 3: Parameters to Include
::::::cols
::::col
- If a GRect or GOval, should be able to customize:
    - Center position
    - Dimensions
    - Coloring
    - If filled
    - If a black border should be visible
::::

::::col
- If a GLabel, should be able to customize:
    - Center position
    - Text
    - Font
    - Coloring
    - If text should be converted to uppercase
::::
::::::





# Live Coding

## Growing Trees
::::::cols
::::col
- I'd like to write a utility function to draw a pine tree directly to the canvas
- I'll specify the bottom location of the tree, the height, and whether it should have snow on its branches
::::

::::col
::::
::::::

