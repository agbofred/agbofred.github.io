'''
For the magic square problem
'''

def is_magic_square(array: list[list[int]]) -> bool:
    nrows = len(array)
    ncols = len(array[0])

    if nrows != ncols: #not a square array
        return False

    magic_num = sum(array[0])

    # Check rows
    for row in array:
        if sum(row) != magic_num:
            return False

    # Check cols
    for c in range(ncols):
        col = [row[c] for row in array]
        if sum(col) != magic_num:
            return False

    # Check diagonals
    d1 = [array[i][i] for i in range(nrows)]
    d2 = [array[i][ncols-1-i] for i in range(nrows)]
    if sum(d1) != magic_num or sum(d2) != magic_num:
        return False

    return True


def test_magic_square():
    sq1 = [[16,3,2,13],[5,10,11,8],[9,6,7,12],[4,15,14,1]]
    sq2 = [[8,1,6],[3,5,7],[4,9,2]]
    sq3 = [[1,23,16,4,21],[15,14,7,18,11],[24,17,13,9,2],[20,8,19,12,6],[5,3,10,22,25]]
    sq4 = [[1,2,3],[4,5,6],[7,8,9]]
    sq5 = [[8,1,6,10],[3,5,7,11],[4,9,2,12]]

    assert is_magic_square(sq1)
    assert is_magic_square(sq2)
    assert is_magic_square(sq3)
    assert not is_magic_square(sq4)
    assert not is_magic_square(sq5)


if __name__ == '__main__':
    test_magic_square()
