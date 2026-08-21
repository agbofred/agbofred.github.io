---
title: "Random Graphics"
author: Jed Rembold
date: "February 11, 2026"
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
- Introduce yourselves! Fun question: What is your favorite shape?

![](../images/group_seating_locs_Ford102.png){width=50%}
::::
::::col
![](https://barcode.orcascan.com/?text=CtegqI&data=https://tools.jedrembold.prof/daily?code=CtegqI){width=60%}
::::
::::::

<!-- Comments
-->


## Quick Announcements
- By working on Project 1! Due Monday
- Sections today and tomorrow!
- Our first exam is a week from Friday!
	- Study materials will come out on Friday
	- Sections next week will be for reviewing and studying


# Group Problems

## Problem 1: 5d100s
- Every week before we start playing, each person in my D&D group rolls 5 (virtual) 100-sided dice
	- A 100-sided dice has numbers 1-100 on its faces
- We like to use the _sum_ of the 5 dice to predict how lucky or unlucky we'll be that night
- But what would be exceptional?
- Your group's task: Roll 5 100-sided dice 10,000 times. What is the maximum value you got?


## Problem 2: Olympic Flags
- With the Olympics going on, you've probably seen way more international flags than usual
- Let's recreate some in PGL!
- Each member of your group should choose a different flag. Your task is to recreate it as exactly as possible.
- A list of countries with flags that would be very approachable with our current shapes follows on the next slide
	- You'll need to search for the flag itself to see what you need to replicate (Wikipedia is great for this)

## Country Flag Options
::::::cols
::::col
- Italy
- Japan
- Laos
- Germany
::::

::::col
- Thailand
- Latvia
- Switzerland
- France

::::
::::::



## Problem 3: The Drunken Robot
- Determine the middle of your window and save the `x` and `y` coordinates. This is your robots current location.
- Draw a 25x25 square at that location (doesn't need to be centered, but could be!)
	- Make it filled with a fill color of your choice
- Now, for 50 iterations:
	- Determine the next direction (North, South, East or West) randomly
	- Update the robot's location variables accordingly, assuming they moved exactly 25 pixels in that direction
	- Draw a **new** square at the robot's new location (with a different fill color than your starting color)
- Admire your robot's little drunken walk! Play around with more iterations!


# Live Coding

## Estimating Pi
- One of the ways that the value of $\pi$ can be estimated is by looking at the number of random points that strike a circle vs a surrounding box
- Our task here is to both estimate they value of $\pi$ using random numbers in this fashion, but to also visualize it!


## A Solution
```{.python style='max-height: 800px; font-size: .8em'}
from pgl import GWindow, GRect, GOval
import random

WIDTH = 800
HEIGHT = 800

SIZE = 700
DART_SIZE = 10

gw = GWindow(WIDTH, HEIGHT)

background = GRect(
    WIDTH / 2 - SIZE / 2,
    HEIGHT / 2 - SIZE / 2,
    SIZE,
    SIZE
)
background.set_filled(True)
background.set_color('gray')
gw.add(background)

target = GOval(
    WIDTH / 2 - SIZE / 2,
    HEIGHT / 2 - SIZE / 2,
    SIZE,
    SIZE
)
target.set_filled(True)
target.set_color('darkgray')
gw.add(target)

attempts = 1000
successful_strikes = 0
for i in range(attempts):
    x = random.uniform(WIDTH / 2 - SIZE / 2, WIDTH / 2 + SIZE / 2)
    y = random.uniform(HEIGHT / 2 - SIZE / 2, HEIGHT / 2 + SIZE / 2)
    dart = GOval(
        x - DART_SIZE / 2,
        y - DART_SIZE / 2,
        DART_SIZE,
        DART_SIZE
    )
    dart.set_filled(True)
    distance_to_center = (
        (x - WIDTH / 2)**2 + (y - HEIGHT / 2)**2
    ) ** (1/2)
    if distance_to_center < SIZE / 2:
        dart.set_fill_color('red')
        successful_strikes += 1
    else:
        dart.set_fill_color('blue')
    gw.add(dart)

# I forgot this extra factor of 4 in class! That is why it wasn't working initially
print(successful_strikes / attempts * 4 )
```
