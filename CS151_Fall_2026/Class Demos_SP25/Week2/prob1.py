
def c_to_f(value):
    """Celcius to Fahrenheit conversion"""
    # C= 9/5 * C + 32
    # F = 5/9 (F - 32)
    result = (9 * value/5) + 32
    return result
    
def f_to_c(value):
    """Fahrenheit to celcius conversion"""
    result = (5 / 9) * (value - 32)
    return result
    
def feet_kilo(value):
    # 1 Kilometer == 3280.84 feet
    # 3280.84 feet == 1 kilometer
    result = value / 3280.84
    return result

def kilo_feet(value):
    result = value * 3280.84
    return result

def pounds_to_grams(value):
    #1 pound == 453.6
    # 453.6 grams = 1 pound
    result = 453.6 * value
    return result
    
def grams_to_pounds(value):
    result = value / 453.6
    return result

def cups_to_litter(value):
    #1 litre = 4.22675 cups
    # 4.22675 cups = 1 litre
    result = value/4.22675
    return result

def litter_to_cups(value):
    return value * 4.22675
    # return result

if __name__ =="__main__":
    print(litter_to_cups(20))

    