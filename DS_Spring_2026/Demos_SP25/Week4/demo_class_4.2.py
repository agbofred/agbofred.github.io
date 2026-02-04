import time

# Create a large list of integers
my_list = list(range(10000000))

# Time the operation
start_time = time.time()

# Square each element using a list comprehension
squared_list = [x**2 for x in my_list]

list_time = time.time() - start_time
#print (squared_list)
print(f"List comprehension time: {list_time:.4f} seconds")

import numpy as np
import time

# Create a large NumPy array
large_np_array = np.arange(10000000)

# Time the NumPy operation
start_time = time.time()

# Perform the vectorized operation
squared_np_array = large_np_array**2

np_time = time.time() - start_time
print(f"NumPy vectorization time: {np_time:.4f} seconds")

# Compare with our previous result
# List time was ~ 2.0 seconds
#print("NumPy is orders of magnitude faster!")

darray = np.zeros((3,5))
darray[0,:] = 2
darray[:,2] = 5
darray[1,:] = 10

# Impact of vectorization
darray = darray**2


print(darray)
print(f"Average of the elements : {darray.mean()}")
print(f"Sum of the elements (rows) : {darray.sum(axis=1)}")
print(f"Sum of the elements (col) : {darray.sum(axis=0)}")



##################################################################