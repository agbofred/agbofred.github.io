---
title: "Clicky Clicky"
author: Jed Rembold
date: "February 23, 2026"
slideNumber: true
theme: python_catppuccin
highlightjs-theme: catppuccin-mocha
width: 1920
height: 1080
transition: slide
hash: true
history: false
---
## Welcome Back!
::::::{.cols style='font-size:.8em'}

::::col
- Scan the QR code or go to [https://tools.jedrembold.prof/daily](https://tools.jedrembold.prof/daily)
- Introduce yourselves! Fun question: What is your favorite sandwich?

![](../images/group_seating_locs_Ford102.png){width=50%}
::::
::::col
![](https://barcode.orcascan.com/?text=Ltno5v&data=https://tools.jedrembold.prof/daily?code=Ltno5v){width=60%}
::::
::::::

<!-- Comments
-->


## Quick Announcements
:::{style='font-size: .8em'}
- I am going to try to have midterms graded by Friday, but I have a lot I am catching up on
- Nothing due tonight, but new homework is out!
    - Dealing with graphics
    - First two problems would already be doable by you
    - Third is doable after today
:::

# Group Problems

## Problem 1: Events and the Event Loop
- Each group is going to take on the role of a simple program, comprised of several parts
    - The Event Loop (The manager): this should be someone comfortable moving around the room
    - The Event Queue (The inbox): this individual will manage incoming events and distribute the oldest one to the loop
    - The Listeners (The sensors): these students will watch for real world actions, and notify the queue when they see one

## Problem 1: The "Code"
- You are now getting distributed several things
    - Role cards: these let the listeners know what they are listening for, and the loop to know what actions it needs to perform. The event queue also gets a special event to listen for, which won't come up that often
    - Event cards: these are labeled cards that the listeners will hand to the queue when they perceive an event. Once the queue has shown the loop a card, it should be given back to the listeners to be reused

## Problem 2: PGL Listeners
- Here you have a coding task. Work in pairs or trios on a single computer.
- Your task is to:
    - Add a black filled background rectangle to the window the same size as the window
    - Add a while filled circle somewhere near the middle (no need to be exact)
    - Add a listener so that when the mouse is clicked, the background rectangle changes to a new random color
    - Add a listener so that when the mouse is double clicked, the circle moves down the screen one diameter's distance

# Live Coding

## Line Art
- Suppose we want to make a basic drawing program
- When the user presses the mouse down, we start drawing a line
- As the user drags the mouse around, we actively update the placement of that line to end at the users cursor
- When the user releases the mouse button, we lock that line onto the screen
- Now a new click starts drawing a new line

