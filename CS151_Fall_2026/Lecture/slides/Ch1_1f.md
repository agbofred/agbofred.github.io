---
title: "Data Type & Functions?"
author: Fred Agbo & Jed
date: "September 2, 2026"
slideNumber: true
theme: "python_monokai"
highlightjs-theme: monokai
width: 1920
height: 1080
transition: fade
hash: true
history: false

---

## Happy Friday!!
::::{style='font-size:.8em'}
- Today's Grouping: Scan the QR code or go to [https://tools.jedrembold.prof/daily](https://tools.jedrembold.prof/daily)
- Class code is `LKhWDb`
- Introduce yourselves! Fun question: favorite name for a pet?
::::
::::::cols

::::col
![](../images/group_arrangement.png){width=60%}
::::
::::col
![](https://barcode.orcascan.com/?data=https://tools.jedrembold.prof/daily?code=LKhWDb){width=60%}
::::
::::::

---

## Quick Announcements
- Hopefully, everyone is already in a section which starts today
  - Attendance is mandatory
- Watching the videos and reading the text helps to give room for class activities
  - Both contributes to your class participation grades
- Problem Set 1 is due on Monday night!
- We are leaving Karel after a quick one more live demo today!
	- We've already covered everything Karel can do, and you should have all the tools needed for PS1
	- Karel will **not** understand the things we are talking about today and going forwards

---

<!-- Comments
- Problem 1: this just isn't really that interesting. How could this be more dynamic?
- Problem 2: Really liked this, and the extra bonus question I thought was fun.
- Problem 3: This felt like a good on-ramp type problem. Fairly quick, but helps get students sorted out
- Problem 4: I rather liked this, but it might be far more difficult if one of the targets isn't a 1
- Live Code: This I think hit the mark. I had time to do it justice, and I think it was useful.
-->
# Group Problems

---

## Problem 1: Arithmetic Operations
What value does the below expression evaluate to? What type of object is the result?

` 1 * 2 * 3 + (4 + 5) % 6 + (7 * 8) // 9 `{.python .inlinecode}

## Problem 2: Names are Hard
Some of the variable names below are invalid. If you take the 3rd character of each invalid variable name, they will form an anagram for a coding concept. What is the hidden word?

|||||
|--|--|--|--|--|
| `user_age` | `1st_place` | `bag%red`    | `first-name` | `_temp_celsius` |
| `elif`{.text}     | `AvgScore`  | `the num`    | `NUM_ITEMS`  | `x2`            |
| `@angle`{.text}   | `item_#`{.text}    | `__secret__` | `attempt23`  | `time4bed`      |

---

## Problem 3: Updates
::::::cols
::::col
What is the final value of the `A` variable at the end of the code to the right?
::::

::::col
```{.idle .python-repl}
>>> A = 10
>>> B = 4
>>> C = A * B
>>> A -= B
>>> A, B, C = C, A, B
>>> A
??
```
::::
::::::

---

## Problem 4: Birthday Variables
- Get the birth month number of each member of your group, and assign them to the variables `A`, `B`, `C`, etc.
- Your challenge is to get each of the variables equating to parts of today's date:
  ```python
  A = 1
  B = 23
  C = 20
  D = 26
  ```
- You are only allowed to use these variables, arithmetic operations, and `for` loops, updating from your starting values each step of the way
    - At no point should other numbers show up in your sequence of commands! (Except inside the `for` loop parentheses, if you use `for` loops

---

# Live-Coding

## Hot Glowing Things
- Planck's law governs the amount of light of a certain color that is emitted when something is glowing at a certain temperature
  $$ B(\lambda, T) = \frac{2hc^2}{\lambda^5} \frac{1}{e^{\frac{hc}{\lambda k_B T}} - 1} $$
- Where
  - $\lambda$ in the wavelength (color) of the light in meters
  - $T$ is the temperature of the object in kelvin
  - $h$ is Planck's constant: $6.62\times 10^{-34}$
  - $c$ is the speed of light: $3\times 10^8$
  - $k_B$ is Boltzmann's constant: $1.38\times 10^{-23}$

---

## Goal
- My goal is to write a short program that would allow a user to define the desired temperature and wavelength at the top, and then compute the brightness of that light

---

## A Solution
```{.python style='max-height: 800px; font-size:.8em;'}
wavelength = 400 * 10 ** -9 # meter
temperature =  1000 # kelvin

H = 6.62E-34
C = 3E8 # m/s
KB = 1.38E-23

first_fraction = 2 * H * C ** 2 / wavelength ** 5
exp_fraction = H * C / (wavelength * KB * temperature)
second_fraction = 1 / (2.71828 ** exp_fraction - 1)
brightness = first_fraction * second_fraction

print(brightness)
```

