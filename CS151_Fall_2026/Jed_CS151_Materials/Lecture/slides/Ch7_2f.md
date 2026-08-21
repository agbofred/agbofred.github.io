---
title: "Mutability"
author: Jed Rembold
date: "March 4, 2026"
slideNumber: true
theme: python_catppuccin
highlightjs-theme: catppuccin-mocha
width: 1920
height: 1080
transition: slide
hash: true
history: false
---
## Happy Hump Day!
::::::{.cols style='font-size:.8em'}

::::col
- Scan the QR code or go to [https://tools.jedrembold.prof/daily](https://tools.jedrembold.prof/daily)
- Fun group question: If you could have a fun mutation, what would it be?

![](../images/group_seating_locs_Ford102.png){width=50%}
::::
::::col
![](https://barcode.orcascan.com/?text=uKF6Dr&data=https://tools.jedrembold.prof/daily?code=uKF6Dr){width=60%}
::::
::::::

<!-- Comments
-->


## Quick Announcements
:::{style='font-size: .8em'}
- Breakout!
- Sections meeting today or tomorrow. Make sure you attend!
- I am having to move my Wed office hours from 4:30-5:30 to 2-2:40 for the rest of the semester
  - I'll be around even longer on Tuesdays and Thursdays though
- I'm going to be working on getting grade reports out this weekend
:::

## Daily LO's
- Correctly trace code working with lists where mutability matters
- Work with and think about the id of mutable objects
- Practice interacting with the VSCode debugger

# Group Problems

## Problem 1: Tracing Clues
What would the below code print out at the end?
```python
ballroom = ['Miss Scarlet', 'Mr. Green', 'Prof Plum']
hall = ['Mrs. Peacock', 'Col. Mustard']
study = ['Mrs. White']
house = [ballroom, hall, study]
hall = hall + study
for character in ballroom:
    if character[0] == 'P':
        house[1][0] = character
print(hall)
```

:::notes
Python actually has a special use of the `+=` for mutable objects, where it effectively does an extend() to update them IN PLACE. Who knew!?
:::

## Problem 2: The Escape
- Work in pairs or trios on a single computer
- At the top of the lecture content `maze.py` file, enter in your pair/trios names
- The idea here is that you are plunged into a mysterious maze
- To cast the escape spell, you need to collect three items: a spellbook, potion, and wand
- The trick lies in finding them

## Problem 2: The Maze
::::::{.cols style="align-items: center"}
::::{.col style='font-size: .9em'}
- Each maze is generated custom for your group
- Consists of connected rooms, depicted with a special `MazeCell` object
- Each room has:
  - Some contents. Usually `None`, but sometimes one of the items you need!
  - A series of directions that _reference_ other connected rooms (or `None`)
::::

::::col
![](../images/reference_maze.svg)

::::
::::::

## Problem 2: The Exploration
- To have a chance of finding your way out, it would help to work out the layout of your maze
- Can do so by utilizing VSCode's debugger!
- Place a breakpoint on the indicated line, and run the program in debug mode
- Now you can "explore" the `MazeCell`s by using the dropdown menu that appears
- Construct yourself a map!
  - What room connects to what? The memory address is unique here!
  - What item, if any, is in the room?

## Problem 3: Escaping!
- Given your map, construct a set of instructions that would take you from your starting position to gather all three needed items
- Express this series of instructions as a string of "NSEW" characters
- Enter it into `twisty` function when it is called at the bottom of the program, and then run the program normally. Did you escape?!


# Demo

## Deep Clues?
- Let's have a list of clue rooms where each room has a list of individuals currently within it, like in our starting question
- How could I properly "move" a character from one room to the next, given the tools we currently have?
