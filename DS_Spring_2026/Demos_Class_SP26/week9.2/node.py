# Code for a singly linked node class:
class Node(object):
    """Represents a singly linked node."""
    def __init__(self, data, next = None):
        """Instantiates a Node with a default next of None."""
        self.data = data
        self.next = next
# Using the Singly Linked Node Class 
node1 = None                # Just an empty link    
node2 = Node("A", None)     # A node containing data and an empty link
node3 = Node("B", node2)    # A node containing data and a link to node2
node2.next = node3

