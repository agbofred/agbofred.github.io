"""
Question 1.

Consider the program for finding the factor of a number 
using brute-force strategy as shown below. 

"""

def largest_factor(n):
    for i in range(n - 1, 0, -1):      
        for j in range(1, n):          
            pass                       
        if n % i == 0:
            return i

if __name__ == '__main__':
    print(largest_factor(27))


"""
A) What output will the code above print? 
Ans: 9

B) What is the asymptotic time complexity of the algorithm?

Ans: O(n^2)

--------  
"""
# -----------------------------------------------
"""
Q2:
Consider the program below
"""
# Answer is ('a', 'M_byte'), 'M_byte') >>>>>Note! if line 34 is  a concatenation say C = B + ('b', ), then it returns error of not able to concetnate string and tuple
var_A = (8, 16, 32, )
var_B = (2*var_A, ('bits', ) )
var_C = var_B , ('M_byte', 'G_byte', 'T_byte')
var_D = ("a",)
for v in var_C[1:]:
    var_D += v[:1]
print(var_D)

"""
A) What output will the program print?

Ans: ('a', 'M_byte')

B) What data type is the printed value in 1A?

Ans: tuple
"""
#------------------------------------------

"""
Q3. 
A)    If the ASCII code of charater 'H' is represented as 0X48 in hexadecimal, 
    what is the base 10 integer value representation of 'H'?

    ANS:72

B) If ASCII code of character 'h' is reprented as 0X68 in hexadecimal, 
    what will be the octal representation value of 'h' in base 8?


ANS: 0o150
"""
#-----------------------------------------------

""" 
Q4.
Consider the program below
"""
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

"""
A) What output will the program print?

Ans: happyday


B)

Functions in Python are said to be first-class functions where you can assign
them to a variable, pass it as a parameter, or return it as a result. 
Observe the program in question 4A above, which line(s) of code depicts example of first-class function?

# Ans: 
    #   return enigma
    #   y= mystery(t,x=x) 
    #   return y(x)+ y() + y(s=8)


"""


#-----------------------------------------------------
"""

Q5:Interactive Graphics
A pie chart is a common visualization method used to convey approximate relative percentages among several categories. 
Comprised of filled colorful wedges (which can be portrayed in this problem using a filled GArc), 
the idea is that each wedge has a size or takes up a portion of the overall circle equal to it's category percentage. 
For instance, the below image shows a pie chart with the red category taking up 50% of the circle, 
the green taking up 30% of the circle and then the blue taking up 20% of the circle.


Your task in this problem will be two-fold: you'd like to both create a pie-chart from a list
of category percentages, but then you'd also like to add some simple mouse interactions.


A). Define a function 'def create_pie_chart()' which will take one argument 
'list_of_percents' - a list of the various category percentages as integers.
This list could have any number of elements, but you are guaranteed that all the
integers within it will add up to 100. Your program should create the necessary
GWindow and then add the needed filled GArcs to create the appearance of a pie
chart centered in the window. You can imagine there are several constants already
defined at the top of the file that you can use:

COLORS = [" red ", " green ", " blue ", " orange "] #colors
GW_WIDTH = 500 # width of window
GW_HEIGHT = 500 # height of window
CHART_RADIUS = 150 # radius of pie chart
HIGHLIGHT_THICKNESS = 10 # line thickness when clicked

As you work through this part, a few extra things to keep in mind:
• The exact rotation of the overall pie chart doesn't matter, though it can be
easiest to start the first wedge at PGL's 0 angle.
• The desired colors of each wedge are given in the COLORS constant, and should
be cycled through. If you have more wedges than colors, then the sequence
should start over, so that the 5th wedge would also be red.
• The elements of the list are integers that represent a percentage, they are not
angles. You will have to convert accordingly to what you need.


B). We'd like to add some interaction to the pie chart, so that when one of the wedges
is clicked, it is highlighted. To this end, you should add callback functions and
corresponding listeners for both "mousedown" and "mouseup". Upon pressing the
mouse down on top of a wedge, the line width of that wedge should be increased
to the specified HIGHLIGHT_THICKNESS and the wedge should be brought to the
front of the stacking order (otherwise parts of the thick line remain behind other
wedges, which looks weird). When the mouse is released, the line width should be
reset back to 0 (you don't need to do anything to the stacking order). Pressing or
releasing the mouse anywhere else on the screen should do nothing. An example of
what the green wedge would look like while being clicked is shown below.
"""


