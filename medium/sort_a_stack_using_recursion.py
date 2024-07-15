"""
Given a stack, the task is to sort it such that the top of the stack has the greatest element.

Example 1:

Input:
Stack: 3 2 1
Output: 3 2 1
Example 2:

Input:
Stack: 11 2 32 3 41
Output: 41 32 11 3 2
Your Task: 
You don't have to read input or print anything. Your task is to complete the function sort() which sorts the elements present in the given stack. (The sorted stack is printed by the driver's code by popping the elements of the stack.)

Expected Time Complexity: O(N*N)
Expected Auxilliary Space: O(N) recursive.

Constraints:
1<=N<=100


"""

class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    # Code here
    def Sorted(self, s):
        # Base case: if the stack is empty, return
        if len(s) == 0:
            return

        # Remove the top element
        top = s.pop()

        # Sort the remaining stack
        self.Sorted(s)

        # Insert the removed element back into the sorted stack
        self.sorted_insert(s, top)

    def sorted_insert(self, s, element):
        # If stack is empty or top of stack is less than or equal to element, push the element
        if len(s) == 0 or s[-1] <= element:
            s.append(element)
            return
        
        # Remove the top element
        top = s.pop()

        # Recur for the rest of the stack
        self.sorted_insert(s, element)

        # Put back the top element
        s.append(top)

