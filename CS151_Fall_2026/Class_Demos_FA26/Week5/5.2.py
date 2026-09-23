import random

max_num = 0

for i in range(10000):
    sum= 0
    for k in range(5):
        sum += random.randint(1, 100) # We could keep the values in the list and sum all [2,5,10,99,4]
    if sum > max_num:
         max_num = sum
         
print(max_num)