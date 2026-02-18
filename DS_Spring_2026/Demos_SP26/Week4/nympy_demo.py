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
print("NumPy is orders of magnitude faster!")
