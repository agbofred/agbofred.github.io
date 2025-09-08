"""
File: expressiontree.py
Project 10.7  Completes the node classes for expression trees.

Defines nodes for expression trees.
"""

from tokens import Token

class LeafNode(object):
    """Represents an integer."""

    # Your code here

class InteriorNode(object):
    """Represents an operator and its two operands."""

    # your code here 

def main():
    a = LeafNode(4)
    b = InteriorNode(Token('+'), LeafNode(2), LeafNode(3))
    c = InteriorNode(Token('*'), a, b)
    c = InteriorNode(Token('-'), c, b) 
    print("Expect ((4 * (2 + 3) - (2 + 3)):", c.infix())
    print("Expect - * 4 + 2 3 + 2 3       :", c.prefix())
    print("Expect 4 2 3 + * 2 3 + -       :", c.postfix())
    print("Expect 15                      :", c.value())

if __name__ == "__main__":
    main()




