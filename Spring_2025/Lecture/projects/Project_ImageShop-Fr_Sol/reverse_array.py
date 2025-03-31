def change_array_row():
    array= [
        [1,2,3,4,5,6],
        [7,8,9,10,11,13],
        
        ]
    print(f"Array before ->{array}")
    row = len(array)
    col = len(array[0])
    new_arr= [[0 for _ in range(row)] for _ in range(col)]
    print(new_arr)
    for i in range(col):
        for j in range(row):
            new_arr[i][j] = array[j][i]
    print(f"Array After ->{new_arr}")      
    #return new_array
print(change_array_row())