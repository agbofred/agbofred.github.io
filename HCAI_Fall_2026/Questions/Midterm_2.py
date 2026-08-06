# QUESTIONS ON FUNCTIONS

#Question 1A: Knowledge on Function and and scope: #Answer: -5
def f1(x,y):
    return z + f2(x,y)
 
def f2(x,y=1):
    def f3(k):
        return (y + k) ** 2
    z = x - f3(y)
    return z - y
 
z = 1
print(f1(f2(4),z))

#Question 1B: Amswer: print(f1(f2(4),z))
"""
In Python, you can pass a function as a parameter to some other function. 
Write out the line in question 1(a) that exhibits this characteristic. 

"""
# Question 1C: Function #Answer = happyday
def puzzle(t): 
    def mystery(r,x): 
        x+=2 
        def enigma(s=0): 
            return r[s::x] 
        return enigma 
    x=1 
    y= mystery(t,x=x) 
    return y(x)+ y() + y(s=8)
print(puzzle("phsyahdpya"))

# Question 1D Amswer: 
                    #   return enigma
                    #   y= mystery(t,x=x) 
                    #   return y(x)+ y() + y(s=8)
"""
Functions in Python are said to be first-class functions where you can assign
them to a variable, pass it as a parameter, or return it as a result. 
From question 1C, which line(s) of code depicts example of this behaviour?

"""

"""---------------------"""
#QUESTIONS ON LIST
#Question 2A
"""
Write a function that receives a string and return a list of tuples containing the unique letters and their frequencies in the string. 
Display the list to the terminal showing each letter with its frequency on a new line. Your function should ignore case sensitivity (that is, 'a' and 'A' are the same).

For example: mystring = 'Today is midterm test'
Output:
a: 1
d: 2
e: 2
i: 2
m: 2
o: 1
r: 1
s: 2
t: 4
y: 1
"""

#One sample solution to Q2A is below
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def summarize_letters(string):
    letters = []
    counts = []
    
    for letter in string.lower():
        if letter in ALPHABET:
            if letter in letters:
                index = letters.index(letter)
                counts[index] += 1
            else:
                letters.append(letter)
                counts.append(1)
           
    tuples = list(zip(letters, counts))
    tuples.sort()
    return tuples

mystring = 'Today is midterm test'
summary = summarize_letters(mystring)

# display counts
for char, count in summary:
    print(f'{char}: {count}')


# Question 2B
"""
    Write a python program that insert 20 random letters in the range 'a' through 'f' into a list. 
    Perform the following tasks on the list and display your results;
      i. Sort the list in ascending order 
      ii. Sort the list in descending order 
      iii. Get the unique values and sort them in an ascending order
"""

# One sample of solution to 2B is below
import random

#Generate list 
random_letters = [random.choice('abcdef') for i in range(20)]

print("Original list:", random_letters)

#First step
ascending_order = sorted(random_letters)
print("Ascending order:", ascending_order)

#Second step
descending_order = sorted(random_letters, reverse=True)
print("Descending order:", descending_order)

#Third step
unique_values = []
for i in random_letters:
    if i not in unique_values:
        unique_values.append(i)
    unique_values.sort()
#unique_values = sorted(set(random_letters))
print("Unique values in ascending order:", unique_values)


"""---------------------"""
#QUESTIONS ON GRAPHICS
"""
Write Python program that uses the PGL library to achieve the following:
 i. Draw an 8X8 checkerboard to the center of the canvas.
 ii. Add a caption or lable directly below the checkerboard 
Note that the checkerboard and its label must be placed at the center of the canvas and you are free to choose any color aside from black and white as shown in an example below.
You should assume that all the neccessary PGL library for this program have been imported.


"""
from pgl import GWindow, GRect, GLabel, GCompound
GWidth= 500
Gheight = 500

def create_board():
    b = GCompound()
    for c in range(0,8):
        for r in range(0,8):
            rect = GRect(30*c,30*r,30,30)
            #rect.set_location(board.get_width()*20*c,board.get_height()*20*r)
            if (r+c) % 2 != 0:
                rect.set_filled(True) 
            b.add(rect)
    return b

gw = GWindow(GWidth,Gheight)
board = create_board()
board.set_location(120, 120)
label = GLabel("An 8X8 checkerboard designed by Fred!")
label.set_font("14px 'Times New Roman'")
x = (gw.get_width() - label.get_width()) / 2
y = (board.get_height() + gw.get_height() + label.get_ascent()) / 2

gw.add(board)
gw.add(label, x,y)



