from rich.traceback import install
install(show_locals=True)

def calculate_fuel(distance):
    """Computes the fuel use to travel a certain distance."""
    return distance * 0.12

def pre_flight_sequence():
    """Runs through some pre-flight checks"""
    dist = 1000
    fuel_needed = calculate_fuel(dist)
    oxygen_needed = verify_oxygen_levels(fuel_needed) 
    return fuel_needed + oxygen_needed

needs = pre_flight_sequence()

def verify_oxygen_levels(fuel):
    """Computes how much oxygen will be needed."""
    return fuel * 0.05

print(needs) # Expected 126
