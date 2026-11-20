import time
from search_algos import linear_search, binary_search, jump_search

def benchmark(func, data, target, runs=100):
    start = time.perf_counter()
    for _ in range(runs):
        func(data, target)
    return (time.perf_counter() - start) / runs

for n in [1000, 10000, 100000, 1000000]:
    data = list(range(n))
    target = n - 1   # worst case
    print(n,
          benchmark(linear_search,target, data),
          benchmark(jump_search, target, data),
          benchmark(binary_search, target, data))