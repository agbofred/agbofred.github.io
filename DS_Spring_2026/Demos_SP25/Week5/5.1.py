from arrays import Array
from node import Node

array = Array(10)
for i in range(10): 
    array[i] = i
    
print(array)

head = None
i = len(array) - 1
while i >= 0:
    head = Node(array[i], head)
    i -= 1
    