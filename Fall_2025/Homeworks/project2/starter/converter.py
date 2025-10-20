########################################
# Your Name:
# Indicate any collaborators or tools used to assist you including AI:
# Estimated time spent (hrs):
########################################
"""
File: converter.py
Defines a class that converts infix expressions to postfix form.
"""

from mytoken import Token
from scanner import Scanner
from arraystack import ArrayStack

class IFToPFConverter(object):

    def __init__(self, scanner):
        self.scanner = scanner

    def convert(self):
        """Returns a list of tokens that represent the postfix
        form.  Assumes that the infix expression is syntactically correct"""
        
   

def main():
    while True:
        sourceStr = input("Enter an infix expression: ")
        if sourceStr == "": break
        else:
            converter = IFToPFConverter(Scanner(sourceStr))
            postfix = converter.convert()
            print("Postfix:", end = " ")
            for token in postfix:
                print(token, end = " ")
            print()

if __name__ == "__main__":
    main()


