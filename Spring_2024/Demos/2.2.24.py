def count_letters(letter, string):
		count = 0
		for character in string:
			if character == letter:
				count += 1
		return count

def test_count_letters():
	""" Runs several tests on the function count_letters """
	assert count_letters("a", "banana") == 3
	assert count_letters("a", "strawberry") == 1
	assert count_letters("A", "apple") == 0
	assert count_letters("e", "eerie") == 3

if __name__ == '__main__':
	#print(count_letters("e", "elephants ego"))
	test_count_letters()
	