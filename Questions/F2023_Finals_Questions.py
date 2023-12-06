"""
Question 1a.

The Kilburn’s algorithm for finding the factor of a number 
using brute-force strategy is shown on the right. 
What would be the printed output of the code below?
"""
def largest_factor(n):
    factor = n - 1
    while n % factor != 0:
        factor -= 1
    return factor

#if __name__ == '__main__':
    

    """
    Options: B
    --------
    A= 12
    B= 18
    C= 16
    D= 9  
    """
# -----------------------------------------------
"""
Q1b:
What will be printed to the terminal if the following probram 
execute?
"""
# Answer is ((2,5,2,5),'b') >>>>>Note! if line 34 is  a concatenation say C = B + ('b', ), then it returns error of not able to concetnate string and tuple
A = (2, 5, )
B = (2*A, ('a', ) )
C = B ,('b', 'c', 'd')
D = tuple()
print(C)
for v in C[:3]:
    D += v[:1]
print(D)

"""
2a. If the ASCII code of charater 'G' is 47X in hexadecimal, 
    what is the base 10 integer value of 'G'?
ANS:

2b. If ASCII code of character 'g' is 67X in hexadecimal, 
    what will be the octal representation value of 'g' in base 8?


ANS: 
"""
#-----------------------------------------------
"""
Q3a. Programming function

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
#My solution to Q3a
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

Q3b.

"""

"""
Nowadays, people use emogi to communication in so many ways. This program try to create an emogi that communicate two main things. (1) a smilly face and (2) an amazing face.
You are already provided with the code that draw the face. Your task is to write an interactive 
program that twist the mouth-shape of the emogi to communicate the two scenarios mentioned here. 
Specifically, you are ro write two callback functions to achieve these tasks using the GArc or GOval,
1. write a callback function makes_me_smile with a click event that will add a smilling mouth-shape to the face as shown in Figure 2. 
2. write a callback and make_me_amaze with a double click event that will add an amazing mouth-shape to the face as shown in Figure 3
"""

from pgl import GWindow,GOval, GLine, GArc

def emogi():
    gw = GWindow(400, 400)
    #
    #Creating the face of the emogi 
    
    def face():
        head = GOval(20, 20, 360, 360)
        head.set_fill_color("yellow")
        head.set_filled(True)
        return gw.add(head)
    
    #Creating the right hand eye of the emogi 
    
    def righteye():
        reye = GOval(110, 100, 40, 40)
        reye.set_filled(True)
        gw.add(reye)
        rdoteye = GOval(120, 110, 20,20)
        rdoteye.set_fill_color("white")
        rdoteye.set_filled(True)
        return gw.add(rdoteye)
    
    #Creating the left hand eye of the emogi 
    
    def lefteye():
        leye = GOval(250, 100, 40, 40)
        leye.set_filled(True)
        gw.add(leye)
        ldoteye = GOval(260, 110, 20,20)
        ldoteye.set_fill_color("white")
        ldoteye.set_filled(True)
        gw.add(ldoteye)
        return gw
    
    #Your smile mouth-shape callback function  
    
    def makes_me_smile(event):
        smile = GArc(150, 250, 110, 50, 180, 180)
        smile.set_line_width(4)
        gw.add(smile)
        return gw
    gw.add_event_listener("click", makes_me_smile) 
    
    #Your amazing mouth-shape callback function  
    
    def make_me_amaze(event):
        amaze = GArc(150, 250, 110, 50, 0, 180)
        amaze.set_line_width(4)
        gw.add(amaze)
        return gw
    gw.add_event_listener("dblclick", make_me_amaze)
    
    #Instantiating the objects
    face()
    righteye()
    lefteye()


if __name__ == "__main__":
    emogi() # Runing theh emogi program

    # ----------------------------------------------------


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
"""Question A: to select and print only the Christmas Holiday..."""

print(data[2]['days']['Mon'])


""" Question B: to format the data and print to terminal as shown in the example"""
for i in range(len(data)):
    print(f"Week: {data[i]['week']} \n--------")
    for x,y in data[i]['days'].items():
        print(f'{x}: {y}')
    print()

"Question C: to save this information to a file called End_of_year_calendar.txt"
with open("End_of_year_calendar.txt", "w") as fh:
            for i in range(len(data)):
                fh.write(f"Week: {data[i]['week']} \n--------\n")
                for x,y in data[i]['days'].items():
                    fh.write(f'{x}: {y}\n')
                fh.write("\n")
