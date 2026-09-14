---
title: "Home on the Range"
author: Fred Agbo & Jed
date: "September 11, 2026"
slideNumber: true
theme: "python_monokai"
highlightjs-theme: monokai
width: 1920
height: 1080
transition: fade
hash: true
history: false

---
## Happy Friday!
::::{style='font-size:.8em'}
- Class grouping today: Scan the QR code or go to [https://tools.jedrembold.prof/daily](https://tools.jedrembold.prof/daily)
- Class code is `jd7WSW`
- Introduce yourselves! Fun question: Do you think you can count faster forwards or backwards?
::::
::::::cols

::::col
![](../images/group_arrangement.png){width=60%}
::::
::::col
![](https://barcode.orcascan.com/?data=https://tools.jedrembold.prof/daily?code=lcjjHj){width=60%}
::::
::::::


## Quick Announcements
- Problem Set 2 is due on Monday Sept 14!



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
	if i >= 0:
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
# My own attempt below!

def pythagorean(a,b,c):
    """
    Identify the contraints
    1. The Ordering: a < b < c (This prevents duplicate searches, like checking both a=3, b=4 and a=4, b=3).
    2. The Equation: a^2 + b^2 = c^2 (The Pythagorean theorem).
    3. The Sum: a + b + c = 1000.
    
    Reduce the Variables (Mathematical Optimization)
    1. Since a + b + c = 1000, you can rewrite c as: c=1000-a-b
    2. In Pythagorean a^2 + b^2 = (1000 - a - b)^2
    
    Establish Strict Loop Boundaries
    1. Boundaries for a: Since a < b < c, a must be strictly less than a third of the total sum.
       
        Max a < 1000/3 => a <=332
    2. Boundaries for b: b must always start at a + 1 (because a < b). It must also be less than the remaining sum divided by 2.
        Max b < (1000 - a) / 2
    
    ALGORITHMS
    Algorithmic Logic With the math simplified, the programmatic blueprint looks like this:
    1. Initialize a loop for a ranging from 1 to 332.
    2. Initialize a nested loop for b ranging from (a + 1) to (1000 - a) / 2.
    3. Calculate c inside the loop: c = 1000 - a - b.
    4. Test the condition: Check if a^2 + b^2 == c^2.
        Return the result: If the condition is met,
        multiply a x b x c to get the final answer and break the loop immediately (since the problem states there is exactly one solution).
    
    """
    for a in range(1,333):
        for b in range(a+1, int((1000 - a)/2)):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                return a * b * c 
            
            
            
print(pythagorean(10 ,40 , 55))
```