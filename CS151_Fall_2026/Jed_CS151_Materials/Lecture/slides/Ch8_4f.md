---
title: "Merge Sort"
author: Jed Rembold
date: "April 24, 2026"
slideNumber: true
theme: python_catppuccin
highlightjs-theme: catppuccin-mocha
width: 1920
height: 1080
transition: slide
hash: true
history: false
---
## Happy Friday!
::::::{.cols style='font-size:.7em'}

::::col
- Scan the QR code or go to [https://tools.jedrembold.prof/daily](https://tools.jedrembold.prof/daily)
- Fun group question: True or False: guessing today's entrance code is an NP problem?

![](../images/group_seating_locs_Ford102.png){width=40%}
::::
::::{.col style='flex-grow:.5'}
![](https://barcode.orcascan.com/?text=T9K8Bv&data=https://tools.jedrembold.prof/daily?code=T9K8Bv){width=100%}
::::
::::::

<!-- Comments
-->


## Quick Announcements
:::{style='font-size: .8em'}
- Infinite Adventure due on Monday
- Midterm 2 corrections due a week from today
- Luau tomorrow!
- No videos to watch before class next week.
  - I'm just going to present on some fun/useful libraries/tools and we'll have time for a few activities
:::


## Daily LO's
- How does merge sort work?
- How does merge sort scale?
- What are P vs NP type problems?

# Group Problems

## Problem 1: Sort It Again!
:::{style='font-size:.9em'}
- I am distributing small stacks of playing cards to each of your groups
- Designate:
  - The splitter: the one responsible for cutting the array in half repeatedly
  - The pointers: the ones responsible for pointing at the leftmost unused card when merging
  - The merger: the one responsible for comparing cards and merging the smallest into the next available space. Count how many merges happen!
- Shuffle the cards and deal out 5 in a row
  - Sort them according to merge sort, following your roles
  - How many total merges happened? Does this look like $5\log_2(5) = 11.6$?
- Shuffle all the cards back together and deal them all out.
  - Sort again. How many merges this time? Does it look like $12\log_2(12) = 42$?
:::

## Problem 2: Classification Court
- We are going to again cycle through some real-world scenarios
- For each, you'll have 2 minutes to discuss within your group about if the problem should be classified as a P on NP type problem.

## Problem 2a: The Grocery List
- You have prices for different items on a grocery list and need to determine the total cost

## Problem 2b: The Delivery Route
- You have 20 houses to deliver packages to. Find a route that will visit all the houses and return you home at the end having driven less than 10 miles.

## Problem 2c: Exam Grading
- A student turned in a multiple-choice test. Use an answer key to see if they got a 100%.

## Problem 2d: Password Cracking
- I forgot my password and need to figure it out to access my email.

## Problem 2e: Section Scheduling
- I have 30 students with different availability. Can I schedule 3 sections that will work for all students?

## Problem 2f: Registration
- Given prerequisites and planned offerings, is it possible to graduate with this major in the next two years?

## Problem 2g: Beyond Checkers
- Given a current chessboard layout, can you choose a move that guarantees you the win, assuming your opponent plays perfectly?

## Problem 2h: Shopping Spree!
- Find a combination of items in your favorite grocery store that total to exactly \$100.


## Problem 3: Dining Plans
- Say you have $15 flex-dollars left and pay a visit to Blitz Market.
  - A P type problem might be: What is the single most expensive item you can afford?
- But how could you "upgrade" this problem?
  - What else could you ask or what constraints could you add that would transform this into an NP type problem?
  - Remember, NP problems are still easy to verify
  - But to solve them you usually would have to check all branching possibilities

