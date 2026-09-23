import random


max_value =0
for i in range(10000):
    current_sum = 0
    for r in range(5):
        current_sum += random.randint(1, 100)
    if current_sum > max_value:
        max_value = current_sum
        
print(max_value)
