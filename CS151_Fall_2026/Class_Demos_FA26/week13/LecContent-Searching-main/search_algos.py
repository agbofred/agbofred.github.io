
def linear_search(target, array):
    """ Uses a linear search to find a target in an array

    Inputs:
        target (any): The element to find
        array (list[any]): The array of elements
    Returns:
        (int) the index of the found element, -1 if not found.
    """
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

def binary_search(target, array):
    """ Uses a binary search to find a target in an array

    Inputs:
        target (any): The element to find
        array (list[any]): The array of elements
    Returns:
        (int) the index of the found element, -1 if not found.
    """
    lh = 0
    rh = len(array) - 1
    while lh <= rh:
        middle = (lh + rh) // 2
        mid_val = array[middle]
        if mid_val == target:
            return middle
        elif mid_val < target:
            lh = middle + 1
        else:
            rh = middle - 1
    return -1

def jump_search(target, array):
    """ Uses a jump search to find a target in an array. Here, the size of the
    initial jumps in hard-coded to be sqrt(N).

    Inputs:
        target (any): The element to find
        array (list[any]): The array of elements
    Returns:
        (int) the index of the found element, -1 if not found.
    """
    jump_size = int(len(array) ** 0.5)
    curr_idx = 0
    while array[curr_idx] < target:
        curr_idx += jump_size
        if curr_idx >= len(array):
            return -1
    while array[curr_idx] != target:
        curr_idx -= 1
    return curr_idx



if __name__ == '__main__':
    A = list(range(401, 535))
    print(f"Salem Area code from Linear: {linear_search(503, A)}")
    print(f"Salem Area code from Binary: {binary_search(503, A)}")
    print(f"Salem Area code from Jump: {jump_search(503, A)}")
