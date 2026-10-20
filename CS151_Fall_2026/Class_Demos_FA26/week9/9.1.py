A = [
     'Fox',
     'Giraffe', 
     'Hippo'
    ]
A.append('Iguana')
B = A[:]

for anim in range(len(A)):
    if B[anim][1] == 'i':
        B.remove(B[anim])
print(A)