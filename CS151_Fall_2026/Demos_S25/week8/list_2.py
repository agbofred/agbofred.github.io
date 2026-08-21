cool = ['blue', 'violet']
warm = ['red', 'orange']

colors = [cool, warm]
#print(colors)
other_colors = [['blue', 'violet'],
                ['red', 'orange']]

#print(colors == other_colors)
#print(colors is other_colors)

cool[0] = 'indigo'
warm = ['orange', 'yellow']

def listarray(array):
    for i in range(len(array)):
        newArr = array# add .copy()
        print(f"Element{i}=> {newArr[i]}")
        print(newArr.pop())
        
        
li = [36,8,6,5,4,5,6,0,1]  
l2= li.copy()
reversed(l2)

#print(l2)
#listarray(li)

list1 = [2,4,6,5,3]
list2 =[] #to store ele
for i in range(len(list1)):
      if list1[i]%2==0: #remove odd
            list2.append(list1[i])
            
print(list1)
print(list2)

