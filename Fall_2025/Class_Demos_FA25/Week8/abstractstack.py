class AbstractStack(object):
    
    """Abstract class that implements the common 
    methods for stack collections"""
    
    # Constructor
    def __init__(self, sourceCollection=None):
        self.size = 0
        if sourceCollection:
            for i in sourceCollection:
                self.push(i)
                
    def isEmpty(self):
        """Returns True if stack is empty. Otherwise, returns False 
        """
        return len(self) == 0
    
    def __len__(self):
        """Returns the number of items in stack
        """
        return self.size
    
    def __str__(self):
        """Returns the string repsentative of S
        """
        return "{" + ", ".join(map(str,self)) +"}"
    