"""
Given a Queue Q containing N elements. The task is to reverse the Queue. Your task is to complete the function rev(), that reverses the N elements of the queue.

Example 1:

Input:
6
4 3 1 10 2 6
Output: 
6 2 10 1 3 4
Explanation: 
After reversing the given elements of the queue , the resultant queue will be 6 2 10 1 3 4.
Example 2:

Input:
4
4 3 2 1 
Output: 
1 2 3 4
Explanation: 
After reversing the given elements of the queue , the resultant queue will be 1 2 3 4.
Your Task: You need to complete the function rev that takes a queue as parameter and returns the reversed queue. The printing is done automatically by the driver code.

Expected Time Complexity : O(n)
Expected Auxilliary Space : O(n)
"""

class Solution:
    
    #Function to reverse the queue.
    def rev(self, q):
        #using a stack to reverse the queue.
        stack=[]
        
        #pushing elements from queue into stack and removing them from queue.
        while(q.qsize()!=0):
            x=q.get()
            stack.append(x)
            
            
        #now pushing elements back into the queue from stack and removing them 
        #from stack. queue gets reversed as stack follows last in first out.
        while(len(stack)!=0):
            x=stack.pop()
            q.put(x)
            
        #returning reversed queue.
        return q
