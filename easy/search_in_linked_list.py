''' Node of a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def searchKey(self, n, head, key):
        #Code here
        current = head

        # Traverse the linked list until the end or the key is found
        while current:
            if current.data == key:
                return True  # Key found, return True
            current = current.next

        return False  # Key not found, return False
