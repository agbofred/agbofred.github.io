def create_histogram_array(imax, list):
    table = [0]*imax
    [[table [i]+1 for i in range(imax)] for item in range(len(list)) if i == list[item]]
    print(table)             
    return table 

    
    
    
    # for i in range(imax):
    #     for item in range(len(list)):
    #         if i == list[item]:
    #             table[i] += 1
    # return table 

print(create_histogram_array(5,[1, 0, 3, 2, 4, 2, 2, 1, 3, 0]))