"""
File: scanner.py
A scanner for processing languages.
Modified version of scanner used in Chapter 7.
Includes methods get and stringUpToCurrentToken.
get returns Token.EOE when the string has been scanned.
No precondition on next.
"""

from tokens import Token

class Scanner(object):

# Your code here

def main():
    # A simple tester program
    while True:
        sourceStr = input("Enter an expression: ")
        if sourceStr == "": break
        scanner = Scanner(sourceStr)
        token = scanner.get()
        while token.getType() != Token.EOE:
            print(token)
            scanner.next()
            token = scanner.get()

if __name__ == '__main__': 
    main()

