---
title: "Home on the Range"
author: Jed Rembold
date: "January 30, 2026"
slideNumber: true
theme: python_catppuccin
highlightjs-theme: catppuccin-mocha
width: 1920
height: 1080
transition: slide
hash: true
history: false
---
## TGIF!
::::{style='font-size:.8em'}
- Scan the QR code or go to [https://tools.jedrembold.prof/daily](https://tools.jedrembold.prof/daily)
- Class code is `jd7WSW`
- Introduce yourselves! Fun question: Do you think you can count faster forwards or backwards?
::::
::::::cols

::::col
![](../images/group_seating_locs_Ford102.png){width=60%}
::::
::::col
![](https://barcode.orcascan.com/?data=https://tools.jedrembold.prof/daily?code=jd7WSW){width=60%}
::::
::::::

<!-- Comments
-->


## Quick Announcements
- Problem Set 2 is due Monday!
- I am working on PS1 feedback for you. It has been a busy week, unfortunately. Except it by the end of tomorrow.


# Group Problems


## Problem 1: Multiple Approaches
Which of the below blocks of code would print something different from the others?

::::: cols

:::: col
:::{.block name=A}
```{.python style='margin-left:1em'}
for n in range(10):
	if n % 2 == 0:
		if n <= 10:
			print(n)
```
:::
:::{.block name=B}
```{.python style='margin-left:1em'}
for k in range(2,10):
	if not (k % 2 > 0):
		print(k)
```
:::
::::

:::: col
:::{.block name=C}
```{.python style='margin-left:1em'}
j = 0
while j < 10:
	print(j)
	j += 2

```
:::
:::{.block name=D}
```{.python style='margin-left:1em'}
for i in range(-2,10,2):
	if i > 0:
		print(i)
```
:::
::::
:::::

## Problem 2: Ranging About
::::::{.cols style='align-items: center'}
::::col
What would be the printed result of the code on the right?
::::

::::{.col style='font-size:1em; flex-grow:1.5'}
```python
biggest = 0
for i in range(2, 8, 2):
    for j in range(10, -1, -5):
        if i * j > biggest:
            biggest = i * j
print(biggest)
```
::::
::::::

## Creating your Algorithms
- Think about how you would solve the problem **without** a computer. You can't write code if you don't understand what you want the computer to do.
- Computers are fast! Brute force methods are often very viable, or at least a good starting point.
- Try to use tools and programming patterns you have already seen. It is often far easier to write programs by assembling pieces from code you have already seen than writing each program entirely from scratch.
    - Identify common patterns that we've used to solve past problems
      - Counting things
      - Various ways to loop
      - Tracking biggest/smallest things
      - Checking divisibility

## A Recommendation
- One of the most useful things you can do early on is to compile yourself a summary page of various problem-solving approaches
  - Indicate what the problem was, how you solved it, and link to or directly include some sample code
- This makes it **far** easier in future problems to identify a similar part of a problem and immediately recall (or look back) at how you have solved it previously

## Problem 3: Optimus Prime
- Write a function `is_prime` which takes one integer as input and which returns a boolean that indicates if the input number is a prime number.
- As a reminder, a number is prime if it has no factors besides 1 and itself.
- When you write out your general algorithm, also include information about where you have previously showcased each of the steps you plan to take (what problem, on what date, etc)
  - I may require this sort of information in future homework problems!

# Live-Coding

## Pythagorean Triples
A Pythagorean triplet is a set of three natural numbers, $a < b < c$, for which,
$$ a^2 + b^2 = c^2$$

There exists exactly one Pythagorean triplet where $a + b + c = 1000$. Find it.

## A Solution
```{.python style='max-height: 800px; font-size:.8em;'}
# Added once completed!
```
