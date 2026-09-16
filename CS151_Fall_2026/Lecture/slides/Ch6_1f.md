---
title: "Binary Strings"
author: Fred Agbo & Jed
date: "September 16, 2026"
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
- Class code is `TD9RC0`
- Introduce yourselves! What is your favorite number in binary?
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
- Problem Set 3 is live and due on Monday Sept 21!
- Thanks to those who attended the SCIS Open House
    - Any follow up questions, please ask me.


# Group Problems

## Problem 1: Base-ic Counting
::::::cols
::::col
- How would you write out a representation of the number of circles to the right in:
  - Decimal (base-10)
  - Binary (base-2)
  - Octal (base-8)
  - Hex (base-16)
::::

::::col
\begin{tikzpicture}%%width=80%
\foreach \c in {0,1,...,17} {
	\pgfmathparse{floor(\c/4)}
	\def\y{\pgfmathresult}
	\pgfmathparse{Mod(\c,5)}
	\def\x{\pgfmathresult}
	\node[circle, thick, fill=Red, minimum size=0.75cm] at ({Mod(\c,5)}, {floor(\c/5)}) {};
}
\end{tikzpicture}
::::
::::::



## Problem 2: Getting Energized
- The Java compiler has a fun quirk where every binary file it produces begins with
<br><br>

\begin{tikzpicture}%%width=70%
[
every node/.style={draw, thick, Green, font=\Large}
]
\node(1) at (0,0) {1};
\node[right=0cm of 1](1) {1};
\node[right=0cm of 1](1) {0};
\node[right=0cm of 1](1) {0};
\node[right=0cm of 1](1) {1};
\node[right=0cm of 1](1) {0};
\node[right=0cm of 1](1) {1};
\node[right=0cm of 1](1) {0};
\node[right=0cm of 1](1) {1};
\node[right=0cm of 1](1) {1};
\node[right=0cm of 1](1) {1};
\node[right=0cm of 1](1) {1};
\node[right=0cm of 1](1) {1};
\node[right=0cm of 1](1) {1};
\node[right=0cm of 1](1) {1};
\node[right=0cm of 1](1) {0};
\end{tikzpicture}

<br>

- What is this in octal? hexadecimal?
- There are hard ways to do this, and very easy ways! I recommend the easy ways :)

## Floating Representations
- Python represents floating point (fractional) numbers using two integers
	- One to represent the significant digits
	- One to represent the exponent (where the decimal place is)
- $1\frac{1}{4}$ Example
	- In decimal:
		$\quad\displaystyle 1\frac{1}{4} = \frac{1}{1} + \frac{2}{10} + \frac{5}{100} = 1.25 = (125, -2)$
	- In binary:
		$\quad\displaystyle 1\frac{1}{4} = \frac{1}{1} + \frac{0}{2} + \frac{1}{4} = 1.01 = (101, -10)$

## Problem 3: Floating Problems
:::incremental
- With this in mind, how could you convert the value $\tfrac{7}{8}$ to a binary floating point representation?
-
	$$\frac{7}{8} = \frac{0}{1} + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} = 0.111 = (111, -11)$$
- Now how would we convert $\frac{1}{10}$ to binary??
	- We run into a problem! An infinitely repeating sequence!
	$$\frac{1}{10} = \frac{0}{1} + \frac{0}{2} + \frac{0}{4} + \frac{0}{8} + \frac{1}{16} + \frac{1}{32} + \frac{0}{64} + \frac{0}{128} + \frac{1}{256} +  \cdots = 0.0001100110011\ldots$$ 
	- Have to stop the sequence somewhere and approximate it:
		$$\frac{3}{32} = 0.09375\quad\text{or}\quad\frac{25}{256} = 0.09765625$$
:::

## Consequences
- The best we can do within the range of normal integers
	$$\frac{3602879701896397}{2^{55}} = 0.10000000000000000555111512312578270$$
- When doing operations on these numbers, extra decimals will sometimes get rounded off, suddenly making the number look precise, but you might always have a tiny bit of this rounding error showing up in floating point values.
- So be _careful_ using `==` for floating numeric comparisons! Rounding might result in unexpected falsehoods
	- `0.1 + 0.1 + 0.1 != 0.3`
	- Far better to check if two numbers are within a small margin of one another, or greater or less than the other


# Live-Coding

## Concatenating ASCII
- Suppose we wanted to print out the simple ASCII table as we saw it in the video
- Grid of 8 rows and 16 columns
- We can use `chr` to get the characters
- Need to "build-up" a string to print for each row

## A Solution
```{.python style='max-height: 800px; font-size:.8em;'}
row=''
for i in range(32,127):
    if len(row) == 16:
        print(row)
        row = ""
    row = row + chr(i)
print(row)
```
