#SOLUTION to Problem 2

def divisible_by_six_or_seven(lower, upper):
    c =0
    for i in range(lower,upper+1):
        if((i%6==0 or i%7==0) and not(i%6==0 and i%7==0)):
            print(i)
            c +=1
    return c

count = divisible_by_six_or_seven(40,60)
print(count)


#SOLUTION to Problem 2
def total_shaded_area(A, B, d):
    # Calculate the areas of the squares
    area_A = A**2
    area_B = B**2
    
    # Calculate the overlap area
    overlap_area = d**2
    
    # Calculate the total shaded area
    total_area = area_A + area_B - overlap_area
    
    return total_area

# Example usage:
A = 5
B = 7
d = 3
print(total_shaded_area(A, B,d))

