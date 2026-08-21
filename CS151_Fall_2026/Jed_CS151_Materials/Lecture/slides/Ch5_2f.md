---
title: "Scoping Things Out"
author: Jed Rembold
date: "February 18, 2026"
slideNumber: true
theme: python_catppuccin
highlightjs-theme: catppuccin-mocha
width: 1920
height: 1080
transition: slide
hash: true
history: false
---
## Happy Wednesday!
::::::{.cols style='font-size:.8em'}

::::col
- Scan the QR code or go to [https://tools.jedrembold.prof/daily](https://tools.jedrembold.prof/daily)
- Introduce yourselves! Fun question: What is your favorite sandwich?

![](../images/group_seating_locs_Ford102.png){width=50%}
::::
::::col
![](https://barcode.orcascan.com/?text=WTby3M&data=https://tools.jedrembold.prof/daily?code=WTby3M){width=60%}
::::
::::::

<!-- Comments
-->


## Quick Announcements
:::{style='font-size: .8em'}
- Midterm on Friday!
- Testing Accommodations? Make sure things are arranged with AES
    - I'll keep the proctoring tool live, so please still share your screen
- Bring your **charged** laptop
- Resources to ensure you can pull up rapidly:
    - The Python Summary
    - The textbook
    - Class and Section slides
    - Your notes, handwritten or electronic
    - Past work on GitHub
- Sections this week about reviewing
- Friday weirdness:
    - You will be in Collins 323, since the BoT takes over this room
    - I will not be there. Prof Deutschbein will be proctoring
:::

# Group Problems

## Problem 1: Interactive Scoping
- I am handing out folded sheets to each group. Focus initially on side A
- The idea is that each group is representing a stack frame
- You may want a scratch piece of paper out to track your variables
- When the global group tells me what would be printed, I will confirm if it is correct or not. If not, you'll need to try again from the start.

## Problem 1: Flow
- Things have been placed so that the group _behind you_ is the one responsible for any functions you need to call
- That group's function was **defined** in your group's stack/function, but I just show you the header, not the contents
- When you need to call a function, you will need to tell the group behind you what values are assigned to each parameter
- When you return a value, you need to tell the group in front of you

## Problem 1: Resolution
- Because each function is defined inside the preceding function, the immediate "enclosing" scope is the groups in _front_ of you
- If you need to determine a value not defined in your stack frame, you need to send someone "up the stack" to find that value

## Problem 2: Reversed Interactive Scoping
- Flip your folded sheet around now to side B
- The direction now is reversed, so that the group in **front** of you is who you call, and you return values to the group behind you
- Thus the group _behind you_ is your immediate "enclosing" scope

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

