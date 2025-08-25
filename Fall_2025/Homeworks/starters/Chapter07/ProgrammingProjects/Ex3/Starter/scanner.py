"""
File: scanner.py
A scanner for processing languages.
"""

from tokens import Token

class Scanner(object):

    EOE = ';'        # end-of-expression
    TAB = '\t'       # tab

    def __init__(self, sourceStr):
        

    def hasNext(self):
        

    def next(self):
        

    def getFirstToken(self):
        
    
    def getNextToken(self):
        
    
    def nextChar(self):
        
    
    def skipWhiteSpace(self):
      
    
    def getInteger(self):
      


def main():
    # A simple tester program
    while True:
        sourceStr = input("Enter an expression: ")
        if sourceStr == "": break
        scanner = Scanner(sourceStr)
        while scanner.hasNext():
            print(scanner.next())

if __name__ == '__main__': 
    main()

