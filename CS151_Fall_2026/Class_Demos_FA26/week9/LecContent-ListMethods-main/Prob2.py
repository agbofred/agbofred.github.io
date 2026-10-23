from raw_data import DATA

def clean_with_append(data_list):
	"""Takes the given data_list and returns a list without any dirty values.

	Uses looping and append.

	Args:
		data_list (list[str]): The original list of strings
	Returns:
		list[int]: The numeric values from the original list as integers
	"""
	new_data =[]
	for i in data_list:
		if i.isnumeric():
			new_data.append(int(i))
	return new_data
      


def clean_with_comprehension(data_list):
	"""Takes the given data_list and returns a list without any dirty values.

	Uses list comprehension

	Args:
		data_list (list[str]): The original list of strings
	Returns:
		list[int]: The numeric values from the original list as integers
	"""
	return [i for i in data_list if i.isnumeric()]


def clean_in_place(data_list):
	"""Takes the given data_list and removes all dirty values from it in-place.

	Also converts legitimate numbers to integers in-place.

	Args:
		data_list (list[str]): The original list
	Returns:
		None
	"""
	for i in range(len(data_list)):
		elem = data_list[i]
		if elem.isdigit():
			data_list[i] = int(elem)
		else:
			data_list[i] = None
	while None in data_list:
		data_list.remove(None)



def count_em(clean_data_list):
	"""Counts the occurrances of each number, and returns a tabulated array of those
	counted values.

	Args:
		clean_data_list (list[int]): The list of integers
	Returns:
		list[int]: The tabulated counts
	"""
	# count = [0]*26
	count = [0 for i in range(26)]
	print(count)
	for i in clean_data_list:
		count[i] += 1
	return count



def test_clean_with_append():
	"""A function to help test Part A"""
	clean = clean_with_append(DATA)
	assert all([isinstance(x, int) for x in clean]) # All integers
	assert sum(clean) == 4740 # Correct total sum

def test_clean_with_comprehension():
	"""A function to help test Part B"""
	clean_og = clean_with_append(DATA)
	clean = clean_with_comprehension(DATA)
	assert all([isinstance(x, int) for x in clean]) # All integers
	assert sum(clean) == 4740 # Correc total sum
	assert clean == clean_og # Equals what you got from Part A

def test_clean_in_place():
	"""A function to help test Part C"""
	data = DATA.copy()
	before = id(data)
	clean_in_place(data)
	after = id(data)
	assert all([isinstance(x, int) for x in data]) # All integers
	assert sum(data) == 4740 # Correct sum
	assert before == after # Id has not changed

def test_count_em():
	"""A function to help test Part D"""
	clean = clean_with_append(DATA)
	counts = count_em(clean)
	assert counts[0] == 17 # Should be 17 0's
	assert counts[25] == 15 # Should be 15 25's
	assert sum(counts) == 380 # Num of clean values
	assert min(counts) == 8 # Smallest amount
	assert min(counts) == counts[3] # Smallest amount of 3s

if __name__ == '__main__':
	# Part A
	# print(clean_with_append(DATA))

	# Part B
	# print(clean_with_comprehension(DATA))

	# Part C
	# data = DATA.copy()
	# clean_in_place(data)
	# print(data)

	# Part D
	print(count_em(clean_with_append(DATA)))
