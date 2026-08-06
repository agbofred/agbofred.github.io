
import numpy as np
import time

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