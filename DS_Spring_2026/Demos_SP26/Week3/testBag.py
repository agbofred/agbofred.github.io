from newbag import Bag


def test_bag():
    bag = Bag()
    # Test add
    bag.add("apple")
    bag.add("banana")
    bag.add("apple")
    assert bag.count("apple") == 2, "Should count two apples"
    assert bag.count("banana") == 1, "Should count one banana"
    # Test __repr__
    actual = repr(bag)
    expected1 = "Bag([apple, banana, apple])"
    expected2 = "Bag([banana, apple, apple])"
    expected3 = "Bag([apple, apple, banana])"
    assert actual == expected1 or actual == expected2 or actual == expected3, f"Expected {expected1} or {expected2} or {expected3}, got {actual}"
    # expected = "Bag([apple, banana, apple])"
    # assert repr(bag) == expected, f"Expected {expected}, got {repr(bag)}"
    #print("__repr__ test passed!")
    # Test remove
    bag.remove("apple")
    assert bag.count("apple") == 1, "Should count one apple after removal"
    # Test contains
    assert bag.contains("banana"), "Bag should contain banana"
    assert not bag.contains("orange"), "Bag should not contain orange"
    # Test length
    assert bag.length() == 2, "Bag should have two items"
    # Test iteration
    items = bag.__iter__()
    assert sorted(items) == sorted(["apple", "banana"]), "Bag should have apple and banana"
    print("All tests passed!")
if __name__ == "__main__":
    test_bag()