A = [1, 2, 3, 4]
B = A[:]
A.append(56)
A[0] = 99

print(B)
print(A)
