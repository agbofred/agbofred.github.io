---
title: "Squashing Bugs"
author: Jed Rembold
date: "February 2, 2026"
slideNumber: true
theme: python_catppuccin
highlightjs-theme: catppuccin-mocha
width: 1920
height: 1080
transition: slide
hash: true
history: false
---
## Welcome back!
::::{style='font-size:.8em'}
- Scan the QR code or go to [https://tools.jedrembold.prof/daily](https://tools.jedrembold.prof/daily)
- Class code is `hVSGho`
- Introduce yourselves! Fun question: What is your favorite bug?
::::
::::::cols

::::col
![](../images/group_seating_locs_Ford102.png){width=60%}
::::
::::col
![](https://barcode.orcascan.com/?data=https://tools.jedrembold.prof/daily?code=hVSGho){width=60%}
::::
::::::

<!-- Comments
-->


## Quick Announcements
- Problem Set 2 is due tonight!
- Please forgive me about PS1 feedback. I tried so hard.
- Problem Set 3 posted by end of day


# Group Problems
## Prep
- All problems today revolve around troubleshooting and finding errors in some "launch code"-esque checks
- You will want at least someone to have downloaded the all the lecture contents linked in Discord
- To get `rich` installed easily, I have included a Python file in the contents that you should just need to run, and it will (in theory) handle things automatically for you.
  - You'll need this for the problems today


## Problem 1: Stress Tests
- The `p1.py` file is doing some stress testing, but has some issues
- Focus on using print statements to track down where things are going wrong
- How could you get around this issue?


## Problem 2: Systems Go?
- The `p2.py` file **should** be saying that all systems are a go, but it is not
- Pay particular attention to the documentation to figure out what has gone wrong
- You should be able to fix all the problems by only changing 3-5 lines

## Problem 3: Sufficient Shields?
- The `p3.py` file should **also** be saying that all systems are go, but is not
- Instead of using print statements here, use only your debugger to track down what is happening and how to fix it

## Problem 4: System Scanning
- Finally, `p4.py` should be verifying a scan, but is instead erring out. Use the printed error alongside print statements or the debugger to establish where things have gone awry
- How can you easily fix this problem?

# Live-Coding

## Writing Tests
- Let's write a suite a tests for each of the library functions
- Always a good idea to target `assert` statements at both typical values, but also edge cases
- Let's try to come up with at least 3-4 for each function


## A Solution
```{.python style='max-height: 800px; font-size:.8em;'}
# Added once completed!
```
