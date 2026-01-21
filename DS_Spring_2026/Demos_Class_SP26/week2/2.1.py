def indexOfMin(lyst):
    """Returns the index of the minimum item."""
    minIndex = 0
    currentIndex = 1
    while currentIndex < len(lyst):
        if lyst[currentIndex] < lyst[minIndex]:
            minIndex = currentIndex
        currentIndex += 1
    return minIndex

if __name__ == "__main__":
    l =[3,4,2,4,5,6,1,2,5]
    min = indexOfMin(l)
    print(min)