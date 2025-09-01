def bubble(lyst):
    for last in range(len(lyst)-1, 0, -1):
        for i in range(last):
            if lyst[i] > lyst[i+1]:
                lyst[i], lyst[i+1]= lyst[i+1], lyst[i]
                



def selectionsort(lyst):
    for i in range(0,len(lyst)):
        small_index =i
        for j in range(i+1,len(lyst)):
            if lyst[j] < lyst[small_index]:
                small_index = j
        lyst[i], lyst[small_index]= lyst[small_index], lyst[i]        
        
l =[34,6,77,9,10]
selectionsort(l)
print(l)

"""
Prints the running times for problem sizes that double, using a single loop.
"""
import time

problemSize = 1000
print("%12s%16s" % ("Problem Size", "Seconds"))
for count in range(10):
    start = time.time()
    # The start of the algorithm
    work = 1
    for x in range(problemSize):
        for y in range(problemSize):
            work += 1
            work -= 1
    # The end of the algorithm
    elapsed = time.time() - start
    print("%12d%16.3f" % (problemSize, elapsed))
    problemSize *= 2