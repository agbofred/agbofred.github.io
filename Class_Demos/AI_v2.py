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
    #Check if square (len = wid)
    #Check if rows add up to same #
    #Check if col add up to same #
    #Check if diags add up to same # (1st index 1st row, 2nd index 2nd row, 3rd index 3rd row, etc. & -1 index row 1, -2 index row 2....)
    #if all is true, return true. if any false, return false 

      
    def check_square():
        #Check if the shape is a square --> if the length of each row is equal to the height (total # of rows)
        count = 0
        for i in range(len(small)):
            if len(small) != len(small[i]):
                count += 1
        if count == 0:
         return True
        else:
            return False
    
    def check_rows():
        count1 = 0
        rows_sum = []
        for r in range(len(small)): 
            rows_list = small[r]
            # print(rows_list)
            rows_sum += [sum(rows_list)]
            # print(rows_sum)
            # print(len(rows_sum))
        for i in range(len(rows_sum)):
                if i == i+1: 
                    count1 +=1
        # print(count1)
        if count1 == 0:
            #return print("Rows are true")
            return True
  
        else:
            #return print("False")
            return False
    
    def check_cols():
        cols_list=[]
        # first_col = []
        first_col = [small[i][0] for i in range(len(small))]
        col1_sum = sum(first_col)
        second_col = [small[i][1] for i in range(len(small))]
        col2_sum = sum(second_col)
        third_col = [small[i][2] for i in range(len(small))]
        col3_sum = sum(third_col)

        if col1_sum == col2_sum and col2_sum == col3_sum:
            return True
            #print("Columns are true")
        else:
            return False
            #print("false")

        #how do I automate? small[i][r+1] ?
                
    
    #Checks if each statement is true and then moves on to the next 
    if check_square(): #is True
        print(check_rows())
        print(check_cols())


if __name__ == '__main__':
    # Test other squares as well!
    small = [[8,1,6],[3,5,7],[4,9,2]]
    is_magic_square(small)