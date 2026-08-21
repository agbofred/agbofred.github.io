Z= {-2,3,4,55,6}
Z.add(34)
Y = {5,3,5,7}

digits = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }
evens = { 0, 2, 4, 6, 8 }
odds = { 1, 3, 5, 7, 9 }
primes = { 2, 3, 5, 7 }
squares = { 0, 1, 4, 9 }

Setcomp ={ x for x in range(0,100,3) if x % 2 !=0 }
Z.discard(-2)

print(Z)

# s= set()
# z= {}
# s.add(45)
# s.add(55)
# k ={10,22}
# s=k
# print(10 in s )
digits = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }
evens = { 0, 2, 4, 6, 8 }
odds = { 1, 3, 5, 7, 9 }
primes = { 2, 3, 5, 7 }
squares = { 0, 1, 4, 9 }
#print((primes&evens)|(odds&squares))
squares.discard(44)
print(squares)