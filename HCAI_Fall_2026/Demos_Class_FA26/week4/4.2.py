import numpy as np
import time
print("=" * 60)
print("Performance Comparison: Python Lists vs NumPy Arrays")
print("=" * 60)

# Size of the data
size = 10000000
print(f"\nData size: {size:,} elements\n")

# ============================================
# Test 1: Squaring elements
# ============================================
# print("Test 1: Squaring all elements")
# print("-" * 40)

# # Python list
my_list = list(range(size))
start_time = time.time()
squared_list = [x**2 for x in my_list]
list_time = time.time() - start_time
print(f"List comprehension: {list_time:.4f} seconds")

# NumPy array
np_array = np.arange(size)
start_time = time.time()
squared_np_array = np_array**2
np_time = time.time() - start_time
print(f"NumPy vectorization: {np_time:.4f} seconds")
print(f"Speedup: {list_time/np_time:.2f}x faster\n")

# ============================================
# Test 2: Sum of elements
# ============================================
print("Test 2: Sum of all elements")
print("-" * 40)

# Python list
start_time = time.time()
list_sum = sum(my_list)
list_time = time.time() - start_time
print(f"List sum(): {list_time:.4f} seconds")

# NumPy array
start_time = time.time()
np_sum = np.sum(np_array)
np_time = time.time() - start_time
print(f"NumPy sum(): {np_time:.4f} seconds")
print(f"Speedup: {list_time/np_time:.2f}x faster\n")

# ============================================
# Test 3: Element-wise multiplication
# ============================================
print("Test 3: Element-wise multiplication (a * b)")
print("-" * 40)

# Python lists
list_a = list(range(size))
list_b = list(range(size))
start_time = time.time()
result_list = [a * b for a, b in zip(list_a, list_b)]
list_time = time.time() - start_time
print(f"List comprehension: {list_time:.4f} seconds")

# NumPy arrays
np_a = np.arange(size)
np_b = np.arange(size)
start_time = time.time()
result_np = np_a * np_b
np_time = time.time() - start_time
print(f"NumPy vectorization: {np_time:.4f} seconds")
print(f"Speedup: {list_time/np_time:.2f}x faster\n")

np_a.