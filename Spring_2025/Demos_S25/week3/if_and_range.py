def grading(grade):
    if grade >= 90:
        print("A")
    elif grade >= 80:
        print("B")
    elif grade >= 70:
        print("C")
    elif grade >= 60:
        print("D")
    else:
        print("F")

if __name__== '__main__':
    grading(90)



def count_letters(letter, string):
    count = 0
    for character in string:
        if character == letter:
            count += 1
    return count

def test_count_letters():
    """ Runs several tests on the function count_letters """
    assert count_letters("z", "banana") == 0
    assert count_letters("a", "strawberry") == 1
    assert count_letters("A", "apple") == 0
    assert count_letters("e", "eerie") == 3

if __name__ =='__main__':
    test_count_letters()
    letter = count_letters("a", "elephantiasis")
    print(letter)