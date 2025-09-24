# Code for a singly linked node class:
class Node(object):
    """Represents a singly linked node."""
    def __init__(self, data, next = None):
        """Instantiates a Node with a default next of None."""
        self.data = data
        self.next = next
        
head = None
# Add five nodes to the beginning of the linked structure
for count in range(1, 6):
    head = Node(count, head)
# Print the contents of the structure
while head != None:
    print(f"Node data: {head.data} -----> Node Pointer {head.next}")
    head = head.next