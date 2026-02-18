"""This program is an OOP that tries to walk you throught the implementation of a bag"""

class Bag(object):
    # contructor method
    def __init__(self, iterable=None):
        self.collection =[]
        if iterable != None:
            self.collection=iterable
    
    # method to add without using any python methods
    def add(self, item):
        index = self.length()
        if index ==0:
            self.collection = [item]
        else:
            new_collection = [None] * (index+1)
            for i in range(index):
                new_collection[i]= self.collection[i]
            new_collection[index]= item 
            self.collection = new_collection
    
    # Manually getting the length of the items in bag    
    def length(self):
        cnt =0
        for i in self.collection:
            cnt +=1
        return cnt
        
    #Manually removing item from bag and adjusting the item     
    def remove(self, item):
        found = False
        index = -1
        
        for i in range(self.length()):
            if self.collection[i] == item :
                found = True
                index = i
                break
        if not found:
            raise ValueError("The item is not in bag")
        new_collection = [None] * (self.length() - 1)
        j= 0
        for i in range(self.length()):
            if i != index:
                new_collection[j] = self.collection[i]
                j +=1
        self.collection = new_collection
    
    #manually count the number of coocurences of an item        
    def count(self, item):
        cnt = 0
        for i in range(self.length()):
            if self.collection[i] == item:
                cnt +=1
        return cnt
                      
    # Mannually iterating over the items in the collection
    def __iter__(self):
        item_list =[]
        i=0
        while i < self.length():
            item_list.append(self.collection[i])
            i += 1
        return item_list
    
    # Manually checking is the bag contain an item 
    def contains(self, item):
        for i in range(self.length()):
            if self.collection[i]== item:
                return True
        return False
    
    def __repr__(self):
        """Return a string representation of the Bag."""
        items = []
        for i in range(self.length()):
            items.append(str(self.collection[i]))
        return f"Bag([{', '.join(items)}])"
        

bag = Bag([3,4,5,6,3,455])

bag.add("Somethring")
bag.add("Fred")
bag.add([3,4,5])
print(bag.__iter__())
bag.remove("Fred")

print(bag.length())
print(bag.__iter__())

print(bag.__repr__())