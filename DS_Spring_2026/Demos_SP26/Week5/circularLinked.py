class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class CircularLinkedList:
    def __init__(self):
        # Create a dummy header node that points to itself
        self.header = Node()
        self.header.next = self.header
        self.tail = self.header 

    def insert(self, data):
        # Insert new node at the end (before header)
        new_node = Node(data, self.header)
        probe = self.header
        while probe.next != self.header:
            probe = probe.next
        probe.next = new_node
        self.tail = new_node

    def remove(self, data):
        # Remove first node with matching data
        probe = self.header
        while probe.next != self.header and probe.next.data != data:
            probe = probe.next
        if probe.next != self.header:
            to_remove = probe.next
            probe.next = to_remove.next
            # If removing the tail, update tail
            if to_remove == self.tail:
                if probe == self.header:
                    # List is now empty
                    self.tail = self.header
                else:
                    self.tail = probe

    def print_last(self):
        if self.tail == self.header:
            print("List is empty")
        else:
            print(self.tail.data)

            
clist = CircularLinkedList()
clist.insert(10)
clist.insert(20)
clist.insert(30)
clist.insert(50)
clist.insert(60)
clist.remove(60)
clist.print_last()