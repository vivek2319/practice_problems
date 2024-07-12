"""
You are given a string that represents the prefix form of a valid mathematical expression. Convert it to its postfix form.

Example:

Input: 
*-A/BC-/AKL
Output: 
ABC/-AK/L-*
Explanation: 
The above output is its valid postfix form.
Your Task:

Complete the function preToPost(string pre_exp), which takes a prefix string as input and returns its postfix form.

 

Expected Time Complexity: O(N).

Expected Auxiliary Space: O(N).

Constraints:

3<=pre_exp.length()<=100
"""


class Solution:
    def preToPost(self, pre_exp):
        # Code here
        stack = []
        
        # Iterate through the prefix expression in reverse order
        for char in pre_exp[::-1]:
            # If the character is an operand, push it to the stack
            if char.isalpha():
                stack.append(char)
            # If the character is an operator, pop two operands from the stack,
            # concatenate them with the operator, and push the result back to the stack
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op1 + op2 + char)
        
        # The final postfix expression is at the top of the stack
        return stack.pop()
