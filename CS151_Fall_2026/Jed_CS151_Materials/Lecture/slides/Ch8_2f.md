---
title: "The Sorting Hat"
author: Jed Rembold
date: "April 17, 2026"
slideNumber: true
theme: python_catppuccin
highlightjs-theme: catppuccin-mocha
width: 1920
height: 1080
transition: slide
hash: true
history: false
---
## Happy Penultimate Friday!!
::::::{.cols style='font-size:.7em'}

::::col
- Scan the QR code or go to [https://tools.jedrembold.prof/daily](https://tools.jedrembold.prof/daily)
- Fun group question: What is one thing that you've had to sort recently?

![](../images/group_seating_locs_Ford102.png){width=40%}
::::
::::{.col style='flex-grow:.5'}
![](https://barcode.orcascan.com/?text=fNBj5Y&data=https://tools.jedrembold.prof/daily?code=fNBj5Y){width=100%}
::::
::::::

<!-- Comments
-->


## Quick Announcements
:::{style='font-size: .8em'}
- Midterm 2 results out
- Grade Reports out this weekend
- Enigma due on Monday night!
- Introducing the last project on Monday
  - NO VIDEO
:::

## Midterm 2 Debrief
::::::{.cols style='align-items:center'}
::::{.col style='flex-grow:1.5'}
\begin{tikzpicture}%%width=80%
  \begin{axis}[
      width=8cm,
      xlabel= Percent,
      ylabel= Number of Students,
      yticklabels={,,},
      ymajorticks=false,
      ylabel near ticks,
      color=white,
      ]
      \addplot [hist={density, bins=5, data min=40, data max=100}, fill=Orange] table[y=perc, col sep=comma] {../../data/Midterm2_Results_S2026.csv};
  \end{axis}
\end{tikzpicture}

::::

::::col
- Final breakdown:
    - Max: 105%
    - Average: 70.87%
    - Median: 70.45%
    - St Dev: 21.7%

::::
::::::

## Exam Corrections
:::{style='font-size:.8em'}
- Given this situation, I am going to offer some exam corrections
- If you lost points on a non-extra credit problem, you can earn up to 50% of the lost points back by:
  - _Creating a Trilogy Portfolio_: Collecting learning objectives, identifying past examples in in-class work and in your work, synthesizing why you didn't make the connections and how to improve going forwards
  - _Creating a **new** problem and solution_: New problem should address at least 80% of your identifying learning objectives, and your solution should be correct. Must also write a "Design Rationale" paragraph about why you made the choices you did in writing your solution.
- Full guide can be found [here](https://people.willamette.edu/~jjrembold/class_files/cs151/ExamCorrections.html)
- Must be completed for **each** problem you want points back on
- Due midnight of May 1st. Past that point, you will not be able to submit.
- 100% optional, and you can not earn over a 100% by doing corrections
:::


## Daily LO's
- How does selection sort operate?
- How can we get an idea for how an algorithm will scale just by looking at the code?
- What is Big-O notation?
- Can we identify examples of Big-O notation?

# Group Problems

## Problem 1: Sort It!
- I am distributing small stacks of playing cards to each of your groups
- Designate:
  - The processor: the one pointing at the current card that is being looked at
  - The memory: the one whose left and right hands will mark the special positions
  - The counter: the one tallying how many cards have been looked at
- Shuffle the cards and deal out 5 in a row
  - Sort them according to selection sort, following your roles
  - How many cards did you look at? Does that agree with what you'd have thought?
- Shuffle all the cards back together and deal them all out.
  - Sort again. How many cards were looked at this time? Does this agree any better?

## Problem 2: Real-World O
- We are going to cycle through some real-world scenarios here
- For each, you'll have about 2 minutes to discuss with your group what Big-O scaling you think the process would involve


## Problem 2a: The Librarian
- Checking a shelf of books to see if any have a torn cover.

## Problem 2b: The Mechanic
- Grabbing the largest wrench in a toolbox organized with molded slots for each tool.

## Problem 2c: Favorite Movies
- Finding 3 people in a class who all share the same favorite movie.

## Problem 2d: The Warehouse
- Retrieving a part from the bin labeled "Part #105" in a large, organized warehouse.

## Problem 2e: The Wedding Planner
- Creating a seating chart that ensures that no "mortal enemies" are seated together at the same table.


## Problem 3: Algorithm Archaeology
- You have written a lot of code over the course of the semester!
- The following slide will have a handful of target "bounties"
- Your task is to fine examples of each bounty in code that you or someone in your group has written over the course of the semester.
- Be prepared to defend your choices to another group!

## Problem 3: The Bounties
- Find a snippet that looks like a single $\mathcal{O}(N)$ loop but is actually $\mathcal{O}(N^2)$ because of a built-in Python function.
- Find an $\mathcal{O}(1)$ operation
- Find an $\mathcal{O}(N^2)$ operation that does **not** use two nested for loops
- Find an $\mathcal{O}(N)$ operation that finishes in $\mathcal{O}(1)$ under special conditions
- Find the heaviest code you wrote this semester. How does it scale?

## Problem 4: Designing a Disaster
- This is a coding problem!
- Linear search is usually $\mathcal{O}(N)$ in the worst case situation.
- Design a searching algorithm that runs in $\mathcal{O}(N^3)$
  - It must still work! That is, it must still return a correct answer.
