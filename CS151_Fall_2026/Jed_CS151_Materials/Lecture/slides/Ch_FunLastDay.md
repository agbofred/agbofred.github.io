---
title: "All Good Things Come to an End"
author: Jed Rembold
date: April 29, 2026
slideNumber: true
theme: "python_catppuccin"
highlightjs-theme: catppuccin-mocha
width: 1920
height: 1080
transition: slide
hash: true
history: false

---


## OUR LAST DAY!
::::::{.cols style='font-size:.7em'}

::::col
- Scan the QR code or go to [https://tools.jedrembold.prof/daily](https://tools.jedrembold.prof/daily)
- Fun group question: At the start of the semester you shared some software you wanted to write. Do you think you could start achieving that now?

![](../images/group_seating_locs_Ford102.png){width=40%}
::::
::::{.col style='flex-grow:.5'}
![](https://barcode.orcascan.com/?text=ALd0ne&data=https://tools.jedrembold.prof/daily?code=ALd0ne){width=100%}
::::
::::::

<!-- Comments
-->


## Quick Announcements
:::{style='font-size: .8em'}
- Infinite Adventure should be submitted promptly if not yet in!
- Midterm 2 Corrections due Friday night!
  - Don't wait until the last minute to submit! These can **not** be late!
- Enigma feedback should be coming your way soon. I'll post another grade report once they are all shared
- Final is Friday afternoon of next week
    - Bring your charged laptops
    - I'll be around in the afternoons I think every day next week if you have questions
:::


## Daily LO's
- How can we connect our local Git repositories to GitHub?
- How can they "communicate" back and forth?
- Python can not "talk" to all other programs natively
  - How might we still use it to automate various tasks?

# Remote Gitting
## Dealing with Remotes
:::{style='font-size:.9em'}
- So far we have great ways to manage our local histories, but still not great ways to collaborate
- Git has a concept of _remotes_, which are basically just copies of a repository kept on a (most of the time) remote server
- Git works locally 99% of the time, so there are special commands to use when you want to "sync" contents between your _local_ repository and the _remote_ repository
- Before either can be done, we need to inform Git of where the remote for a given repository exists
  ```bash
  git remote add {name} {url}
  ```
  - `{name}` is by convention `origin` unless you are connecting multiple remotes
  - `{url}` is the address where that remote can be reached
:::

## Cloning
- Often, you might be given a remote address initially, and need to copy that repository over to your local system
- Git calls this _cloning_ a repository
  ```bash
  git clone {remote url} {directory name}
  ```
  - `{remote url}` is the url of where the remote lives
  - `{directory name}` is the local directory you want to copy that remote repository into
    - If not given, it will create a directory with the same name as the remote repository
- This automatically sets up a remote for the new local git repository

## Upload Changes to a Remote
:::{style='font-size:.9em'}
- In order for the remote to be useful, we need to let it know what we have done locally
- Git calls this _pushing_ changes to the remote
  ```bash
  git push {remote name} {local branch}:{remote branch}
  ```
- Typing all that in can get old, so we can specify it once by saying
  ```bash
  git branch --set-upstream-to={remote name}/{remote branch}
  ```
  at which point in the future we could just do
  ```bash
  git push
  ```
:::

## Getting the latest updates
:::{style='font-size:.9em'}
- On multi-computer setups, it is possible that another system uploaded content to the remote that you do not yet have locally
  - Git does not check for this sort of thing automatically! You need to be clear about checking for an update
- Git calls this _fetching_ from the remote
  ```bash
  git fetch
  ```
  - If there is more than one remote, you can specify the remote after `fetch`
- Gets the remote information, but does **not** merge it with your local content
- To do both at the same time (which is what you usually want), you can do
  ```bash
  git pull
  ```
:::

# Automate Everything!
## General Automation
- There are **many** libraries and API's you can use with Python to control or automate things
- Sometimes though, nothing exists, and you need something more primitive
- The `PyAutoGUI` library gives you methods to simulate moving and clicking the mouse and pressing keys on the keyboard
	- Will need to install through pip
- **Important!**
	- Should always have an emergency escape if you start automating the mouse and keyboard!
	- `PyAutoGUI` has a failsafe if you slam the mouse (cursor) into one of the window corners

## Common Methods

Command|Description
---|-----
`.click()` | Clicks the mouse at the current location
`.moveTo(|||x,y|||)` | Moves to the coordinate (x,y)
`.move(|||dx, dy|||)` | Moves from current position `dx` horizontally and `dy` vertically
`.drag(|||dx, dy|||)` | Clicks the mouse down and moves `dx` over and `dy` down
`.pixel(|||x,y|||)` | Gets the RGB tuple of the pixel at that location
`.write(|||text|||)` | Presses the keys represented in the string text
`.position()` | Gets the current mouse position
`.displayMousePosition()` | Constantly prints the mouse position


## PyAutoGUI Art
- Perhaps easiest to demonstrate with a simple drawing program
- Because it is just moving the mouse, should work with _any_ drawing program: Paint, Photoshop, Krita, etc.
- Initially we'd like to draw a rectangular spiral
- Then can add changing colors if time

## Rectangular Spiral
```{.python style="max-height:900px;"}
import pyautogui as pag

CHANGE = 50

pag.countdown(10)
pag.click()  # Click to make the window active.
distance = 500
while distance > 0:
	pag.drag(distance, 0, duration=0.5)  # Move right.
	distance -= CHANGE
	pag.drag(0, distance, duration=0.5)  # Move down.
	pag.drag(-distance, 0, duration=0.5)  # Move left.
	distance -= CHANGE
	pag.drag(0, -distance, duration=0.5)  # Move up.
```

## Cookies!
:::{style='font-size:.9em'}
- Web applications can be interesting to try to automate
- Idle games are a fun test, like [Cookie Clicker](https://orteil.dashnet.org/cookieclicker/)
- Step 1: Run `install.py` to get PyAutoGUI installed on your system
- Step 2: Open up Cookie Clicker in a browser, and run `cookie_clicker.py`.
  - Note the coordinates of the main cookie and the purchase options along the left of the screen
- Step 3: Implement `click_the(loc)`, to move the mouse to a given location and click
- Step 4: Implement `main`, which should loop over and click the cookie
  - Every 10 iterations, check each of the shop options and click it instead if available
:::

# Wrapping Things Up
## Class Picture!
- I always take a class picture, so please indulge me and form up for a pic!
	- Probably need a crouching or shorter row in front in order to fit in everyone!

## Evaluations
::::{style='font-size:.9em'}
- You should have gotten an email about 2 weeks ago saying that SAI's are live on Canvas
- I've left the rest of class for you to fill those out if you have not yet done so (which is most of you! Please complete them before leaving!)
- Direct comments about what you think worked well or did not work well are usually the most useful to me
    - The flipped nature of this class was a big change this semester! Please give me feedback!
	- If you also have suggestions about how the things that did not go well could be improved, then awesome! Include them!

<br><br>

:::{.block name="Thank you!"}
You all have been awesome this semester! It has been a joy to have you all in class and I hope to see you around in the future! (And maybe in another class!)
:::
::::
