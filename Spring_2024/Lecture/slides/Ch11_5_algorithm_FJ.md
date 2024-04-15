---
title: "Searching Algorithm"
author: Jed Rembold and Fred Agbo
date: April 15, 2024
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
- Personal Project is due tonight at 10 pm!
	- If you are asking for extension, send me an email. 
		- I will check to see you have not used your 3 chances before granting it.
- Project 5 __Adventure__ guidelines is posted.
	- Due on ***Monday 29th of April at 10 pm***  (i.e., exactly 2 weeks from now!)
	- You __Can__ work with a partner on this project. Both partners will earn the same grade. 
- Polling: [https://www.polleverywhere.com/agbofred203](https://www.polleverywhere.com/agbofred203)


## Review Question!

::::cols
:::col
The two classes to the right mimic a bit of what might occur in the course of the Adventure Project. What python data type is `ANS`?

:::::poll
#. A String
#. An AdvObject
#. An AdvLocation
#. A List
:::::


:::
:::col


```{.python style='max-height:1000px; font-size:.6em;'}
class AdvObject:
	def __init__(self, name, loc):
		self.name = name
		self.loc = loc
	def get_loc(self):
		return self.loc

class AdvLocation:
	def __init__(self, name):
		self.name = name
		self.stuff = []
	def store(self, item):
		self.stuff.append(item)
	def retrieve_top(self):
		return self.stuff.pop()

A = AdvObject("Hammer", "RA")
B = AdvObject("Torch", "RA")
RA = AdvLocation("Room A")
RA.store(A)
RA.store(B)
ANS = RA.retrieve_top().get_loc()
```
:::
::::

<!--
## Abstract Data Types
- Many object types have some aspect of storing information as their primary purpose
- Types that are instead defined largely by their behavior are called _abstract data types_ or _ADT_ s which have the following advantages
	- Simplicity. The internal representation is hidden from the client
	- Flexibility. If the internal representation needs to be changed by the programmer, they can do so without breaking outside compatibility
	- Security. Keeping the internal representation away from clients; prevents clients from directly altering values that may cause the type to behave unexpectedly
- Want to start to focus on how we can bring all these ideas together to define our own abstract types


## Token ADT
-  Think of ADT's as a data type which helps to fulfill a particular objective or behavioral goal
	- They are little machines, packaged up inside a class
- Thinking back to our Pig Latin translation program:
	- `word_to_pig_latin` took a single word and translated into Pig Latin
	- To translate an entire sentence, we would need code to break the sentence up into individual words, which we could then pass into `word_to_pig_latin`
- The latter is an example of something that comes up often in computer science: breaking a larger thing into particular smaller chunks
	- These "chunks" can really be anything, so the more general term computer scientists use is a _token_

## A Token Scanner
- A class that plucked out individual tokens might be called a _token scanner_
- What would a client want from a token scanner?
	- A way to pass in the necessary input
	- A way to retrieve the next individual token
	- A way to know when there are no more tokens
	- Maybe a way to tailor what tokens are desired
- These requirements help inform what methods should be incorporated into a token scanner class!
	- Still need to determine what internal attributes or method might be needed

## Token Scanner Design
- Frequently, specific wants or objectives make for good methods to include in the token scanner
- Chapter 10 includes an example of a common implementation
- Exports 4 main methods:
	#. `scanner.set_input(str)`
	    - Sets the input of the token scanner to the specified string or input stream
	#. `scanner.next_token()`
		- Returns the next token from the stream, or `""` at the end
	#. `scanner.has_more_tokens`
		- Returns `True` if more tokens exist, `False` otherwise
	#. `scanner.ignore_whitespace()`
		- Customization option which tells the scanner to ignore whitespace characters

## Token Scanner Code
```{.python style='max-height:900px; font-size:.6em; font-spacing:2em;' data-line-numbers='7-46|54-59|63-69|71-86|88-94|96-100|104-109'}
# File: tokenscanner.py

"""
This file implements a simple version of a token scanner class.
"""

# A token scanner is an abstract data type that divides a string into
# individual tokens, which are strings of consecutive characters that
# form logical units.  This simplified version recognizes two token types:
#
#   1. A string of consecutive letters and digits
#   2. A single character string
#
# To use this class, you must first create a TokenScanner instance by
# calling its constructor:
#
#     scanner = TokenScanner()
#
# The next step is to call the set_input method to specify the string
# from which tokens are read, as follows:
#
#     scanner.set_input(s)
#
# Once you have initialized the scanner, you can retrieve the next token
# by calling
#
#    token = scanner.next_token()
#
# To determine whether any tokens remain to be read, you can either
# call the predicate method scanner.has_more_tokens() or check to see
# whether next_token returns the empty string.
#
# The following code fragment serves as a pattern for processing each
# token in the string stored in the variable source:
#
#     scanner = TokenScanner(source)
#     while scanner.has_more_tokens():
#         token = scanner.next_token()
#         . . . code to process the token . . .
#
# By default, the TokenScanner class treats whitespace characters
# as operators and returns them as single-character tokens.  You
# can set the token scanner to ignore whitespace characters by
# making the following call:
#
#     scanner.ignore_whitespace()

class TokenScanner:

    """This class implements a simple token scanner."""

# Constructor

    def __init__(self, source=""):
        """
        Creates a new TokenScanner object that scans the specified string.
        """
        self.set_input(source)
        self._ignore_whitespace_flag = False

# Public methods

    def set_input(self, source):
        """
        Resets the input so that it comes from source.
        """
        self._source = source
        self._nch = len(source)
        self._cp = 0

    def next_token(self):
        """
        Returns the next token from this scanner.  If called when no
        tokens are available, next_token returns the empty string.
        """
        if self._ignore_whitespace_flag:
            self._skip_whitespace()
        if self._cp == self._nch:
            return ""
        token = self._source[self._cp]
        self._cp += 1
        if token.isalnum():
            while self._cp < self._nch and self._source[self._cp].isalnum():
                token += self._source[self._cp]
                self._cp += 1
        return token

    def has_more_tokens(self):
        """
        Returns True if there are more tokens for this scanner to read.
        """
        if self._ignore_whitespace_flag:
            self._skip_whitespace()
        return self._cp < self._nch

    def ignore_whitespace(self):
        """
        Tells the scanner to ignore whitespace characters.
        """
        self._ignore_whitespace_flag = True

# Private methods

    def _skip_whitespace(self):
        """
        Skips over any whitespace characters before the next token.
        """
        while self._cp < self._nch and self._source[self._cp].isspace():
            self._cp += 1
```

## Using `TokenScanner`
- Need to initialize the token scanner object
- Generally keep looping as long as there are still tokens
	- Each iteration, get the latest token and then do something with it


## Using `TokenScanner` in `PigLatin`
```{.python style='max-height:900px'}
from tokenscanner import TokenScanner

def to_pig_latin(text):
	translation = ""
	scanner = TokenScanner()
	scanner.set_input(text)
	while scanner.has_more_tokens():
		token = scanner.next_token()
		if token.isalpha():
			token = word_to_pig_latin(token)
		translation += token
	return translation
```
-->
## Searching for Efficiency
- Our last chapter is less about introducing new programming machinery and more about better understanding what we already have
- Hopefully you have realized by now that there can be **many** approaches to solving a problem computationally
	- So far, the first way you figure out has likely been the "best", in that it gets the job done.
	- Sometimes there is a different though in an approach that is technically correct and one that is practically correct.
	- How can we make informed choices about the algorithms we use?
- Want to look at algorithm efficiency in this chapter
- Will focus mainly on Searching and Sorting as our examples to better understand how an algorithm's efficiency can be quantified


## A Linear Search
- Suppose you needed to determine if a particular element was in a list, and didn't have any of the built-in methods available to you
- The easiest method (which many of you have indeed used!) is to just search through the list element by element and check it to see if it is the one you desire
	- This approach is called a _linear search_
- Easy to understand and implement:
  ```python
  def linear_search(quest, array):
  	  for i in range(len(array)):
  		  if array[i] == quest:
  			   return i
  	  return -1
  ```


## Linear Search from English Words 
- Assuming we would like to search for a word in the list of `ENGLISH_WORDS`
- The Python strategy using `is_english_word` would below
```python
def is_english_word(s):
	s = s.lower()
 	for i in range(len(ENGLISH_WORDS)):
 		if s == ENGLISH_WORDS[i]:
 		return True
 	return False
```
- The for loop begins at the beginning and continues until it comes to the end of the ENGLISH_WORDS array. 
- The function returns `True` when it finds the word in the array or, `False` when it fails to find the word at the end of the for loop.


## Searching for Area Codes
- To illustrate the efficiency of linear search, it can be helpful to work with a larger dataset
- We'll look here at searching through potential US area codes to find that of Salem: 503
- Linear search examines each value in order to find the matching value. 
	- As the arrays get larger, the number of steps required also grows
- As you watch linear search do its thing on the next slide, see if you can beat the computer at finding 503. 
	- What approach did you take?

## Linear Search in Action
<div class="fig-container" data-file="../images/d3/LinearSearch.html" data-style="width:100%; display:inline;" data-scroll="no"></div>


## How did you do?
- Frequently, many people can "beat the animation" in finding 503
- Approaches vary, but you may well have done something along the lines of:
	- Look at some number in the middle
	- Depending on how close it was to 503, jump ahead some in that direction and check again
- Requires some special conditions though, so let's try again

## Racing Linear Search Again
<div class="fig-container" data-file="../images/d3/LinearSearch_v2.html" data-style="width:100%; display:inline;" data-scroll="no"></div>


## Idea of a Binary Search
- If your data is ordered, then you might try a alternative search strategy
- Look at the center element in the array, it is either:
	- The value you want. Excellent! Return it.
	- A value larger than what you want. Throw away that value and everything bigger.
	- A value smaller than what you want. Throw away that value and everything smaller.
- Then you can repeat the process with the remaining elements until you find your value
- Since number of searched elements is divided by 2 each time, called a _binary search_


## Binary Search in Action
<div class="fig-container" data-file="../images/d3/BinarySearch.html" data-style="width:100%; display:inline;" data-scroll="no"></div>


## Implementing Binary Search
```{.python style="max-height:900px"}
def binary_search(target, array):
	lh = 0
	rh = len(array) - 1
	while lh <= rh:
		middle = (lh + rh) // 2
		if array[middle] == target:
			return middle
		elif array[middle] < target:
			lh = middle + 1
		else:
			rh = middle - 1
	return -1
```
## Sorting
- Binary search only works on arrays in which the elements are ordered.
	- The process of putting the elements into order is called _sorting_.
- Lots of different sorting algorithms, which can vary substantially in their efficiency.
- From an algorithms view, sorting is probably the most applicable algorithm we'll discuss in this course
	- Organizing data makes it easier to digest that data, whether the data is being digested by other machines or by humans


## Selection Sort
- The easiest sorting algorithm to explain is that of _selection sort_
- Imagine your left hand keeping track of where you were in the array, and your right hand scanning through and finding the next smallest value to move to that location each iteration

```python
def selection_sort(array):
	for lh in range(len(array)):
		rh = lh
		for i in range(lh+1, len(array)):
			if array[i] < array[rh]:
				rh = i
		array[lh], array[rh] = array[rh], array[lh]
```

## Following Selection Sort
```{.python data-line-numbers='1-9|2|3|4|5|4|5|4|5|6|4|5|4|5|4|5|4|5|4|5|6|4|4|7|2|3|4|1-9'}
def selection_sort(array):
	for lh in range(len(array)):
		rh = lh
		for i in range(lh+1, len(array)):
			if array[i] < array[rh]:
				rh = i
		array[lh], array[rh] = array[rh], array[lh]
L = [31, 41, 59, 26, 53, 58, 97, 93, 23, 84]
selection_sort(L)
```

<div class="fig-container" data-file="../images/d3/SelectionSort.html" data-scroll="no", data-style="width:90%; display:inline;"></div>

