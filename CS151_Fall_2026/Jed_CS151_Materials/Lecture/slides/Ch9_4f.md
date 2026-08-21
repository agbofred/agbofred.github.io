---
title: "Inheriting Class"
author: Jed Rembold
date: "March 20, 2026"
slideNumber: true
theme: python_catppuccin
highlightjs-theme: catppuccin-mocha
width: 1920
height: 1080
transition: slide
hash: true
history: false
---
## Spring Break is SO CLOSE!
::::::{.cols style='font-size:.7em'}

::::col
- Scan the QR code or go to [https://tools.jedrembold.prof/daily](https://tools.jedrembold.prof/daily)
- Fun group question: What is one thing you'd eventually like to inherit from your parents?

![](../images/group_seating_locs_Ford102.png){width=40%}
::::
::::{.col style='flex-grow:.5'}
![](https://barcode.orcascan.com/?text=NrCdJe&data=https://tools.jedrembold.prof/daily?code=NrCdJe){width=100%}
::::
::::::

<!-- Comments
-->


## Quick Announcements
:::{style='font-size: .8em'}
- Hopefully you have made good ImageShop progress!
	- Due after break, but don't put it off!
- I'm going to try to have PS4 and PS5 scored by the end of break, and then will push out a new grade report (which will also include Project 2)
:::


## Daily LO's
- Define a class that inherits from another
- Override parent methods in a child class
- Properly use `super()` in a child constructor

# Group Problems

## Problem 1a: I'm on a Boat!
- This is a coding problem. Work in pairs or trios on a single computer, and discuss your algorithm **BEFORE YOU WRITE ANY CODE**. 
- I have provided to you already a `Vehicle` class, which tracks several attributes and includes an initial `__repr__` method
- Your task:
	- Create a new `Boat` class that inherits from `Vehicle`
	- Its constructor should only accept a weight, as the terrain type should always be set to `"water"`
	- Override its `__repr__` method to correctly print out command needed to create the new boat objects. So it should return something like `"Boat(5000)"`, if 5000 was the weight.


## Problem 1b: I'm on a really big boat!
- Swap who is typing!
- Now define a `Carrier` class that inherits from boat
- A carrier has two new attributes to track:
	- A `capacity` (integer) which should be provided when a carrier is created
	- An `onboard` list which tracks what planes are currently onboard. It always starts empty when the carrier is created.
- Override its `__repr__` method to correctly print out command needed to create the new Carrier objects. So it should return something like `"Carrier(8000, 3)"`, if 8000 was the weight, and it had a capacity for 3 planes


## Problem 1c: Insert Plane Here
- Swap who is typing!
- Add a method to the `Carrier` class of `add_plane`, which accepts a plane's weight as an argument
	- If the number of planes currently on the carrier is less than its capacity, then add the weight to the onboard list and increase the carriers own weight by that amount
	- Otherwise, just print `"Deck full!"`


# An Explosive Demo Continues
## The Objective
::::::cols
::::col
- We are trying to write a program to simulate a fireworks show in PGL
- We are already working on a `Firework` class, and have many attributes defined
- How could we use inheritance in this case?
- Let's define all the necessary methods to make this show a reality!
::::

::::col
![](../images/fireworks.png)
::::
::::::
