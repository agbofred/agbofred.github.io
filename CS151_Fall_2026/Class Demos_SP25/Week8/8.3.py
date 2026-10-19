A = [
     'Fox',
     'Giraffe', 
     'Hippo'
    ]
A.append('Iguana')
B = A[:]
for anim in A:
    if anim[1] == 'i':
        B.remove(anim)
        print(anim)
print(B, A)