"""
Given the head of a singly linked list, the task is to check if the linked list has a loop. A loop means that the last node of the linked list is connected back to a node in the same list.  So if the next of the last node is null. then there is no loop. We need to return true if there is a loop, otherwise false.

The following is an internal representation of every test case (three inputs).
A LinkedList and a pos (1-based index)-Position of the node to which the last node links back if there is a loop. If the linked list does not have any loop, then pos = 0.

Examples:

Input: LinkedList: 1->3->4, pos = 2
Output: true
Explanation: 

See the above list there exists a loop connecting the last node back to the second node.
Input: LinkedList: 1->8->3->4, pos = 0
Output: false
Explanation: 

There is no loop exists.
Input: LinkedList: 1->2->3->4, pos = 1
Output: true
Explanation:

A loop is present connecting the last node back to the first node.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ number of nodes ≤ 104
1 ≤ node->data ≤ 103
"""

#User function Template for python3
'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	
'''
class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        #code here
        slow = head
        fast = head
    
        # Step 2: Traverse the linked list
        # with the slow and fast pointers
        while fast is not None and fast.next is not None:
            # Move slow one step
            slow = slow.next
            # Move fast two steps
            fast = fast.next.next
    
            # Check if slow and fast pointers meet
            if slow == fast:
                return True  # Loop detected
    
        # If fast reaches the end of the
        # list, there is no loop
        return False
