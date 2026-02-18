"""
File: test_arraysortedbag.py
A comprehensive test program for ArraySortedBag implementation.
"""

from arraysortedbag import ArraySortedBag

def test_arraysortedbag():
    """Tests the ArraySortedBag class with various operations."""
    
    print("=" * 60)
    print("Testing ArraySortedBag Implementation")
    print("=" * 60)
    
    # Test 1: Creating an empty sorted bag
    print("\n1. Creating an empty sorted bag:")
    bag1 = ArraySortedBag()
    print(f"   Empty bag: {bag1}")
    print(f"   Is empty: {bag1.isEmpty()}")
    print(f"   Length: {len(bag1)}")
    
    # Test 2: Adding items (should maintain sorted order)
    print("\n2. Adding items [5, 2, 8, 1, 9, 3]:")
    items = [5, 2, 8, 1, 9, 3]
    for item in items:
        bag1.add(item)
    print(f"   Sorted bag: {bag1}")
    print(f"   Length: {len(bag1)}")
    
    # Test 3: Testing iteration (should be in sorted order)
    print("\n3. Iterating through the bag:")
    print("   Items: ", end="")
    for item in bag1:
        print(item, end=" ")
    print()
    
    # Test 4: Testing __contains__ with binary search
    print("\n4. Testing membership (binary search):")
    print(f"   5 in bag: {5 in bag1}")
    print(f"   7 in bag: {7 in bag1}")
    print(f"   1 in bag: {1 in bag1}")
    print(f"   10 in bag: {10 in bag1}")
    
    # Test 5: Creating bag from a collection
    print("\n5. Creating bag from list [15, 10, 20, 5, 25]:")
    bag2 = ArraySortedBag([15, 10, 20, 5, 25])
    print(f"   Sorted bag: {bag2}")
    
    # Test 6: Testing concatenation (+)
    print("\n6. Concatenating two bags (bag1 + bag2):")
    bag3 = bag1 + bag2
    print(f"   bag1: {bag1}")
    print(f"   bag2: {bag2}")
    print(f"   Result: {bag3}")
    print(f"   Length: {len(bag3)}")
    
    # Test 7: Testing equality
    print("\n7. Testing equality:")
    bag4 = ArraySortedBag([1, 2, 3, 5, 8, 9])
    bag5 = ArraySortedBag([9, 3, 1, 8, 2, 5])  # Same items, different order
    print(f"   bag4: {bag4}")
    print(f"   bag5: {bag5}")
    print(f"   bag4 == bag5: {bag4 == bag5}")
    print(f"   bag1 == bag4: {bag1 == bag4}")
    print(f"   bag4 is bag5: {bag4 is bag5}")
    
    # Test 8: Testing count
    print("\n8. Testing count:")
    bag6 = ArraySortedBag([1, 2, 2, 3, 3, 3, 4])
    print(f"   Bag: {bag6}")
    print(f"   Count of 2: {bag6.count(2)}")
    print(f"   Count of 3: {bag6.count(3)}")
    print(f"   Count of 5: {bag6.count(5)}")
    
    # Test 9: Testing remove
    print("\n9. Testing remove:")
    print(f"   Before remove: {bag1}")
    bag1.remove(5)
    print(f"   After removing 5: {bag1}")
    bag1.remove(1)
    print(f"   After removing 1: {bag1}")
    
    # Test 10: Testing clear
    print("\n10. Testing clear:")
    bag_temp = ArraySortedBag([1, 2, 3, 4, 5])
    print(f"   Before clear: {bag_temp}")
    bag_temp.clear()
    print(f"   After clear: {bag_temp}")
    print(f"   Is empty: {bag_temp.isEmpty()}")
    
    # Test 11: Testing error handling
    print("\n11. Testing error handling:")
    try:
        bag1.remove(100)
        print("   ERROR: Should have raised KeyError!")
    except KeyError as e:
        print(f"   Correctly raised KeyError: {e}")
    
    # Test 12: Testing with strings
    print("\n12. Testing with strings:")
    bag_str = ArraySortedBag(['dog', 'cat', 'bird', 'fish', 'ant'])
    print(f"   String bag: {bag_str}")
    print(f"   'cat' in bag: {'cat' in bag_str}")
    print(f"   'zebra' in bag: {'zebra' in bag_str}")
    
    # Test 13: Testing with larger dataset
    print("\n13. Testing with larger dataset:")
    import random
    large_list = [random.randint(1, 100) for _ in range(20)]
    bag_large = ArraySortedBag(large_list)
    print(f"   Original list: {large_list}")
    print(f"   Sorted bag: {bag_large}")
    print(f"   Length: {len(bag_large)}")
    
    print("\n" + "=" * 60)
    print("All tests completed successfully!")
    print("=" * 60)

if __name__ == "__main__":
    test_arraysortedbag()
