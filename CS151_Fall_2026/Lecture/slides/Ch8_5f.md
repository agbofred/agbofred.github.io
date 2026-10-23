---
title: "Reading & Writing Files"
author: Fred Agbo
date: "October 23, 2026"
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
- Class code is `HPYHr`
- Introduce yourselves! What is your favorite textbook?
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

- Problem set 5 is due next week Monday.
- The deadline for courses withdrawal is today Friday October 23 at 5pm.

--- 

## Recall the Moon Thresholding Problem

- On wednesday, we got the files from the __Discord__ and completed the first task
- Initial tasks:
	- Add a dark blue background rectangle to the window
	- Add a `GImage` of the `moon.png` image centered in the window

---

## Problem 2b: Odd Pixels
- Extract the pixel array from the moon image
- This moon image is a grayscale image, so the Red, Green, and Blue components are always equal
- Looping over all the pixels, how many pixels are darker than a value of 30?

:::notes
Should be 65760
:::

---

## Problem 2c: Thresholding
- Modify your last code to actually update the pixels in the array
	- If they are darker than 30, set them to a perfectly black pixel
	- Otherwise, set them to a perfectly white pixel
- Pass the updated pixel array into `GImage(pix_array)` and add the result to the window
- Play around with the thresholds to see different effects
- Since you are adding it on top of the original, you can also play around with giving the pixels some transparency (or making them different colors!)

---

## Reading & Writing Files
- Programs often need to work with collections of data that are too large to reasonably exist typed all out in the code
	- Easier to read in the values of a list from some external data file
- A _file_ is the generic name for any named collection of data maintained on some permanent storage media attached to a computer
- Files can contain information encoded in many different ways
	- Most common is the _text file_
	- Contains character data like you'd find in a string

---

## Strings vs Text Files
- While strings and text files both store characters, there are some important differences:
	- **The longevity of the data stored**
		- The value of a string variable lasts only as long as the string exists, is not overridden, or is not thrown out when a function completes
		- Information in a text file exists until the file is deleted
	- **How data is read in**
		- You have access to all the characters in a string variable pretty much immediately
		- Data from text files is generally read in sequentially, starting from the beginning and proceeding until the end of the file is reached

---

## Reading Text Files
- The general approach for reading a text file is to first _open_ the file and associate that file with a variable, commonly called its _file handle_
- We will also use the _with_ keyword to ensure that Python cleans up after itself (closes the file) when we are done with it.
  ```python
  with open(filename) as file_handle:
  	# Code to read the file using the file_handle
  ```
- Python gives you several ways to actually read in the data
	- `read` reads the entire file in as a string
	- `readline` or `readlines` reads a single line or lines from the file
	- `read` alongside `splitlines` gets you a list of line strings
	- Can use the file handle as an iterator to loop over

---

## Entire file ⟶ String
- The `read` method reads the entire file into a string, with includes newline characters (`\n`) to mark the end of lines
- Simple, but can be cumbersome to work with the newline characters, and, for large files, it can take a large amount of memory

- As an example, the file:

  :::{.block name="Seuss.txt" style='width:40%; margin-left: auto; margin-right: auto;'}
	One fish<br>
	two fish<br>
	red fish<br>
	blue fish
  :::

  would get read as `"One fish\ntwo fish\nred fish\nblue fish"`{style="display: block; margin: auto; text-align: center;"}

---

## Line by Line
- Of the ways to read the file in a string at a time, using the file handler as an iterator and looping is probably best and certainly most flexible
- Leads to code that looks like:
  ```python
  with open(filename) as f:
	  for line in f:
		  # Do something with the line
  ```
- Note that **most** strategies preserve the newline character, which you very likely do not want, so be ready to strip them out before doing more processing

---

## String Methods That Involve Lists
- `str.split()` splits `str` into a list of substrings at each whitespace character
- `str.split(separator)` splits `str` into a list of substrings at each occurrence of `separator`
- `str.splitlines()` splits `str` into a list of substrings at each line break
- `sep.join(list)` joins the elements of `list` into a string, using `sep` to separate them

---

## Powers Combined
- So long as your files are not gigantic, using `read` and then the `splitlines` method can be a good option
- This **does** remove the newline characters, since it splits the string at them
  ```python
  with open(filename) as f:
	  lines = f.read().splitlines()
  # Then you can do whatever you want with the list of lines
  ```

---

## Writing Text Files
- You can write text files using almost the same syntax as reading:
  ```python
  with open(filename, mode) as file_handle:
  	  # Code to write the file using file_handle
  ```
- Note the `mode` parameter to `open` here! Mode is a string which is either
	- `"w"` to **write** a new file (or overwrite an existing file)
	- `"a"` to **append** new contents to the end of an existing file
- The file handler supports the methods:
	- `.write(some_string)` to write a string to the file
	- `.writelines(iterable_of_strings)` to write each iterable element to the file

---

## Aren't you Exceptional
:::{.sml style="font-size: 45px;"}
- When opening a file for reading, it is possible the file does not exist!
	- Python handles this (and many other potential errors that can arise) using a mechanism called _exception handling_
	- Common in other languages as well
