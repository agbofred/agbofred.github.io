"""
File: fib.py
Project 3.6

Employs memoization to improve the efficiency of recursive Fibonacci.
"""

def fib(n, table):
    """Fibonacci function with a table for memoization."""
    if  :
        
    else:
        # Attempt to get values for n - 1 and n - 2
        # from the table
        # If unsuccessful, recurse and add results to
        # the table
    

def main():
    """Tests the function with some powers of 2."""
    problemSize = 2
    print("%4s%12s" % ("n", "fib"))
    for count in range(5):
        print("%4d%12d" % (problemSize, fib(problemSize, {})))
        problemSize *= 2

if __name__ == "__main__":
    main()
