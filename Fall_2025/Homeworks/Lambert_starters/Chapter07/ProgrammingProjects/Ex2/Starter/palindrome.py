"""
File: palindrome.py
Project 7.2

"""

from arraystack import ArrayStack

def isPalindrome(string):          
    """Returns True if string is a palindrome
    or False otherwise."""
   

def main():
    while True:
        string = input("Enter a string or Return to quit: ")
        if string == "":
            break
        elif isPalindrome(string):
            print("It's a palindrome")
        else:
            print("It's not a palindrome")

if __name__ == '__main__': 
    main()
