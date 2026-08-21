---
title: "Clever Karel"
author: Jed Rembold
date: "January 16, 2026"
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
::::{style='font-size:.8em'}
- Scan the QR code or go to [https://classroomtools-production.up.railway.app/daily?code=eTRF9](https://classroomtools-production.up.railway.app/daily?code=eTRF9)
- Class code is `eTRF9`
::::
::::::cols

::::col
![](../images/group_seating_locs_Ford102.png){width=70%}
::::
::::col
![](https://barcode.orcascan.com/?data=https://classroomtools-production.up.railway.app/daily?code=eTRF9){width=70%}
::::
::::::
<!-- Comments
- Problem 1: I think this worked and was approachable for most students. I like the alternative "shift" idea as well, which could maybe be more formalized?
- Problem 2: This seemed to work nicely. Can be done without the for loops though, if that is of concern?
- Problem 3: Nested loops, as always, are hard for students. But this is a useful example to have them work on and then go through myself.
- Live Code: This narrow path problem is interesting, and I didn't leave myself nearly enough time for it unfortunately.
-->



## Quick Announcements
- Ensure you have the tech installed on your system!
	- Then swing by my office during office hours (or when my door is open) to check in with me before the end of next Tuesday
- Sections start next week. If you have not yet filled out your availability, please do that **now** [here](https://docs.google.com/forms/d/e/1FAIpQLSfBzB0F2-loUUf63MU5DglpW2_oMuksVZ0vJkEZ9dUnVvbexA/viewform?usp=dialog)! I'm still missing about 10 of you.
- Discord channel is live! Invite code in Canvas announcement.
- Problem Set 1 is live! Not due until a week from Monday


# Group Problems

## Preliminaries
- Take a quick moment to introduce yourself to your group-mates for the day
	- Name
	- Class year
	- Major?
- Fun question of the day: if you were to add one fun command to Karel, what would it do (and be named)?

## Considerations
- Don't forget about decomposition!
- For all code writing questions today, try to think about how you could decompose it into at least two parts
	- Frequently, you'll be able to reuse one of those parts!
- You can find a repository of worlds for today's problems [here](https://github.com/rembold-cs151-master/Lec3Content)
	- Not required, but there if you want to be able to test solutions

## Problem 1: Flippy Floppy
- Suppose we had the situation similar to the world below, and you want to exchange where beepers are
	- Replace empty space with a beeper, and a beeper with empty space
- The world is always the same size, Karel has infinite beepers, and always starts facing East
- Initial beepers could be anywhere though!

\begin{tikzpicture}%%width=90%
\karelgrid[Green]{6}{1}
\karelbeeper[Blue]{3}{1}
\karelbeeper[Blue]{5}{1}
\karelbeeper[Blue]{6}{1}
\karelmark[Yellow]{1}{1}{0}

\begin{scope}[xshift=8cm]
\karelgrid[Green]{6}{1}
\karelbeeper[Blue]{1}{1}
\karelbeeper[Blue]{2}{1}
\karelbeeper[Blue]{4}{1}
\karelmark[Yellow]{6}{1}{0}
\end{scope}

\end{tikzpicture}

:::notes
An interesting variant of this would be to shift all the beepers to the right or left, wrapping around!
:::


## Problem 2: The Race
::::::cols
::::col
- Karel starts at the bottom of a world facing north
- There are exactly _two_ stacks of beepers placed somewhere above them
- To win the race Karel needs to pick up both stacks of beepers and then touch the North wall
	- Remember that Karel can only pick up one beeper at a time!
::::

::::col
\begin{tikzpicture}%%width=60%
\karelgrid[Green]{1}{6}
\karelbeeper[Blue]{1}{2}
\node at (1,2) {4};
\karelbeeper[Blue]{1}{4}
\node at (1,4) {3};
\karelmark[Yellow]{1}{1}{90}

\begin{scope}[xshift=3cm]
\karelgrid[Green]{1}{6}
\karelmark[Yellow]{1}{6}{90}
\end{scope}
\end{tikzpicture}

::::
::::::







## Problem 3: Nested Beeper Drops
::::::cols
::::{.col style='flex-grow:1.5'}
Karel starts as shown to the right with 20 beepers in its bag. After executing the commands below, how many beepers are left in the bag upon the conclusion of the program?

```python
while left_is_clear():
	while front_is_clear():
		move()
		if no_beepers_present():
			put_beeper()
	turn_left()
```
::::

::::col
\begin{tikzpicture}%%width=90%
\karelgrid[Green]{5}{5}
\karelmark[fill=Yellow]{1}{1}{0}
\draw[very thick, Green] (.5,2.5) --++(1,0) --++(0,-1)--++(2,0)--++(0,1)--++(1,0)
						  (2.5,3.5) --++(0,-1)
						  (5.5,3.5) --++(-1,0) --++(0,1) --++(1,0)
						  (0.5,4.5) --++(2,0) --++(0,1)
						  (3.5,4.5) --++(0,1);
\karelbeeper[fill=Blue]{3}{1}
\karelbeeper[fill=Blue]{3}{4}
\karelbeeper[fill=Blue]{1}{3}
\karelbeeper[fill=Blue]{5}{3}
\node at (1,1) {20};
\end{tikzpicture}
::::
:::::

# Live-Coding

<!--
## Option 1: More Bars in More Places
- A line of stacks of beepers goes across the bottom of Karel's world
- Karel's job is to spread each stack out on the corresponding avenue, with 1 beeper on each street, starting from 1st street
- You don't know how big the world is, or how many beepers might be in each stack
	- But there will be fewer beepers than the height of the world
- Karel always starts from the lower right facing west

## Visualized

\begin{tikzpicture}%%width=90%
\karelgrid[Green]{5}{5}
\karelbeeper[Blue]{1}{1}
\node at (1,1) {2};
\karelbeeper[Blue]{2}{1}
\node at (2,1) {4};
\karelbeeper[Blue]{3}{1}
\node at (3,1) {5};
\karelbeeper[Blue]{4}{1}
\karelbeeper[Blue]{5}{1}
\node at (5,1) {3};
\karelmark[Yellow]{5}{1}{180}

\begin{scope}[xshift=7cm]
\karelgrid[Green]{5}{5}
\foreach \y in {1,2} \karelbeeper[Blue]{1}{\y};
\foreach \y in {1,2,3,4} \karelbeeper[Blue]{2}{\y};
\foreach \y in {1,2,3,4,5} \karelbeeper[Blue]{3}{\y};
\karelbeeper[Blue]{4}{1}
\foreach \y in {1,2,3} \karelbeeper[Blue]{5}{\y};
\karelmark[Yellow]{1}{1}{180}
\end{scope}
\end{tikzpicture}
-->

## A Narrow Path
::::::cols
::::col
- There is a beeper path that extends from one side of the world to the other
- Karel starts on one end, facing toward the first beeper
- Goal is to follow the path to the other end
::::

::::col
\begin{tikzpicture}%%width=90%
\karelgrid[Green]{10}{10}
\foreach \x/\y in {1/2,2/2,3/2,3/3,4/3,4/4,4/5,4/6,5/6,6/6,7/6,8/6,8/5,8/4,9/4,10/4} \karelbeeper[Blue]{\x}{\y};
\karelmark[Yellow]{1}{2}{0}
\end{tikzpicture}

::::
::::::



## A Solution
```{.python style='max-height: 800px'}
import karel

def main():
    """Follows a path of beepers as best as possible from one end of the
    world to the other end.
    """
    while front_is_clear():
        follow_straight_beeper_path()
        determine_next_direction()

def follow_straight_beeper_path():
    """Follows a beeper path until no beeper
    is found, then doubles back to last beeper
    space"""
    while beepers_present():
        if front_is_clear():
            move()
    if front_is_clear():
        turn_around()
        move()

def determine_next_direction():
    """Determines the direction of the next path of beepers. Tries one direction
    and if it finds no beeper there it knows it must be the other direction.
    Leaves Karel facing the next path of beepers.
    """
    turn_left()
    if front_is_clear():
        move()
        if beepers_present(): # This side! I'm reseting here but probably don't need to
            turn_around()
            move()
            turn_around()
        else: # No beepers, so must be the other direction
            turn_around()
            move()
    

def turn_around():
    """Turns Karel 180"""
    turn_left()
    turn_left()
```

