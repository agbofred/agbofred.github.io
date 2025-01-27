def count_letters(letter, string):
    count = 0
    for character in string:
        if character == letter:
            count += 1
    return count

def test_count_letters():
    """ Runs several tests on the function count_letters """
    assert count_letters("a", "banana") == 3

if __name__ =='__main__':
    test_count_letters()
    print(count_letters("W","willamette"))