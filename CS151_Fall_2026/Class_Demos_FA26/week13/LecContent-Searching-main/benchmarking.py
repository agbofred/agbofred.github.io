from search_algos import linear_search, binary_search, jump_search
import time
import random

N_ITERS = 100


def benchmark(func, target, array):
    """Measures the time it takes a search func to find the target in an array.

    Args:
        func (function): The function to test
        target (int): The target to look for
        array (list[int]): The list to search through
    Returns:
        (float): The elapsed time in seconds
    """
    start = time.perf_counter()
    execute = func(target, array)
    end = time.perf_counter()
    elapsed = end - start 
    return elapsed


def compute_avg_time(func, array):
    """Measures the average time it takes a search func to find N_ITERS targets
    in an array.

    Targets should be randomly chosen to be anywhere within the array range OR OUTSIDE IT

    Args:
        func (function): The search function to test
        array (list[int]): The list to search through
    Returns:
        (float): The average elapsed time for each benchmark
    """
    total_time = 0
    for i in range (N_ITERS):
        target = random.randint(0, len(array))
        total_time += benchmark(func, target, array)
    return total_time/N_ITERS


def sweep_of_sizes(func, size_list):
    """Measures the average time it takes a search func to find N_ITERS targets
    in sorted arrays of different sizes.

    Args:
        func (function): The search function to test
        size_list (list[int]): A list of the desired array sizes to test
    Returns:
        (your choice): Data collection holding both array size and avg time info
    """

    data =[]
    for size in size_list:
        array = [i for i in range(size)]
        avg_time = compute_avg_time(func,array)
        data.append((size, avg_time))
    return data

def display_results(res):
    """Takes the results of sweep_of_sizes and prints them to the screen in a nice
    aligned table.

    Args:
        res (your choice): The results from sweep_of_sizes
    Returns:
        None
    """



def test_benchmark(func):
    alist = list(range(10))
    out = benchmark(func, 15, alist)
    print(
        f"{func.__name__} took {out} seconds to find 15 in the list of {len(alist)} elements"
    )


def test_compute_avg_time(func):
    alist = list(range(10))
    avg_out = compute_avg_time(func, alist)
    print(
        f"{func.__name__} took an average of {avg_out} seconds to find a target in the list of {len(alist)} elements"
    )


def test_sweep_of_sizes(func):
    sizes = [10**x for x in range(1, 5)]
    res = sweep_of_sizes(func, sizes)
    print(res)


def test_display_results(func):
    sizes = [10**x for x in range(1, 7)]
    res = sweep_of_sizes(func, sizes)
    display_results(res)


if __name__ == "__main__":
    curr = linear_search #You can change this to the other search functions if you want!
    # test_benchmark(curr)
    # test_compute_avg_time(curr)
    test_sweep_of_sizes(curr)
    # test_display_results(curr)
