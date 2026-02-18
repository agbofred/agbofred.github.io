from linked import Node
head = None
# Add five nodes to the beginning of the linked structure
for count in range(1, 6):
    head = Node(count, head)
# Print the contents of the structure
searchTarget = 2
while head != None and searchTarget !=head.data:
    print(head.data, "----", head.next)
    head = head.next