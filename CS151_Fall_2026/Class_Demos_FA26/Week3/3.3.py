biggest = 0
for i in range(2, 8, 2):
    for j in range(10, -1, -5):
        if i * j > biggest:
            biggest = i * j
print(biggest)