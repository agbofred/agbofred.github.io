---
title: "Tis Tuple Time"
author: Jed Rembold
date: "March 13, 2026"
slideNumber: true
theme: python_catppuccin
highlightjs-theme: catppuccin-mocha
width: 1920
height: 1080
transition: slide
hash: true
history: false
---
## Happy Friday the 13th!
::::::{.cols style='font-size:.8em'}

::::col
- Scan the QR code or go to [https://tools.jedrembold.prof/daily](https://tools.jedrembold.prof/daily)
- Fun group question: What records do you consult or look at most often?

![](../images/group_seating_locs_Ford102.png){width=50%}
::::
::::col
![](https://barcode.orcascan.com/?text=mBZejD&data=https://tools.jedrembold.prof/daily?code=mBZejD){width=60%}
::::
::::::

<!-- Comments
-->


## Quick Announcements
:::{style='font-size: .8em'}
- Problem Set 5 due on Monday!
- We'll be introducing ImageShop on Monday
- I am basically booked solid all afternoon, so email or dm me if you have questions
:::

## Daily LO's
- Understanding when to choose tuples
- Practice working with basic tuple operations
- Practice packing and unpacking tuples

# Group Problems

## Problem 1: Tuple Tactics
::::::{.cols style='align-items: center'}
::::col
What would the code to the left print off?

:::poll
#. `2`
#. `4`
#. `6`
#. This would error
:::
::::

::::col
```python
A = (1, 2, (3, 4))
B = A[1::2]
x, y, z = A
for i in range(x):
	B += z
print(y * B[-2])
```
::::
::::::


## Problem 2a: Karel Trackers
- This is a coding problem. Work in pairs or trios on a single computer, and discuss your algorithm **BEFORE YOU WRITE ANY CODE**. 
- The file `positions.py` exports a single constant called `KAREL_POS`, which is a _list_ of _tuples_, recording what street and avenue intersection Karel is located at different elapsed times
	- The tuples are ordered by time, street (x), avenue (y)
- Your task:
	- Return the start and end times between which Karel moved the furthest
	- Since Karel can't move diagonally, you can compute distance as
	  $$ |x_1 - x_2| + |y_1 - y_2|$$


## Problem 2b: Lazy Logging
- Swap who is typing!
- Sometimes Karel doesn't move in a given interval
- Here, we'd like to enhance the existing records of Karel's position by including a boolean flag if Karel moves in the _following_ interval
	- The last record will always have `None` here, since we don't know what the next position is
- For example, the left should become the right:

::::::{.cols style='font-size:.8em'}
::::col
```python
KAREL_POS = [
	(0, 4, 3),
	(1, 4, 3),
	(2, 3, 3),
	(3, 0, 2),
	(4, 0, 2)
]
```

::::

::::col
```python
KAREL_POS = [
	(0, 4, 3, False),
	(1, 4, 3, True),
	(2, 3, 3, True),
	(3, 0, 2, False),
	(4, 0, 2, None)
]
```

::::
::::::

# Demo

## Yarn Art
::::::cols
::::col
- Points, or tuples of an x and y position, often show up in graphical applications
- Let's make some yarn art, where we:
	- Place a set of "pegs" at regular intervals around the border
	- Tie a piece of "yarn" around one peg
	- Loop that yarn around the peg a number of pegs ahead
	- Continue until we return to our starting point
::::

::::col
![](../images/yarn_pattern.svg)

::::
::::::

