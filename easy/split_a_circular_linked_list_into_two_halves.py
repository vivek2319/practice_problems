"""
Given a Circular linked list. The task is split into two Circular Linked lists. If there are an odd number of nodes in the given circular linked list then out of the resulting two halved lists, the first list should have one node more than the second list.

Examples :

Input: LinkedList : 10->4->9
Output: 10->4 , 9
 
Explanation: After dividing linked list into 2 parts , the first part contains 10, 4 and second part contain only 9.
Input: LinkedList : 10->4->9->10
Output: 10->4 , 10->9

Explanation: After dividing linked list into 2 parts , the first part contains 10, 4 and second part contain 10, 9.
Expected Time Complexity: O(n)
Expected Auxilliary Space: O(1)

Constraints:
1 <= number of nodes <= 105
1 <= node->data <= 103


"""

#User function Template for python3
'''
class Node:
    def __init__(self):
        self.data = None
        self.next = None
'''


class Solution:
    def splitList(self, head):
        #code here
        if head is None:
            return None, None
        fast, slow = head, head
        while fast.next != head and fast.next.next != head:
            fast = fast.next.next
            slow = slow.next
        
        if fast.next.next == head:
            fast = fast.next
        
        head1 = head
        head2 = slow.next
        fast.next = slow.next
        slow.next = head
        
        return head1, head2

