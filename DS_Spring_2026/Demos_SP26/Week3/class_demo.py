for n in range(40):
    print(f"{n}--> {n**4} ----------- {2**n}")
    
    
    
#FIbonnacci

def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1) + fib(n-2)
for i in range(10):  
    print(fib(i))
    


# Recursive function to reverse string or list
def reverseString(s):
    
    if len(s) ==1:
        return s
        
    else:
        return reverseString(s[1:]) + s[:1] # This will reverse list argument
        #return reverseString(s[1:]) + s[0] # This will reverse string argument
print(reverseString([4,4,5,3]))

# Recursive function to find index of a number in a given list
def recursiveFind(x, num, index=0):
    if len(num)==0 or index >= len(num):
        return -1
    if num[index]== x:
        return index
    return recursiveFind(x, num, index + 1)
cool=[4,6,3,4,6,10]    
print(recursiveFind(11, cool))



def checkPowerofN(n):
    print(f"{'#':<10}  {'Problem size':<20} {'Computation':>10}")
    print(f"{'----------'}{'------------':<20} {'---------':>10}")
    for i in range (20):
        print(f"{i:<10}{i**4:<20} {2**i:>10}")
checkPowerofN(20)     
        
        