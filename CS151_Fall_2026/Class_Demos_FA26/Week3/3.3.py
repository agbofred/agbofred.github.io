
def factors(num):
    """ This program finds the factors of a given number"""
    possible_factor = 1 
    count= 0
    while possible_factor<= num: # This loops throiugh from 1 to number inclusive
        if num % possible_factor == 0:
            count += 1
            print(possible_factor)
        possible_factor += 1
    return count
    
print(factors(5))




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



