"""A = [
     'Fox',
     'Giraffe', 
     'Hippo'
    ]
A.append('Iguana')
A[:].reverse()
B = A
for i in A:
    if i[1]== 'G':
        A.pop()
    print(B)"""

A = [
     'Fox',
     'Giraffe', 
     'Hippo',
    ]
A.append('Iguana')
A[:].reverse()
B = A
C =[] # Create a new list C
for num  in B:
       if num[1]=='i':
           continue
       else:
            C.append(num)

print(f'this is A {A}')
print(f'this is B {B}')
print(f'this is C {C}')
