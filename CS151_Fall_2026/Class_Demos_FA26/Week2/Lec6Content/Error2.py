from rich.traceback import install
install(show_locals=True)
from math import pi

def mass_of_sphere(radius, density):
    """Computes the mass of a sphere of certain size and density """
    volume = 4 / 3 * pi * radius ** 3
    print(density * volume)


R1 = 10
rho1 = 0.1
m1 = mass_of_sphere(R1, rho1)

R2 = 13
rho2 = 1.2
m2 = mass_of_sphere(R2, rho2)

print(m1 + m2) # Expected result is 11462.2

