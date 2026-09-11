def thermo_contro(current_temp, target_temp):
    if abs(current_temp - target_temp) < 5:
        print("Off")
    elif current_temp < target_temp:
        print("Heating")
    else: 
        print("Cooling")
    if abs(current_temp - target_temp) > 25:
        print("Warming High Load!")
        
        
#thermo_contro(23, 50)

def interger_factors(n):
    """This program will output all the factors of a number and the count of those numbers"""
    possible_factor = 1
    count = 0
    while possible_factor <= n:
        if n % possible_factor == 0:
            count += 1
            print(possible_factor)
        possible_factor += 1
    return count


print(interger_factors(45))
        