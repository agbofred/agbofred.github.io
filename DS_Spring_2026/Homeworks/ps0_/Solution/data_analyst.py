########################################
# Name: Instructor Solution
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
    Uses filter() and map() with lambda expressions.
    """
    valid_temps = filter(lambda temp: temp >= -459.67, fahrenheit_temps)
    celsius_temps = map(lambda f: (f - 32) * 5 / 9, valid_temps)
    return tuple(celsius_temps)


def detailed_processing(fahrenheit_temps):
    """Processes temperatures with detailed step-by-step output."""
    print(f"Original temperatures (°F): {fahrenheit_temps}")
    print()
    
    # Step 1: Filtering
    print("Step 1: Filtering (removing invalid temperatures)")
    print(f"  Absolute zero in Fahrenheit: -459.67°F")
    valid_temps = list(filter(lambda temp: temp >= -459.67, fahrenheit_temps))
    print(f"  Valid temperatures: {valid_temps}")
    print()
    
    # Step 2: Mapping (conversion)
    print("Step 2: Mapping (Fahrenheit to Celsius)")
    print("  Using formula: C = (F - 32) × 5/9")
    celsius_temps = list(map(lambda f: (f - 32) * 5 / 9, valid_temps))
    print(f"  Converted temperatures: {[round(c, 2) for c in celsius_temps]}")
    print()
    
    # Step 3: Type conversion to tuple
    print("Step 3: Type Conversion (list to tuple)")
    result = tuple(celsius_temps)
    print(f"  Final immutable tuple: {tuple(round(c, 2) for c in result)}")
    
    return result


def main():
    """
    Tests the temperature processing functions with sample data.
    """
    print("Data Analyst's Toolkit - Temperature Processing")
    print("=" * 60)
    print()
    
    # Sample temperature data with some erroneous readings
    raw_temps = [32.0, 68.5, -500.0, 212.0, 98.6, 0.0, -460.0, 75.3, 100.4]
    
    # Process with detailed output
    result = detailed_processing(raw_temps)
    
    print()
    print("=" * 60)
    print("\nDirect processing (without detailed output):")
    result2 = process_temperatures(raw_temps)
    print(f"Result: {tuple(round(c, 2) for c in result2)}")
    
    # Demonstrate that the result is immutable
    print()
    print("Verification:")
    print(f"  Result type: {type(result)}")
    print(f"  Is tuple (immutable): {isinstance(result, tuple)}")
    print(f"  Number of valid temperatures: {len(result)}")


if __name__ == "__main__":
    main()
