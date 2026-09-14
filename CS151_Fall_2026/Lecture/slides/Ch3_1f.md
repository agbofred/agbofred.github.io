---
title: "Home on the Range"
author: Fred Agbo & Jed
date: "September 14, 2026"
slideNumber: true
theme: "python_monokai"
highlightjs-theme: monokai
width: 1920
height: 1080
transition: fade
hash: true
history: false

---

## Happy New Week!
::::{style='font-size:.8em'}
- Class grouping today: Scan the QR code or go to [https://tools.jedrembold.prof/daily](https://tools.jedrembold.prof/daily)
- Class code is `hVSGho`
- Introduce yourselves! What is your favorite bug?
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
- My apologies, I'm yet to complete the grading of Problem set 1. Should be cone by the end of the week.
- Welcome to SCIS Open House: Computer Science, Data Science, Industrial Eng, and Statistics
    - WHEN: __Sep 15, 2026 Tuesday 11:30 AM – 1:00 PM__
    - WHERE: __Salem Campus - Ford Hall 102__
        - [See this link for more info](https://events.willamette.edu/e/8070)

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
    2. Boundaries for b: b must always start at a + 1 (since a < b). 
        It must also be less than the remaining sum divided by 2.
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
    # Now Write the program 

```


# Group Problems

## Prep
- All problems today revolve around troubleshooting and finding errors in some "launch code"-esque checks
- You will want at least someone or all of you to have downloaded all the lecture contents linked in ```Discord```
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

<!-- # Live-Coding

## Writing Tests
- Let's write a suite a tests for each of the library functions
- Always a good idea to target `assert` statements at both typical values, but also edge cases
- Let's try to come up with at least 3-4 for each function


## A Solution
```{.python style='max-height: 800px; font-size:.8em;'}
# Added once completed!
``` -->
