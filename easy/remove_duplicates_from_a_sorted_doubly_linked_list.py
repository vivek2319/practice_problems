"""
Given a doubly linked list of n nodes sorted by values, the task is to remove duplicate nodes present in the linked list.

Example 1:

Input:
n = 6
1<->1<->1<->2<->3<->4
Output:
1<->2<->3<->4
Explanation:
Only the first occurance of node with value 1 is 
retained, rest nodes with value = 1 are deleted.
Example 2:

Input:
n = 7
1<->2<->2<->3<->3<->4<->4
Output:
1<->2<->3<->4
Explanation:
Only the first occurance of nodes with values 2,3 and 4 are 
retained, rest repeating nodes are deleted.
Your Task:
You have to complete the method removeDuplicates() which takes 1 argument: the head of the linked list.  Your function should return a pointer to a linked list with no duplicate element.

Constraint:
1 <= n <= 105
Expected Time Complexity: O(n)
Expected Space Complexity: O(1)


"""

#Back-end complete function Template for Python 3

'''
# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
		        self.prev = None
'''
class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        # return head after editing list
        
        curr = head

        # Handle edge cases: empty or single-node list
        if not head or not head.next:
            return head

        while curr and curr.next:
            # Check if current node's data is equal to next node's data
            if curr.data == curr.next.data:
                # Remove the duplicate node (curr.next)
                next_node = curr.next
                curr.next = next_node.next
                if next_node.next:  # If not the last node
                    next_node.next.prev = curr

                # No need to advance curr as we already checked the next node
            else:
                curr = curr.next

        return head
