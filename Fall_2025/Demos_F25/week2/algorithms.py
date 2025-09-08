# def bubbleSort(lyst):
#     for i in range(len(lyst)-1, 0,-1):
#         for j in range(i):
#             if lyst[j]>lyst[j]:
#                 lyst[j], lyst[j+1] == lyst[j+1], lyst[j]
#     return lyst
                
def bubble(lyst):
    for last in range(len(lyst)-1, 0, -1):
        for i in range(last):
            if lyst[i] > lyst[i+1]:
                lyst[i], lyst[i+1]= lyst[i+1], lyst[i]
    return lyst
                                
print(bubble([2,5,3,1,0]))
