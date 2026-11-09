# evens = { 0, 2, 4, 6, 8 }
# odds = { 1, 3, 5, 7, 9 }
# primes = { 2, 3, 5, 7 }
# squares = { 0, 1, 4, 9 }
# A = primes.intersection(evens)
# B = odds.intersection(squares)
# C = A.union(B)
# print(C)

digits = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }
evens = { 0, 2, 4, 6, 8 }
odds = { 1, 3, 5, 7, 9 }
primes = { 2, 3, 5, 7 }
squares = { 0, 1, 4, 9 }

print(evens.union(squares))
print(odds.intersection(primes))
print(primes.difference(evens))
print(odds.symmetric_difference(squares))