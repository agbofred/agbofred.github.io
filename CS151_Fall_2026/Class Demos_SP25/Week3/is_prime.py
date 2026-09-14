

def is_prime(num):
    """
    A function that takes in a number and decide if its a prime or not
    
    ALGORITHM:
        check for or loop over possible factors
        check if a factor is divisible (num % possible factor)
        if factor, then return false
        otherwise, true 
    """
    
    factor_count = 0
    for possible_factor in range(2, num):
        if num % possible_factor == 0:
            return False
        return True
    
print(is_prime(18))