########################################
# Name:
# Indicate any collaborators or tools used to assist you including AI:
# Estimated time spent (hrs):
########################################


class Bag:
    def __init__(self, iterable=None):
        """Initialize the Bag. Optionally add items from iterable."""
        self.collection =[]
        if iterable != None:
            self.collection=iterable

    def add(self, item):
        """Add one occurrence of item to the Bag."""
        index = self.length()
        if index ==0:
            self.collection = [item]
        else:
            new_collection = [None] * (index+1)
            for i in range(index):
                new_collection[i]= self.collection[i]
            new_collection[index]= item 
            self.collection = new_collection

    def remove(self, item):
        """Remove one occurrence of item from the Bag. Raise ValueError if not found."""
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

    def count(self, item):
        """Return the number of times item appears in the Bag."""
        cnt = 0
        for i in range(self.length()):
            if self.collection[i] == item:
                cnt +=1
        return cnt

    def length(self):
        """Return the total number of items in the Bag (including duplicates)."""
        cnt =0
        for i in self.collection:
            cnt +=1
        return cnt

    def __iter__(self):
        """Yield each item in the Bag, including duplicates."""
        item_list =[]
        i=0
        while i < self.length():
            item_list.append(self.collection[i])
            i += 1
        return item_list

    def contains(self, item):
        """Return True if item is in the Bag, False otherwise."""
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
    
    
    
    
        """_Justification and Analysis_
        
        1) Why do you choose the particular data structure for your bag?
        
        2)
        
        """