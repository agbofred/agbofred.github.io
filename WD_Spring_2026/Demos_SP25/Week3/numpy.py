import time

# Create a large list of integers
my_list = list(range(10000000))

# Time the operation
start_time = time.time()

# Square each element using a list comprehension
squared_list = [x**2 for x in my_list]

list_time = time.time() - start_time
print(f"List comprehension time: {list_time:.4f} seconds")