from rich.traceback import install
install(show_locals=True)

def sum_of_first_n_odds(N):
    """Computes the sum of the first N odd numbers"""
    num = 1
    total = 1
    for i in range(N-1):
        num += 2
        total += num
        return total


print(sum_of_first_n_odds(8)) # Expected to get 64
print(sum_of_first_n_odds(12)) # Expected to get 144
