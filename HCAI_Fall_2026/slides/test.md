---
title: "Kickoff: Course Overview"
author: "Jed Rembold"
date: April 28, 2023
slideNumber: true
theme: moon
highlight-style: espresso
width: 1920
height: 1200
transition: slide
hash: true
history: false
format:
revealjs:
center: false        # Disable vertical centering globally
scrollable: true     # Make all slides scrollable
smaller: false       # Or true for smaller text globally
---


---


## Announcements
- Adventure due next Wednesday!
- I'll be putting review materials up on the website today I'll be putting review materials up on the website today
	- Will include a sample exam as well as objective list
- Polling: [rembold-class.ddns.net](http://rembold-class.ddns.net)
- Let us __come to the hall__ on time and gather at **5pm to receive the lecture**

## Basic Program Elements

- Python programs consist of one or more modules
- Module: a file of Python code
	- Can include statements, function definitions, and class definitions
- Script: a short Python program
	- Can be contained in one module
- Longer programs typically include
	- One main module and one or more supporting modules
- Main module
	- Contains starting point of program execution
- Supporting modules
	- Contain function and class definitions

## An Example Python Program: Guessing a Number

```{.python}
import random
 
def main():
	"""Inputs the bounds of the range of numbers
	and lets the user guess the computer’s number until
	the guess is correct."""
	smaller = int(input("Enter the smaller number: "))
	larger = int(input("Enter the larger number: "))
	myNumber = random.randint(smaller, larger)
	count = 0
	while True:
		count += 1
		userNumber = int(input("Enter your guess: "))
		if userNumber < myNumber:
			print("Too small")
		elif userNumber > myNumber:
			print("Too large")
		else:
			print("You’ve got it in", count, "tries!")
			break
 
if __name__ == "__main__":
	main()

```


## Make a round twice