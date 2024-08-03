"""
Given a linked list of N nodes where nodes can contain values 0s, 1s, and 2s only. The task is to segregate 0s, 1s, and 2s linked list such that all zeros segregate to head side, 2s at the end of the linked list, and 1s in the mid of 0s and 2s.

Example 1:

Input:
N = 8
value[] = {1,2,2,1,2,0,2,2}
Output: 0 1 1 2 2 2 2 2
Explanation: All the 0s are segregated
to the left end of the linked list,
2s to the right end of the list, and
1s in between.
Example 2:

Input:
N = 4
value[] = {2,2,0,1}
Output: 0 1 2 2
Explanation: After arranging all the
0s,1s and 2s in the given format,
the output will be 0 1 2 2.
Your Task:
The task is to complete the function segregate() which segregates the nodes in the linked list as asked in the problem statement and returns the head of the modified linked list. The printing is done automatically by the driver code.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <= N <= 106


"""

#User function Template for python3
'''
	Your task is to segregate the list of 
	0s,1s and 2s.
	
	Function Arguments: head of the original list.
	Return Type: head of the new list formed.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''
class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        #code here 
        if not head or not head.next:
            return head

        # Create three dummy nodes to point to beginning of 
        # three linked lists. These dummy nodes are created to 
        # avoid null checks. 
        zeroD = Node(0)
        oneD = Node(0)
        twoD = Node(0)
    
        # Initialize current pointers for three 
        # lists 
        zero = zeroD
        one = oneD
        two = twoD
    
        # Traverse list 
        curr = head
        while curr:
            if curr.data == 0:
                # If the data of current node is 0, 
                # append it to pointer zero and update zero
                zero.next = curr
                zero = zero.next
            elif curr.data == 1:
                # If the data of current node is 1, 
                # append it to pointer one and update one
                one.next = curr
                one = one.next
            else:
                # If the data of current node is 2, 
                # append it to pointer two and update two
                two.next = curr
                two = two.next
            curr = curr.next
    
        # Combine the three lists
        zero.next = oneD.next if oneD.next else twoD.next
        one.next = twoD.next
        two.next = None
    
        # Updated head 
        head = zeroD.next
    
        return head
