def is_magic_square(array):
    """
    Predicate function to determine whether a two-dimensional array of integers
    creates a magic square by checking that the sum of all the rows, columns, and
    both diagonals is equal.

    Inputs:
        array (list of lists of integers): the array to evaluate
    Outputs:
        (boolean): whether the array forms a magic square
    """
    
    sums = []   # Initializes an empty list used to store the sums of each row, column, and diagonal                               

    number = 0
    for rows in range(len(array)):           # Checks each of the rows going horizontally
        for columns in range(len(array)):
            number += array[rows][columns]
        sums.append(number)
        number = 0

    number = 0
    for columns in range(len(array)):        # Checks each of the columns going vertically
        for rows in range(len(array)):
            number += array[rows][columns] 
        sums.append(number)
        number = 0

    number = 0
    for rows in range(len(array)):               # Checks the diagonals going top left to bottom right 
        for columns in range(len(array)):
            if rows == columns:
                number += array[rows][columns]
    sums.append(number)

    number = 0
    for rows in range(1, len(array) + 1):                # Checks the diagonals going top right to bottom left
        for columns in range(-1, -len(array) - 1, -1):
            if rows == -columns:
                number += array[rows - 1][columns]
    sums.append(number)

    for check in range(len(sums)):   # Checks every value in the sum list against the first value 
        if sums[0] != sums[check]:   # If one of them is not equal
            return False             # The square in question is not magic
    return True                      # If they are all equal, the square is magic
    
if __name__ == '__main__':
    # Test other squares as well!
    small = [[8,1,6],[3,5,7],[4,9,2]]
    medium = [[6,3,10,15],[9,16,5,4],[7,2,11,14],[12,13,8,1]]
    print(is_magic_square(small))
    print(is_magic_square(medium))