---
title: "Readin and Riting"
author: Jed Rembold
date: "March 11, 2026"
slideNumber: true
theme: python_catppuccin
highlightjs-theme: catppuccin-mocha
width: 1920
height: 1080
transition: slide
hash: true
history: false
---
## You've made it halfway!
::::::{.cols style='font-size:.8em'}

::::col
- Scan the QR code or go to [https://tools.jedrembold.prof/daily](https://tools.jedrembold.prof/daily)
- Fun group question: What is your favorite book?

![](../images/group_seating_locs_Ford102.png){width=50%}
::::
::::col
![](https://barcode.orcascan.com/?text=RTCtUf&data=https://tools.jedrembold.prof/daily?code=RTCtUf){width=60%}
::::
::::::

<!-- Comments
-->


## Quick Announcements
:::{style='font-size: .8em'}
- Problem Set 5 is live!
  - You've got everything you need to complete it already
- Office hours from 2-2:45 today
- Don't forget to attend your section today or tomorrow!
:::

## Daily LO's
- Understanding how to open a file
- Reading contents from a file
- Writing text back to a file

# Group Problems

## Problem 1: Inconceivable Code
::::::cols
::::col
To the right are the contents of a text file named `PBride.txt`. Which code snippet below would print off the word "father"?
::::

::::col
```{.text}
My name is Inigo Montoya.
You killed my father.
Prepare to die.
```

::::
::::::

::::::cols
::::col

:::{.block name=A}
```python
with open('PBride.txt') as f:
	for line in f:
		w = line.split()
		if w[0] == "You":
			print(w[-1])
```
:::

:::{.block name=B}
```python
c = read('PBride.txt')
print(c.find("father"))
```
:::


::::

::::col

:::{.block name=C}
```python
with open('PBride.txt') as f:
	c = f.read().splitlines()
	print(c[1][4])
```
:::

:::{.block name=D}
```python
with open('PBride.txt') as f:
	c = f.read()
	i = c.find("f")
	print(c[i:i+6])
```
:::

::::
::::::


## Problem 2a: The Great White Whale
- This is a coding problem. Work in pairs or trios on a single computer
	- Discuss your algorithm **BEFORE YOU WRITE ANY CODE**. Make sure everyone understands.
- You are working in `Prob2.py`
- Initial tasks:
	- Read in the contents of `moby_dick.txt`, which contains the first paragraph from the classic text.
	- Print the text to the screen without any line breaks. (It will still wrap at the end of your terminal, that is ok.)


## Problem 2b: The Great White Swine?
- Swap who is typing!
- Now you want to "Pig-Latinify" the text
- Will require extracting individual words from each string and passing into the imported `word2piglatin` function
	- This function has been written to be able to work with punctuation. So you don't need to strip out punctuation. You can just pass in any string of characters that appears between two space.
- Print out the "Pig-Latinified" text to the terminal!


## Problem 2c: The Great White Publisher
- Swap who is typing!
- This new version of Moby Dick is too good to let vanish!
- Write it to a new file, called `moby_bacon.txt`
- Format it across the same number of lines in this file as in the original


# Demo

## Fingerprinting
- Suppose we had a text file that stores information about a particular users fingerprint
    - Name, dimensions, and the print itself
- We want to read this information in and display the fingerprint as a `GImage`
- Possible extensions if time:
	- Then we want to allow the user to click on parts of the fingerprint and store those important coordinates to a file
