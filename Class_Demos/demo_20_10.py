A = [
     'Fox',
     'Giraffe', 
     'Hippo'
    ]
A.append('Iguana')
A[:].reverse()
B = A
for anim in B:
    if anim[1] == 'i':
        B.pop()
print(A)

li =[[3,2,1],[4,5,6],[7,8,9]]
print(li[2][1])