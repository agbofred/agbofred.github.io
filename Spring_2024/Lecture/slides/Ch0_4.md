---
title: "Stepwise Refinement"
author: Jed Rembold & Fred Agbo
date: January 26, 2024
slideNumber: true
theme: "python_monokai"
highlightjs-theme: monokai
width: 1920
height: 1200
transition: slide
hash: true
history: false
---


## Announcements
- Remember, problem Set 1 is due on __Monday Jan. 29th @ 10pm__!
- Small sections started this week. Keep attending
	- Remember! The channel for getting help is ***Section leaders***,  __QUAD__, Instructors 
    - Did you not get a message from _Prof. Jed_ about your section meeting time? 
	    - Come see me after class and we can see about getting you placed into one.
- Polling: [https://www.polleverywhere.com/agbofred203](https://www.polleverywhere.com/agbofred203)
	- Reminder: include enough of your name that I can uniquely identify you!

## Review Question
::::::cols
::::{.col style='flex-grow:1.5'}
Karel starts as shown to the right. At which beeper do they end up when the below sequence of commands finishes?

```python
while no_beepers_present():
	while front_is_clear():
		move()
		if beepers_present():
			turn_left()
        else:
            turn_right()
	turn_left()
```
::::

::::col
\begin{tikzpicture}%%width=90%
\karelgrid[MGreen]{5}{5}
\karelmark[fill=MYellow]{2}{3}{-90}
\draw[very thick, MGreen] (.5,2.5) --++(1,0) --++(0,-1)--++(2,0)--++(0,1)--++(1,0)
						  (2.5,3.5) --++(0,-1)
						  (5.5,3.5) --++(-1,0) --++(0,1) --++(1,0)
						  (0.5,4.5) --++(2,0) --++(0,1)
						  (3.5,4.5) --++(0,1);
\karelbeeper[fill=MBlue]{3}{1}
\karelbeeper[fill=MBlue]{3}{4}
\karelbeeper[fill=MBlue]{1}{3}
\karelbeeper[fill=MBlue]{5}{3}

\node[font=\large\bf] at (1,3) {A};
\node[font=\large\bf] at (3,4) {B};
\node[font=\large\bf] at (5,3) {C};
\node[font=\large\bf] at (3,1) {D};
\end{tikzpicture}


::::
::::::

<!--
## Counting Loops
- Sometimes we **know** the number of times we want to loop
	- It is not dependent on some condition like a while loop
- In these circumstances, the iterative statement called a _for_ loop is best used
- Syntax looks like:

	```python
	for i in range(desired_count):
		# statements to be repeated
	```
   - `desired_count` is an _integer_ indicating the number of times you want the loop to repeat
   - The `i` is a name that we will later make more general, but for now you can always leave it as an `i`


## An Example `for` you 
::::::cols
::::col
- Suppose Karel starts in the bottom left corner of a "room"
- We want Karel to create a 6x6 square outline of beepers in the center of the room
- Need to repeat making each side 4 times
- Need to repeat placing a beeper and moving 6 times for each side
	- Placing 6 beepers requires moving only 5 times. So not everything can be in the loop
::::
::::col
\begin{tikzpicture}%%width=100%
\karelgrid[MGreen]{10}{10}
\foreach \x in {3,4,5,6,7,8}{
	\karelbeeper[MBlue]{\x}{3};
	\karelbeeper[MBlue]{\x}{8};
	\karelbeeper[MBlue]{3}{\x};
	\karelbeeper[MBlue]{8}{\x};
}
\karelmark[MYellow]{3}{3}{0}
\end{tikzpicture}
::::
::::::

## A Potential Solution
```{.python style="max-height: 900px"}
import karel

def main():
    """Draw a 4x4 square in the world."""
    position()
    draw_box()

def position():
    """Move to starting corner of box."""
    move()
    move()
    turn_left()
    move()
    move()
    turn_right()

def turn_right():
    """Turns Karel 90 deg to the right."""
    turn_left()
    turn_left()
    turn_left()

def draw_box():
    """Draws a box with 4 equal sides in a CCW direction."""
    for i in range(4):
        draw_6_line()
        turn_left()

def draw_6_line():
    """Draws a straight line of 6 beepers, if space."""
    for i in range(5):
        if no_beepers_present():
            put_beeper()
        if front_is_clear():
            move()
    if no_beepers_present(): # Last beeper to make 6
        put_beeper()
```

-->

## Summary So Far
::::::{.cols style='font-size:.95em'}
::::col
:::{.block name="Karel Cmds"}
- Karel can only:
	- `move()`
	- `turn_left()`
	- `pick_beeper()`
	- `put_beeper()`
- Get info about surroundings using predicate functions
	- Eg. `front_is_clear()`
	- Inverse options exist as well
:::

:::{.block name="Functions"}
- Group code into reusable bundles
```python
def function_name():
	# Code to be grouped
```
:::
::::

::::{.col style='flex-grow:1.5'}
:::{.block name="Control Statements"}
- Conditional statements
	- Run certain code blocks only if a condition is true (the `else` block is optional)
	```python
	if condition_test:
		# Code if answer yes
	else:
		# Code if answer no
	```
- Iterative statements
	- Repeat code block as long as condition is true
	```python
	while condition_test:
		# Code to repeat
	```
	- Repeat set number of times
	```python
	for i in range(desired_count):
		# Code to repeat
	```
:::
::::
::::::

## Stepwise Refinement {.data-auto-animate}
::::::cols
::::col
- The most successful way to solve a complex problem is to break it down into progressively simpler problems
- Begin by breaking the whole problem into a few simpler parts
    - Some of these parts might then need further breaking down into even simpler parts
- The process is commonly called _stepwise refinement_ or _decomposition_
::::

::::col
\begin{tikzpicture}[box/.style={MGreen, draw, very thick, rounded corners, font=\Large\tt}]%%width=100%
\node[box] (prob) at (0,0) {Problem};
\node[box, MBlue] (sub1) at (-3,-3) {Subprob 1};
\node[box, MBlue] (sub2) at (0,-3) {Subprob 2};
\node[box, MBlue] (sub3) at (3,-3) {Subprob 3};
\draw[MGreen, very thick, -latex] (prob.south) -- (sub1.north);
\draw[MGreen, very thick, -latex] (prob.south) -- (sub2.north);
\draw[MGreen, very thick, -latex] (prob.south) -- (sub3.north);
\node[box, MRed] (ssub1) at (-2,-6) {Subprob 2a};
\node[box, MRed] (ssub2) at (2,-6) {Subprob 2b};
\draw[MGreen, very thick, -latex] (sub2.south) -- (ssub1.north);
\draw[MGreen, very thick, -latex] (sub2.south) -- (ssub2.north);

\end{tikzpicture}


::::
::::::

## Excellent Decomposing
- A good problem decomposition should mean:

  The proposed pieces should be easy to explain
    : One indication that you have succeeded is if it is easy to give them simple names

  The steps are as general as possible
    : Each piece of code you can reuse is one less piece of code you need to write! If your steps solve general tasks, they are much easier to reuse.

  The steps should make logical sense for the problem you are solving
    : If you have a function that will work to solve a step but was designed (and named) with something else entirely in mind, adopt it for the currently needed situation

## Enter the Winter
- Suppose we want Karel to usher in the Fall/Winter by removing the "leaves" from the tops of all the trees

\begin{tikzpicture}%%width=90%
\karelgrid[MGreen]{13}{6}
\karelmark[MYellow]{1}{1}{0}
\draw[MGreen, very thick] (2.5,0.5) --+ (0,2) (4.5,0.5) --+(0,4) (8.5,0.5) --+(0,2) (11.5,0.5) -- +(0,3);

\newcommand{\treetop}[2]{
    \foreach \x in {0,1} {
        \foreach \y in {0,1} {
            \karelbeeper[MBlue]{#1+\x}{#2+\y}
        }
    }
}
\treetop{2}{3}
\treetop{4}{5}
\treetop{8}{3}
\treetop{11}{4}
\end{tikzpicture}


## Understanding the Problem
- What are we guaranteed by the problem?
- How will we know when we are done?

\begin{tikzpicture}%%width=80%
\karelgrid[MGreen]{13}{6}
\karelmark[MYellow]{1}{1}{0}
\draw[MGreen, very thick] (2.5,0.5) --+ (0,2) (4.5,0.5) --+(0,4) (8.5,0.5) --+(0,2) (11.5,0.5) -- +(0,3);
\newcommand{\treetop}[2]{
    \foreach \x in {0,1} {
        \foreach \y in {0,1} {
            \karelbeeper[MBlue]{#1+\x}{#2+\y}
        }
    }
}

\treetop{2}{3}
\treetop{4}{5}
\treetop{8}{3}
\treetop{11}{4}
\end{tikzpicture}

## Understanding the Problem
- There are four trees in this problem
- We need to find a tree at a time
- We need to remove the leaves 
    - there are four leaves per tree

\begin{tikzpicture}%%width=80%
\karelgrid[MGreen]{13}{6}
\karelmark[MYellow]{1}{1}{0}
\draw[MGreen, very thick] (2.5,0.5) --+ (0,2) (4.5,0.5) --+(0,4) (8.5,0.5) --+(0,2) (11.5,0.5) -- +(0,3);
\newcommand{\treetop}[2]{
    \foreach \x in {0,1} {
        \foreach \y in {0,1} {
            \karelbeeper[MBlue]{#1+\x}{#2+\y}
        }
    }
}

\treetop{2}{3}
\treetop{4}{5}
\treetop{8}{3}
\treetop{11}{4}
\end{tikzpicture}


## Top-Level Decomposition {data-auto-animate=True}
- We could break this problem into two main subproblems:
  #. Find the next tree
  #. Strip the leaves off that tree

\begin{tikzpicture}%%width=80%
\karelgrid[MGreen]{13}{6}
\karelmark[MYellow]{1}{1}{0}
\draw[MGreen, very thick] (2.5,0.5) --+ (0,2) (4.5,0.5) --+(0,4) (8.5,0.5) --+(0,2) (11.5,0.5) -- +(0,3);
\newcommand{\treetop}[2]{
    \foreach \x in {0,1} {
        \foreach \y in {0,1} {
            \karelbeeper[MBlue]{#1+\x}{#2+\y}
        }
    }
}

\treetop{2}{3}
\treetop{4}{5}
\treetop{8}{3}
\treetop{11}{4}
\end{tikzpicture}

## Top-Level Decomposition {data-auto-animate=True}
- We could break this problem into two main subproblems:
  #. **Find the next tree**
  #. Strip the leaves off that tree

\begin{tikzpicture}%%width=80%
\karelgrid[MGreen]{13}{6}
\karelmark[MYellow]{2}{1}{0}
\draw[MGreen, very thick] (2.5,0.5) --+ (0,2) (4.5,0.5) --+(0,4) (8.5,0.5) --+(0,2) (11.5,0.5) -- +(0,3);
\newcommand{\treetop}[2]{
    \foreach \x in {0,1} {
        \foreach \y in {0,1} {
            \karelbeeper[MBlue]{#1+\x}{#2+\y}
        }
    }
}

\treetop{2}{3}
\treetop{4}{5}
\treetop{8}{3}
\treetop{11}{4}
\end{tikzpicture}

## Top-Level Decomposition {data-auto-animate=True}
- We could break this problem into two main subproblems:
  #. Find the next tree
  #. **Strip the leaves off that tree**

\begin{tikzpicture}%%width=80%
\karelgrid[MGreen]{13}{6}
\karelmark[MYellow]{3}{1}{0}
\draw[MGreen, very thick] (2.5,0.5) --+ (0,2) (4.5,0.5) --+(0,4) (8.5,0.5) --+(0,2) (11.5,0.5) -- +(0,3);
\newcommand{\treetop}[2]{
    \foreach \x in {0,1} {
        \foreach \y in {0,1} {
            \karelbeeper[MBlue]{#1+\x}{#2+\y}
        }
    }
}

\treetop{4}{5}
\treetop{8}{3}
\treetop{11}{4}
\end{tikzpicture}

## Top-Level Decomposition {data-auto-animate=True}
- We could break this problem into two main subproblems:
  #. **Find the next tree**
  #. Strip the leaves off that tree

\begin{tikzpicture}%%width=80%
\karelgrid[MGreen]{13}{6}
\karelmark[MYellow]{4}{1}{0}
\draw[MGreen, very thick] (2.5,0.5) --+ (0,2) (4.5,0.5) --+(0,4) (8.5,0.5) --+(0,2) (11.5,0.5) -- +(0,3);
\newcommand{\treetop}[2]{
    \foreach \x in {0,1} {
        \foreach \y in {0,1} {
            \karelbeeper[MBlue]{#1+\x}{#2+\y}
        }
    }
}

\treetop{4}{5}
\treetop{8}{3}
\treetop{11}{4}
\end{tikzpicture}

## Top-Level Decomposition {data-auto-animate=True}
- We could break this problem into two main subproblems:
  #. Find the next tree
  #. **Strip the leaves off that tree**

\begin{tikzpicture}%%width=80%
\karelgrid[MGreen]{13}{6}
\karelmark[MYellow]{5}{1}{0}
\draw[MGreen, very thick] (2.5,0.5) --+ (0,2) (4.5,0.5) --+(0,4) (8.5,0.5) --+(0,2) (11.5,0.5) -- +(0,3);
\newcommand{\treetop}[2]{
    \foreach \x in {0,1} {
        \foreach \y in {0,1} {
            \karelbeeper[MBlue]{#1+\x}{#2+\y}
        }
    }
}

\treetop{8}{3}
\treetop{11}{4}
\end{tikzpicture}

## Top-Level Decomposition {data-auto-animate=True}
- We could break this problem into two main subproblems:
  #. **Find the next tree**
  #. Strip the leaves off that tree

\begin{tikzpicture}%%width=80%
\karelgrid[MGreen]{13}{6}
\karelmark[MYellow]{8}{1}{0}
\draw[MGreen, very thick] (2.5,0.5) --+ (0,2) (4.5,0.5) --+(0,4) (8.5,0.5) --+(0,2) (11.5,0.5) -- +(0,3);
\newcommand{\treetop}[2]{
    \foreach \x in {0,1} {
        \foreach \y in {0,1} {
            \karelbeeper[MBlue]{#1+\x}{#2+\y}
        }
    }
}

\treetop{8}{3}
\treetop{11}{4}
\end{tikzpicture}

## Top-Level Decomposition {data-auto-animate=True}
- We could break this problem into two main subproblems:
  #. Find the next tree
  #. **Strip the leaves off that tree**

\begin{tikzpicture}%%width=80%
\karelgrid[MGreen]{13}{6}
\karelmark[MYellow]{9}{1}{0}
\draw[MGreen, very thick] (2.5,0.5) --+ (0,2) (4.5,0.5) --+(0,4) (8.5,0.5) --+(0,2) (11.5,0.5) -- +(0,3);
\newcommand{\treetop}[2]{
    \foreach \x in {0,1} {
        \foreach \y in {0,1} {
            \karelbeeper[MBlue]{#1+\x}{#2+\y}
        }
    }
}

\treetop{11}{4}
\end{tikzpicture}

## Top-Level Decomposition {data-auto-animate=True}
- We could break this problem into two main subproblems:
  #. **Find the next tree**
  #. Strip the leaves off that tree

\begin{tikzpicture}%%width=80%
\karelgrid[MGreen]{13}{6}
\karelmark[MYellow]{11}{1}{0}
\draw[MGreen, very thick] (2.5,0.5) --+ (0,2) (4.5,0.5) --+(0,4) (8.5,0.5) --+(0,2) (11.5,0.5) -- +(0,3);
\newcommand{\treetop}[2]{
    \foreach \x in {0,1} {
        \foreach \y in {0,1} {
            \karelbeeper[MBlue]{#1+\x}{#2+\y}
        }
    }
}

\treetop{11}{4}
\end{tikzpicture}

## Top-Level Decomposition {data-auto-animate=True}
- We could break this problem into two main subproblems:
  #. Find the next tree
  #. **Strip the leaves off that tree**

\begin{tikzpicture}%%width=80%
\karelgrid[MGreen]{13}{6}
\karelmark[MYellow]{12}{1}{0}
\draw[MGreen, very thick] (2.5,0.5) --+ (0,2) (4.5,0.5) --+(0,4) (8.5,0.5) --+(0,2) (11.5,0.5) -- +(0,3);

\end{tikzpicture}

## Remember Your Algorithms!
- _Algorithmic design_: The process of designing a solution strategy to a problem 
- An _algorithm_ is just an approach or recipe for a method to solve a particular problem
	- Frequently language agnostic
- Can you design algorithm to address the Fall/Winter problem?

## Algorithm ⮕ Code
::::::{.cols style='font-size:.95em'}
::::col
:::{.block name="General Algorithm"}
- for four iterations
    - find a tree
    - then remove leaves
:::

:::{.block name="Algorithm to find a tree"}
- while the front is clear
    - keep moving

:::
::::

::::{.col style='flex-grow:1.5'}
:::{.block name="Algorithm to remove leaves"}
- move up the tree
- remove each leaf
- move down the tree
	
:::
::::
::::::

## Algorithm ⮕ Code
::::::{.cols style='font-size:.95em'}
::::col
:::{.block name="Main Program"}
```python
import karel
def main():
    # Here is our general solution with higher level of decomposition
    for i in range(3):
        find_next_tree()
        remove_leaves()
```
:::

:::{.block name="Find next tree"}
```python
def find_next_tree():
    # the codes to find next tree
    while front_is_clear():
        move()
```
:::
::::

::::{.col style='flex-grow:1.5'}
:::{.block name="Remove leaves"}
```python
def remove_leaves():# codes to remove leaves
    move_up()
    deleaf()
    move_down()
```
- moving up
```python
def move_up():
    turn_left()
    while right_is_blocked():
        move()
```
- deleafing
```python
def deleaf():
    pick_beeper()
    for i in range(3):
        move()
        pick_beeper()
        turn_right()
    turn_left()
```
- moving down
```python
def move_down():
    while front_is_clear():
        move()
    turn_left()
```
:::
::::
::::::


## Data Types
- Generally, the data processed by computers can take on many forms
- A _data type_ defines the common characteristics of some data values that have a certain form or purpose.
	- Ex: a whole number or integer has certain characteristics common to all integers
- A data type has a _domain_, which is the set of all potential values that would belong to that type.
	- Ex: 0,1,2,3,4,5,6,7,...
- A data type has a _set of operations_ that define how those values can be manipulated
	- Ex: You can add two whole numbers (5+2)

## Numeric Types
- Initially, we'll focus on the numeric types
- Python has 3 data types for representing numbers:
	- `int`{.python} for integers and whole numbers

		```python
		1, 2, 3, 10, 1001010101, -231
		```

	- `float`{.python} for numbers containing a decimal point

		```python
		1.23, 3.14, 10.001, 0.0, -8.23
		```

	- `complex`{.python} for numbers with an imaginary component (which we won't deal with)

---

## Expressions
- Python describes computation using _arithmetic expressions_, which consist of _terms_ joined by _operators_
	- Very similar to how a logical English sentence has nouns connected by verbs
- A term in an expression can be:
	- an explicit numeric value (called a literal) like 1 or 3.14
	- a variable name serving as a placeholder to a value (more on those in a moment!)
	- a value resulting from the output of a function call (more on those on Monday!)
	- another expression enclosed in parentheses

<br>

![](../images/expressions.svg)
