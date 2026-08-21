"""
Question 1a.

The Kilburn’s algorithm for finding the factor of a number 
using brute-force strategy is shown below. 
What output will the code below print?
"""
def largest_factor(n):
    factor = n - 1
    while n % factor != 0:
        factor -= 1
    return factor

if __name__ == '__main__':
    print(largest_factor(36))

    """
    Ans: 18
    --------  ((2,5,2,5), 'b')
    """
# -----------------------------------------------
"""
Q1b:
What output will the following program print?
"""
# Answer is ((2,5,2,5),'b') >>>>>Note! if line 34 is  a concatenation say C = B + ('b', ), then it returns error of not able to concetnate string and tuple
A = (2, 5, )
B = (2*A, ('a', ) )
C = B ,('b', 'c', 'd')
D = tuple()
for v in C[:3]:
    D += v[:1]
print(D)

"""
2a. If the ASCII code of charater 'G' is represented as 0X47 in hexadecimal, 
    what is the base 10 integer value representation of 'G'?
ANS:71

2b. If ASCII code of character 'g' is reprented as OX67 in hexadecimal, 
    what will be the octal representation value of 'g' in base 8?


ANS: 0o147
"""
#-----------------------------------------------


""" 
Q3a.
What output will the following program print?
"""
def mystery (x , y =10):
    z = len (x)
    return puzzle (x , y) + puzzle (w[:enigma(z ,3)], y )
def enigma (x , w):
    return x - w ** 2
def puzzle (y , z):
    return y[z :]
w = "exoticizing nor"
print (mystery (w , -3))

"""
Ans: nortic
"""
#-----------------------------------------------------
"""
Q3b. Function programming

English words that begin and end with the same letter are called "palindromic words." 
Here are some examples: *Civic*, *noon*, *rotor*. Write a predicate function is_palindromic_word that returns True 
if the word starts and ends with the same letter (ignoring upper or lower case).
Thus,

is_palindromic_word("Noon")
or 
is_palindromic_word("noon")

both should return True. Conversely,

is_palindromic_word("soon")

should return False.

"""
#------------------------------------
#My solution to Q3b
def is_palindromic_word(word):
    """Returns True if the word contains more than one instance of any letter 
    and the start and end letter of the word are the same irrespective of upper or lower case.

    Arguments:
        word (str): The word to check
    Returns:
        (bool): True or False depending on if the word meets the condition
    """
    # Your turn!
    letter = []
    for i in word:
        word=word.lower()
        i = i.lower()
        if i in letter and word.startswith(i) and word.endswith(i):
            return True
        letter += i
    return False
if __name__ == "__main__":
    print(is_palindromic_word("data"))
    #fac = largest_factor(36)
    #print(fac)
# -----------------------------------------------------------

"""
Q4:
Nowadays, people use emojis to communication in so many ways. This program try to create an emoji that communicate two main things. (1) a smily face and (2) an amazing face.
You are already provided with the code that draw the face as shown in Figure A.


Your task is to write an interactive program that twist the mouth-shape of the emoji to communicate the two scenarios mentioned here.
Specifically, you are to write two callback functions to achieve these tasks using the GArc or GOval objects,


(i). Write a callback function makes_me_smile with a click event that will add a smiley mouth-shape to the face as shown in Figure B.


(ii). write a callback function make_me_amaze with a double click event that will add an amazing mouth-shape to the face as shown in Figure 3
"""

from pgl import GWindow,GOval, GArc

def emoji():
    gw = GWindow(400, 400)
  
    def face(): #Creating the face of the emogi 
        head = GOval(20, 20, 360, 360)
        head.set_fill_color("yellow")
        head.set_filled(True)
        return gw.add(head)
    
    def righteye(): #Creating the right hand eye of the emogi 
        reye = GOval(110, 100, 40, 40)
        reye.set_filled(True)
        gw.add(reye)
        rdoteye = GOval(120, 110, 20,20)
        rdoteye.set_fill_color("white")
        rdoteye.set_filled(True)
        return gw.add(rdoteye)
    
    def lefteye(): #Creating the left hand eye of the emogi 
        leye = GOval(250, 100, 40, 40)
        leye.set_filled(True)
        gw.add(leye)
        ldoteye = GOval(260, 110, 20,20)
        ldoteye.set_fill_color("white")
        ldoteye.set_filled(True)
        gw.add(ldoteye)
        return gw
    
    def make_me_smile(event): #Your smile mouth-shape callback function  
        """
        Type in your code in this bluck
        """
        """
        smile = GArc(150, 250, 110, 50, 180, 180)
        smile.set_line_width(4)
        gw.add(smile)
        return gw
    gw.add_event_listener("click", make_me_smile) 
    """
    
    def make_me_amaze(event): #Your amazing mouth-shape callback function  
        """
        Type in your code in this bluck
        """
        """
        amaze = GArc(150, 250, 110, 50, 0, 180)
        amaze.set_line_width(4)
        gw.add(amaze)
        return gw
    gw.add_event_listener("dblclick", make_me_amaze)
    """
    
    #Instantiating the objects
    face()
    righteye()
    lefteye()

if __name__ == "__main__":
    emoji() # Runing theh emogi program

    # ----------------------------------------------------
"""
Q5.
Consider the data structure below which somewhat indicates the calendar for the remaining weeks in the year. 
"""

data = [
        {'week': 50,
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
    {  'week': 51,
        'days': {
            'Mon': "Workday",
            'Tue': "Workday",
            'Wed': "Workday",
            'Thu': "Workday",
            'Fri': "Workday",
            'Sat': "Weekend",
            'Sun': "Christmas eve"
        }
    },
    {  'week': 52,
        'days': {
            'Mon': "Christmas holiday",
            'Tue': "Boxing day holiday",
            'Wed': "Workday",
            'Thu': "Workday",
            'Fri': "Workday",
            'Sat': "Weekend",
            'Sun': "New year eve"
        }
    }
]
"""Question A: write python expression to select and print only the value with 'Christmas holiday'."""

# ANS: print(data[2]['days']['Mon'])

# --------------------------------------------------------

""" Question B: Write a python program to format the data and print to terminal as shown in the example below

Week: 50 
--------
Mon: Workday
Tue: Workday
Wed: Workday
Thu: Workday
Fri: Workday
Sat: Weekend
Sun: Weekend

Week: 51 
--------
Mon: Workday
Tue: Workday
Wed: Workday
Thu: Workday
Fri: Workday
Sat: Weekend
Sun: Christmas eve

Week: 52 
--------
Mon: Christmas holiday
Tue: Boxing day holiday
Wed: Workday
Thu: Workday
Fri: Workday
Sat: Weekend
Sun: New year eve

"""
# My solution to question B
for i in range(len(data)):
    print(f"Week: {data[i]['week']} \n--------")
    for x,y in data[i]['days'].items():
        print(f'{x}: {y}')
    print()

# ----------------------------------------------------------------

"""Question C: Write python program to store the formatted data structure in question C into 
the local computer memory with filename 'End_of_year_calendar.txt' """

#My solution to question C
with open("End_of_year_calendar.txt", "w") as fh:
            for i in range(len(data)):
                fh.write(f"Week: {data[i]['week']} \n--------\n")
                for x,y in data[i]['days'].items():
                    fh.write(f'{x}: {y}\n')
                fh.write("\n")