- An _exception_ is a object that belongs to an overarching hierarchy of exception classes
	- Different classes/types for different purposes
	- File operations, for example, use the exception class `IOError`
- If `open` encounters an error, it reports the error by _raising an exception_ with `IOError` as its type.
	- Raising an exception generally immediately terminates your program, but sometimes that is undesirable
:::

---

## Ignore Yoda, there is a `try`
:::{.sml style="font-size: 45px;"}
- Python uses the `try` statement to indicate an interest in trying to handle a possible exception
- In simplest form, the syntax is:
  ```python
  try:
  	  # Code that may cause an exception
  except type_of_exception:
  	  # Code to handle that type of exception
  ```
- `type_of_exception` here is the class name of the exception being handled
	- `IOError` for the file reading errors we are discussing
- Any exceptions arising from within the `try` block or within functions *called* within the try block would be "caught" and the lower block of code run instead of terminating the program
:::

---

## Example: Requesting Existing File
:::{.sml style="font-size: 45px;"}
- As an example, the below function will repeatedly ask the user to supply a file name that actually exists. 
- It will not just immediately break should they give it an invalid filename!
  ```python
  def get_existing_file(prompt="Input a filename: "):
	  while True:
		  filename = input(prompt)
  		  try:
  			  with open(filename):
  				  return filename
  		  except IOError:
  			  print("That filename is invalid!")
  ```
- If the `open` call succeeds, we immediately just return the filename, but if it fails due to a `IOError`, we display a message and then keep asking
:::


<!--
## Choosing Wisely
:::{.sml style="font-size: 45px;"}
- The Python package used to implement `pgl.py` also supports a mechanism to choose files interactively, made available through the `filechooser.py` library module.
- `filechooser.py` exports two functions:
	- `choose_input_file` for selecting a file
	- `choose_output_file` for selecting a folder and filename to save a file to
- Both open up a file dialog that lets you select/choose a file
	- Clicking Open or Save returns the full pathname of the file
	- Clicking Cancel returns an empty string

- Using it thus looks something like:
```python
filename = choose_input_file()
with open(filename) as f:
	# Code to read file
```
:::


 ## Writing ASCII SINE
- Suppose I wanted to try my hand at some ASCII art and fill a text file with a vertical oscillating sine wave
- A sine wave generally looks like:
	$$ A + A \sin\left(\frac{2\pi}{T}x\right)$$
  where $A$ is the amplitude of the wave and $T$ the period of the wave, or how quickly it repeats
  - The extra $A +$ out front is to push the wave over to the right, since we can't really place negative characters
- How can we put this together?


## ASCII SINE Code
```{.python style='font-size:.6em; max-height:900px;'}

from math import sin, pi

def sine_file(filename, A, T, symbol, padding=" "):
    """ 
    Creates a new sine wave in the provided file with the provided amplitude (A),
    and period (T) with the indicated symbol at the end.

    Inputs:
        filename (string): the name of the file to write the art to
        A (int): the amplitude of the wave in terms of number of characters
        T (int): the period of the wave in terms of number of lines
        symbol (string): the symbol to place to mark the wave
        padding (string): what character to pad the left side of the wave with

    Outputs:
        None
    """

    def compute_symb_placement(A, T, x):
		"""Computes where the symbol should be placed."""
        value = A * sin(2 * pi / T * x) + A
        return int(value) # to integer character placement

    def construct_line(placement, symbol, padding):
		"""Constructs the line with the necessary padding and symbol at the end."""
        return padding * placement + symbol

    with open(filename, 'w') as fh:
        for x in range(10 * T): # write 10 periods worth of lines
            v = compute_symb_placement(A, T, x)
            line = construct_line(v, symbol, padding)
            fh.write(line + '\n') # need the newline character at the end!

if __name__ == '__main__':
    sine_file('sine_test.txt', A=30, T=50, symbol='X')
``` -->

## Today's Group Problems LO's
- Understanding how to open a file
- Reading contents from a file
- Writing text back to a file

---

## Problem 1: Inconceivable Code
:::{.sml style="font-size: 45px;"}
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
:::


---

## Problem 2a: The Great White Whale
- If you have not done so, get the starter files from the __Discord__
- This is a coding problem. Work in pairs on a single computer
	- Discuss your algorithm **BEFORE YOU WRITE ANY CODE**. Make sure everyone understands.
- You are working in `Prob2.py`
- Initial tasks:
	- Read in the contents of `moby_dick.txt`, which contains the first paragraph from the classic text.
	- Print the text to the screen without any line breaks. (It will still wrap at the end of your terminal, that is ok.)

---

## Problem 2b: The Great White Swine?
- Swap who is typing!
- Now you want to "Pig-Latinify" the text
- Will require extracting individual words from each string and passing into the imported `word2piglatin` function
	- This function has been written to be able to work with punctuation. So you don't need to strip out punctuation. You can just pass in any string of characters that appears between two space.
- Print out the "Pig-Latinified" text to the terminal!

---

## Problem 2c: The Great White Publisher
- Swap who is typing!
- This new version of Moby Dick is too good to let vanish!
- Write it to a new file, called `moby_bacon.txt`
- Format it across the same number of lines in this file as in the original