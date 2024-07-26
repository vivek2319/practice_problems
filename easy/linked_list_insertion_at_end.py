'''    
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
class Solution:
    #Function to insert a node at the end of the linked list.
    def insertAtEnd(self,head,x):
        # code here 
        temp = Node(x)
        if head is None:
            return temp
        
        pointer = head
        while pointer.next:
            pointer = pointer.next
        
        pointer.next = temp
        
        return head
