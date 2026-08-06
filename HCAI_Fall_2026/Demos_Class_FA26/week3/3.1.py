def reverseString(s):
    
    #base case 
    if len(s)==1:
        return s
    # Recursive case
    else:
        return reverseString(s[1:])+ s[:1]
print(reverseString("SAMUEL Is the TA"))

def checkPowerofN(n):
    print(f"{'#':<10}  {'Problem size':<20} {'Computation':>10}")
    print(f"{'----------'}{'------------':<20} {'---------':>10}")
    for i in range (20):
        print(f"{i:<10}{i**4:<20} {2**i:>10}")
checkPowerofN(20)     
        