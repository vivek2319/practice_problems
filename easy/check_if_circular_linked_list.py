"""
Given the head, the head of a singly linked list, find if the linked list is circular or not. A linked list is called circular if it is not NULL terminated and all nodes are connected in the form of a cycle. An empty linked list is considered circular.

Note: The linked list does not contain any inner loop.

Examples:

Input: LinkedList: 2->4->6->7->5

Output: true
Explanation: As shown in figure the first and last node is connected, i.e. 5 --> 2
Input:LinkedList: 2->4->6->7->5->1
 
Output: false
Explanation: As shown in figure this is not a circular linked list.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
0 <= number of nodes <= 100
1 <= node -> data <= 104


"""

#class Node:
#    def __init__(self, data):
#        self.data = data
#        self.next = None


# your task is to complete this function
# function should return true/false or 1/0
class Solution:
    def isCircular(self, head):
        # Code here
        if head is None:
            return True
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        if slow == fast:
            return True
        
        return False
