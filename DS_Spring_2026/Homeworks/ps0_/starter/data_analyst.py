########################################
# Name:
# Indicate any collaborators or tools used to assist you including AI:
# Estimated time spent (hrs):
########################################

"""
Problem 3: The Data Analyst's Toolkit (Functional Programming & Mapping)

This module demonstrates functional programming concepts using filter(), map(),
and lambda expressions to process temperature data.
"""


def process_temperatures(fahrenheit_temps):
    """
    Filters invalid temps (< -459.67°F), converts to Celsius, returns tuple.
    Use filter(), map(), and lambda expressions.
    """
    # TODO: Use filter() with lambda to remove temps < -459.67
    # TODO: Use map() with lambda to convert F to C: (F - 32) × 5/9
    # TODO: Convert result to tuple and return
    pass


def main():
    """
    Tests the temperature processing functions with sample data.
    """
    print("Data Analyst's Toolkit - Temperature Processing")
    print("=" * 60)
    print()
    
    # Sample temperature data with some erroneous readings
    raw_temps = [32.0, 68.5, -500.0, 212.0, 98.6, 0.0, -460.0, 75.3, 100.4]
    
    print(f"Original temperatures (°F): {raw_temps}")
    print()
    
    # Process temperatures
    result = process_temperatures(raw_temps)
    
    print(f"Processed temperatures (°C): {tuple(round(c, 2) for c in result)}")
    print()
    print(f"Result type: {type(result)}")
    print(f"Number of valid temperatures: {len(result)}")


if __name__ == "__main__":
    main()
