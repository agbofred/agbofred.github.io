import math

wavelength =  400 * 10 ** -9 # meters
temperature = 1000 #kelvin

#Define the constants 
C = 3E8
H = 6.62E-34
KB = 1.38E-23

fraction_1 = 2 * H * C ** 2 / wavelength ** 5
fraction_2 = H * C / (wavelength * KB * temperature)

plank = fraction_1 * (1 / (math.e ** fraction_2 - 1))

print(plank)