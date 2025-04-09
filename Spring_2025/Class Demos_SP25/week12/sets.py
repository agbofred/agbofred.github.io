# D = { }
# S= set()
# S.add(100)
# S.add(200)
# K= {200, 100}
# print(( 400 in K))

digits = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }
evens = { 0, 2, 4, 6, 8 }
odds = { 1, 3, 5, 7, 9 }
primes = { 2, 3, 5, 7 }
squares = { 0, 1, 4, 9 }
s={0,1,4,9}
s.discard(9)
print(s)

#print((primes.intersection(evens)).union(odds.intersection(squares)))