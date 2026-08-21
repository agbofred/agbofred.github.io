---
title: "The Search for Efficiency"
author: Jed Rembold
date: "April 13, 2026"
slideNumber: true
theme: python_catppuccin
highlightjs-theme: catppuccin-mocha
width: 1920
height: 1080
transition: slide
hash: true
history: false
---
## Not Many Mondays Left!
::::::{.cols style='font-size:.7em'}

::::col
- Scan the QR code or go to [https://tools.jedrembold.prof/daily](https://tools.jedrembold.prof/daily)
- Fun group question: What do you lose most often that you need to search for? What strategy do you use to search for it?

![](../images/group_seating_locs_Ford102.png){width=40%}
::::
::::{.col style='flex-grow:.5'}
![](https://barcode.orcascan.com/?text=bvRhZ3&data=https://tools.jedrembold.prof/daily?code=bvRhZ3){width=100%}
::::
::::::

<!-- Comments
-->


## Quick Announcements
:::{style='font-size: .8em'}
- I'm sorry, but I didn't quite make it through Midterm 2 feedback :/
- Grade Reports out though?
- Don't forget about Enigma!
	- Due _next_ Monday night
- No class on Wednesday!
  - Sections **are** still happening Wednesday and Thursday, so don't forget to attend!
:::


## Daily LO's
- How can we think about the "efficiency" of an algorithm?
- What are some common searching algorithms?
- How can we "benchmark" and algorithm
- Can we build an empiric model of how some code will scale?

# Group Problems

## Problem 1: Time It!
- This is a coding problem. Work in pairs or trios on a single computer, and discuss your algorithm/approach _before_ you write any code!
- Write a function to benchmark the time it takes an arbitrary search function to run on a particular array and with a particular target
- You can use the `perf_counter()` function from the `time` library to get an arbitrary second count
  - Take two and subtract to get elapsed time
- Return the elapsed time

## Problem 2: Averaging Out
- Swap who is typing!
- If the target is near the start, we are likely to find it much faster
- It is better to randomly choose a bunch of targets, and then average over all the times
- Complete `compute_avg_time` to return the average benchmark time for 100 random targets
  - Randomly choose targets both inside and outside of the array!

## Problem 3: Multiple Arrays
- Swap who is typing!
- Ideally we want to see how our function _scales_, as the arrays get larger
- Complete `sweep_of_sizes` to compute the average benchmark for each size in the list
  - Choose a data type to return the results that include both the array size and the average time
    - You have several good options! Which do you prefer here?

## Problem 4: Table Display
::::::cols
::::{.col style='font-size:.8em'}
- Swap who is typing!
- Looking at the results in the data type you chose is not the nicest
- Complete `display_results` to print out a table of the computed output
- Add a third column for "Ratio", which is the current time divided by the previous time
- How does `jump_search` compare to our other algorithms?

::::

::::col
```{.text style='font-size:.8em'}
      N       Time (sec)  Ratio
          10    2.84e-07
         100    1.44e-06   5.06
       1,000    1.87e-05  13.00
      10,000    2.05e-04  10.99
     100,000    2.03e-03   9.91
   1,000,000    2.04e-02  10.02
  10,000,000    2.05e-01  10.04
```

::::
::::::



# Demo?

## Histogram of Times
- Let us further explore the benchmarked times to look at the distribution of times for each algorithm
- Are they clustered around certain values or every spread? Why might that be the case?
