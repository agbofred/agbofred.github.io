---
title: "Bombastic Booleans"
author: Jed Rembold
date: "January 28, 2026"
slideNumber: true
theme: python_catppuccin
highlightjs-theme: catppuccin-mocha
width: 1920
height: 1080
transition: slide
hash: true
history: false
---
## You've made it halfway!
::::{style='font-size:.8em'}
- Scan the QR code or go to [https://tools.jedrembold.prof/daily](https://tools.jedrembold.prof/daily)
- Class code is `lcjjHj`
- Introduce yourselves! Fun question: What is your favorite riddle about liars/truth-tellers?
::::
::::::cols

::::col
![](../images/group_seating_locs_Ford102.png){width=60%}
::::
::::col
![](https://barcode.orcascan.com/?data=https://tools.jedrembold.prof/daily?code=lcjjHj){width=60%}
::::
::::::

<!-- Comments
- Problem 1 I think was still instructive, and worth keeping
- Problem 2 is good, and NEED TO UPDATE VIDEO TO PROPERLY TEACH THIS!
- Problem 3 I think only needed the "hard" version. We skipped the short
- Problem 4 was a bit rushed. And asking them to print strings feel weird before introducing strings.
- Live coding I think was good, both from a algorithm and conceptual viewpoint
-->


## Quick Announcements
- Problem Set 2 is due Monday!
  - All problems should be approachable after today
- Sections today or tomorrow! Don't forget!
- Faculty candidate teaching demo before class on Friday
  - "An Introduction to Human Factors and Ergonomics"
  - We always value student feedback about potential faculty hires!!


# Group Problems

## Problem 1: Reviewing Functions
::::::{.cols style='align-items: center'}
::::col
Examining the code to the right, what is the returned value if I evaluate the expression `func2(1,5)`?
::::

::::{.col style='font-size:1em; flex-grow:1.5'}
```python
def func1(x):
	for i in range(3):
		x *= 2
	return x + x

def func2(y, z):
	A = func1(y+1) % 8
	z, A = A + z, y
	return z ** A
```
::::
::::::

## Problem 2: The Boolean Expression
What would the below expression evaluate to?

`True and not False or False and not (False or True or False) or False`{.inlinecode}

## My Shame
- I have straight up missed this in the past when teaching, and was gobsmacked last night when I realized
- Boolean operators absolutely have an order of operations:
  - Parentheses
  - `not`
  - `and`
  - `or`
- Only operations at the same "level" act left to right


## Problem 3: Gridded Booleans
::::::{.cols style='align-items: center'}
::::{.col style='font-size:.9em'}
- The grid to the right shows several comparison expressions, along with placeholders for unknown boolean operations
- It also shows a target result for each row and column
- Your task is to fill in the missing boolean operators to ensure all rows and columns evaluate to their desired target
::::

::::col

![](../images/bool_logic1.svg)

::::
::::::

## Problem 3b: Raising the Stakes

![](../images/bool_logic2.svg)

## Problem 4: Being Smart
- Suppose you are writing a function to "control" a thermostat for an HVAC system
- Your function has two variables as input: `current_temp` and `target_temp`
  - If the two values are within 5 degrees, you should print "Off"
  - If the current temperature is less than the target, you should print "Heating"
  - If the current temp is greater than the target, you should print "Cooling"
- If they are separated by more than 25 degrees, you should _also_ print "Warning: High Load!"
  - This is in addition to whichever of the three values you printed above

# Live-Coding

## Multiples
- I want to write a function that takes a given number as input and prints all of its integer factors
  - As a reminder, a factor of a number is a value that evenly divides the number
- I want to return a count of how many factors were printed


## A Solution
```{.python style='max-height: 800px; font-size:.8em;'}

def print_factors_of(num):
    """Prints off all the integer factors of
    the provided number, and returns the count of
    them.
    
    Algorithm:
        Loop over all numbers less than num
        Check if factor by seeing if remainder is 0
        Print and increment counter if so
    """
    possible_factor = 1
    count = 0
    while possible_factor <= num:
        if num % possible_factor == 0: # Factor found!
            print(possible_factor)
            count += 1
        possible_factor += 1
    return count

print(print_factors_of(45632636))
```
