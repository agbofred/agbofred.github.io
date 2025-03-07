def listarray(array):
    for i in range(len(array)):
        newArr = list(array)
        print(f"Element-{i} => {newArr[i]}")
        print(newArr.pop())
        
        
li = [36,8,6,5,4,5,6,0,1]
  
li.sort()
lv = reversed(li)
print(li)
print(lv)