#Sample Solution 

from pgl import GWindow , GArc
COLORS = ["red", "green", "blue"]
GW_WIDTH = 500
GW_HEIGHT = 500
CHART_RADIUS = 150
HIGHLIGHT_THICKNESS = 10
def create_pie_chart (data):
    def down_action (event):
        elem = gw. get_element_at (event . get_x (), event . get_y ())
        if elem is not None :
            elem . send_to_front ()
            elem . set_line_width ( HIGHLIGHT_THICKNESS )
    def up_action ( event ):
        elem = gw. get_element_at ( event . get_x (), event . get_y ())
        if elem is not None :
            elem . set_line_width (1)
    gw = GWindow (GW_WIDTH , GW_HEIGHT )
    start = 0
    i = 0
    for entry in data :
        stride = int(entry /100*360)
        x = GW_WIDTH / 2 - CHART_RADIUS
        y = GW_HEIGHT / 2 - CHART_RADIUS
        arc = GArc (x , y,2* CHART_RADIUS ,2* CHART_RADIUS ,start , stride)
        arc . set_filled (True)
        arc . set_fill_color (COLORS [i % len( COLORS )])
        gw.add(arc)
        start += stride
        i += 1
    gw. add_event_listener ("mousedown", down_action )
    gw. add_event_listener ("mouseup", up_action )

if __name__=="__main__":
    create_pie_chart([50,30,20])

    # ----------------------------------------------------
"""
Q6.
    On July 4, 1776, the America Second Continental Congress unanimously adopted the Declaration of Independence.
    Since then, June 4 of every year is a federal holiday. Consider the data which represents weeks 
"""
data = [    
    {'week': 22,
        'days': {
            'Mon': "Workday",
            'Tue': "Workday",
            'Wed': "Workday",
            'Thu': "Workday",
            'Fri': "Workday",
            'Sat': "Weekend",
            'Sun': "Weekend"
        }
    },
    {  'week': 23,
        'days': {
            'Mon': "Workday",
            'Tue': "Independence Day!",
            'Wed': "Workday",
            'Thu': "Workday",
            'Fri': "Workday",
            'Sat': "Weekend",
            'Sun': "Weekend"
        }
    },
    {  'week': 24,
        'days': {
            'Mon': "Workday",
            'Tue': "Workday",
            'Wed': "Workday",
            'Thu': "Workday",
            'Fri': "Workday",
            'Sat': "Weekend",
            'Sun': "Weekend"
        }
    }
]


"""
A) Write python expression to select and print only the value with 'Independence Day!'.

# ANS: print(data[1]['days']['Tue'])
"""
# --------------------------------------------------------

""" 
B) Write a python program to format the data and print to terminal as shown in the example below

Week: 22 
--------
Mon: Workday
Tue: Workday
Wed: Workday
Thu: Workday
Fri: Workday
Sat: Weekend
Sun: Weekend

Week: 23 
--------
Mon: Workday
Tue: Independence Day!
Wed: Workday
Thu: Workday
Fri: Workday
Sat: Weekend
Sun: Weekend

Week: 24 
--------
Mon: Workday
Tue: Workday
Wed: Workday
Thu: Workday
Fri: Workday
Sat: Weekend
Sun: Weekend

"""
# My solution to question B
for i in range(len(data)):
    print(f"Week: {data[i]['week']} \n--------")
    for x,y in data[i]['days'].items():
        print(f'{x}: {y}')
    print()

# ----------------------------------------------------------------

"""
C) Write python program to store the formatted data structure in question B into 
the local computer memory with filename 'summer_calendar.txt' """

#My solution to question C
with open("End_of_year_calendar.txt", "w") as fh:
            for i in range(len(data)):
                fh.write(f"Week: {data[i]['week']} \n--------\n")
                for x,y in data[i]['days'].items():
                    fh.write(f'{x}: {y}\n')
                fh.write("\n")
