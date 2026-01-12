############################################################
# Name:
# Name(s) of anyone worked with:
# Est time spent (hr):
############################################################

def next_number(n):
    """ Computes the next number in the Collatz sequence. """
    if n % 2 == 1:
        return 3*n+1
    else:
        return n // 2

def count_chain(num):
    """
    For a given starting number, computes the length of the
    Collatz chain before it terminates at 1.
    """
    count = 0
    while num > 1:
        count += 1
        num = next_number(num)
    return count

def find_longest_chain(max_start_num):
    """
    Finds the number between 1 and max_start_num (inclusive)
    which results in the longest Collatz chain. Prints out 
    the result and returns the length of the longest chain.
    """
    longest = 0
    best_start = 1
    for start_num in range(1, max_start_num+1):
        length = count_chain(start_num)
        if length > longest:
            longest = length
            best_start = start_num

    print("The longest chain was", longest, "links, starting at", best_start)
    return longest


if __name__ == "__main__":
    max_num = 10000
    print(find_longest_chain(max_num))
    # print(count_chain(4))

# Start count 1 too high on 19
# flip even and odd effects on line 9
# print instead of return count on 25
# move 42 and 43 inside of for loop

