---
title: "Arrays and Lists"
author: Fred Agbo
date: "October 14, 2026"
slideNumber: true
theme: "python_monokai"
highlightjs-theme: monokai
width: 1920
height: 1080
transition: fade
hash: true
history: false

---

## Happy Wednesday 

::::{style='font-size:.8em'}
- Class grouping today: Scan the QR code or go to [https://tools.jedrembold.prof/daily](https://tools.jedrembold.prof/daily)
- Class code is `HUsTv1`
- Introduce yourselves! What is experience with matrix?
::::

::::::cols

::::col
![](../images/group_arrangement.png){width=60%}
::::
::::col
![](https://barcode.orcascan.com/?data=https://tools.jedrembold.prof/daily?code=lcjjHj){width=60%}
::::
::::::

---

## Quick Announcements
- Midterm exam 1 review/solution is posted on Canvas
- Project Breakout is due next week Monday
- Starting early is a key factor to success
- Attend your session meeting for more help and tools needed to succeed on the Breakout project.

---

## Midterm Polling
:::{.incremental style="font-size: 35px;"}
- __If there's a single most important thing to do to help you improve in content understanding and grades in this class what would that be?__

    - Being allowed to work on a project over an extended period 
        - Unfortunately, this is how the curriculum has been built for years!
            - Intensive!

    - Take time in class to go over the homework before it's due.
        - I strongly recommend to start working on homework from Tuesdays
        - Visiting office hours and QUAD Center, and ask Section leaders
    - Videos and its grade points; Spend some class time talking about the video concepts
        - Please consistently watch the videos. The points are huge overtime.
        - I have and will continue to reinforce the topic in the video before jumping to the activities.    
    - Further explaining what certain lines of code do.
        - Raise your hand to ask me questions or to repeat my explanation.
    - I wasn't as understanding of the material as I could be ...
        - Read the text material shared with you chapter by chapter. 
        - This is a useful supplementary material upon which ALL the lecture contents in the class was built.
:::


--- 

## Arrays and Lists
- From the earliest days, programming languages have supported the idea of an _array_, or an ordered sequence of values.
- Individual values in an array are called _elements_, and the number of elements is the _length_ of the array.
- Each element's position in the array is given by its _index_, with index numbers starting at 0 and extending up to 1 less than the length of the array
- Python implements the array concept in a bit more general form called a _list_.

---

## Reminder: Making Lists
- Created using square brackets with elements separated by commas:
  ```python
  COIN_VALUES = [1, 5, 10, 25, 50, 100]
  COIN_NAMES = [ "penny", "nickle", "dime",
                 "quarter", "half-dollar", "dollar" ]
  ```
- Lists are commonly represented visually or conceptually as a series of numbered boxes:
\begin{tikzpicture}%%width=80%
[box/.style={draw, thick, MBlue, minimum width=2cm, minimum height=1cm, font=\tt, text width=2cm, align=center}]
\node[box, label={[MPurple,font=\footnotesize]below:0}](0) at (0,0) {1};
\node[box, label={[MPurple,font=\footnotesize]below:1}, right=0cm of 0](1) {5};
\node[box, label={[MPurple,font=\footnotesize]below:2}, right=0cm of 1](2) {10};
\node[box, label={[MPurple,font=\footnotesize]below:3}, right=0cm of 2](3) {25};
\node[box, label={[MPurple,font=\footnotesize]below:4}, right=0cm of 3](4) {50};
\node[box, label={[MPurple,font=\footnotesize]below:5}, right=0cm of 4](5) {100};
\node[anchor=south west, font=\tt\footnotesize, color=MGreen] at (0.north west) {COIN\_VALUES};
\node[box, label={[MPurple,font=\footnotesize]below:0}](0) at (0,-2) {"penny"};
\node[box, label={[MPurple,font=\footnotesize]below:1}, right=0cm of 0](1) {"nickel"};
\node[box, label={[MPurple,font=\footnotesize]below:2}, right=0cm of 1](2) {"dime"};
\node[box, label={[MPurple,font=\footnotesize]below:3}, right=0cm of 2](3) {"quarter"};
\node[box, label={[MPurple,font=\footnotesize]below:4}, right=0cm of 3](4) {"half-\\dollar"};
\node[box, label={[MPurple,font=\footnotesize]below:5}, right=0cm of 4](5) {"dollar"};
\node[anchor=south west, font=\tt\footnotesize, color=MGreen] at (0.north west) {COIN\_NAMES};
\end{tikzpicture}

---

## What we already know
- Can retrieve the value of any element in a list by writing the index of that element in square brackets after the list name
	- `COIN_VALUES[3]` ⟶ `25`
	- `COIN_NAMES[2]` ⟶ `"dime"`
- Can concatenate two lists to form a new list with elements from both
    - `[1,2,3] + [4,5,6]`⟶  `[1,2,3,4,5,6]`

- Can loop through each of the list elements in turn
  ```python
  for elem in my_list:
  	# do stuff with elem
  ```
  where `elem` is the name of the variable that will sequentially get assigned the value of every element in `my_list`

---

## Sequences 
:::{.small style="font-size: 30"}
- Sound familiar? Lists are just like more general strings!
- Strings and lists are examples of a more general class of object in Python called _sequences_

::::::cols
::::col
:::{.block name=Old}
- We already knew that all sequences support:
  - The `len` function
  - Index numbering starting at 0
  - Concatenation using `+` or `+=`
  - Selection of an individual element using square brackets
  - Looping over elements
:::
::::

::::col
:::{.block name=New .fragment}
- We can now add:
  - Negative index numbering counting backwards from the end 
  - Slicing in all forms
  - Comparing sequences
  - Repetition using `*`
  - Inclusion testing using `in` operator
:::
::::
::::::
:::

---

## Problem 1A: Tracing Understanding  {data-notes="Solution: None of the above, as it errors"}
What would the below expression evaluate to?

```{.python .inlinecode}
["One", 2, True][-1:1:-1][1]
```

:::{.poll}
#. `"n"`
#. `2`
#. `True`
#. None of the above, or this will error
:::

---

## Problem 1B: Tracing Understanding 
What would the below expression evaluate to? Or would it error out?
```{.python .inlinecode}
['One', 2, True][-1:1:-1][0]
```

---

## Problem 2: Airline Boarding
- This is a coding problem, work in pairs or trios on a single computer
- In `manifest.py`, I've created a list of passenger information for an airline
- The list has passenger information in a "name", "age", "seat" ordering
- So, for example, the first few passengers look like:
  ```python
  MANIFEST = [
    "Anthony Hutchinson", 77, "24A",
    "Carol Turner", 37, "8F",
    ...etc...
  ]
  ```

---

## Problem 2b: Seat Taken?
- In `Prob2.py`, you can add your code
- Imagine a passenger would like to switch seats. It would be nice to have an easy function to check a potential seat assignment and determine if it is available
- Complete the function `is_seat_available` to check to see if a particular seat is available (not currently assigned)
- BONUS: Sometimes robots will ride the plane with names like '2F'. Make sure your function still would work properly in that case

---

## Problem 2c: New Family
- Switch who is typing!
- A new family purchased tickets late! Add their information to the manifest.
    - Bill Yu, age 43, in seat 15C
    - Jackie Yu, age 39, in seat 15B
    - Hayden Yu, age 12, in seat 15A
- Then, complete the function `avg_age_window_seats`, which returns the average age of all passengers riding in a window seat ("A" and "F" seats)

