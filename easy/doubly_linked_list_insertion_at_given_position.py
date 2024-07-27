# Your task is to complete this function
# function should add a new node after the pth position
# function shouldn't print or return any data

'''
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

'''
#Function to insert a new node at given position in doubly linked list.
def addNode(head, p, data):
    # Code here
    # Create the new node
    if not head:
        return

    temp = head
    i = 0
    while i < p and temp:
        temp = temp.next
        i += 1

    if temp is None:
        return  # Handle case where pos is out of bounds

    new_node = Node(data)
    fwd = temp.next
    temp.next = new_node
    new_node.prev = temp
    new_node.next = fwd
    if fwd:
        fwd.prev = new_node
