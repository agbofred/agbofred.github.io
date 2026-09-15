# My own attempt below!
def pythagorean(a,b,c):
    """
    Identify the contraints
    1. The Ordering: a < b < c (This prevents duplicate searches, like checking both a=3, b=4 and a=4, b=3).
    2. The Equation: a^2 + b^2 = c^2 (The Pythagorean theorem).
    3. The Sum: a + b + c = 1000.
    
    Reduce the Variables (Mathematical Optimization)
    1. Since a + b + c = 1000, you can rewrite c as: c=1000-a-b
    2. In Pythagorean a^2 + b^2 = (1000 - a - b)^2
    
    Establish Strict Loop Boundaries
    1. Boundaries for a: Since a < b < c, a must be strictly less than a third of the total sum.
       
        Max a < 1000/3 => a <=332
    2. Boundaries for b: b must always start at a + 1 (since a < b). 
        It must also be less than the remaining sum divided by 2.
        Max b < (1000 - a) / 2
    
    ALGORITHMS
    Algorithmic Logic With the math simplified, the programmatic blueprint looks like this:
    1. Initialize a loop for a ranging from 1 to 332.
    2. Initialize a nested loop for b ranging from (a + 1) to (1000 - a) / 2.
    3. Calculate c inside the loop: c = 1000 - a - b.
    4. Test the condition: Check if a^2 + b^2 == c^2.
        Return the result: If the condition is met,
        multiply a x b x c to get the final answer and break the loop immediately (since the problem states there is exactly one solution).
    
    """
    for a in range(1, 333):
        for b in range(a+1, int((1000 - a)/2)):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                print(a, b, c)
                return a + b + c
            
print (pythagorean(30, 200, 300))
