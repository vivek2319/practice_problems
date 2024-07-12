"""
You are given a string S of size N that represents the prefix form of a valid mathematical expression. Convert it to its infix form.

Example 1:

Input: 
*-A/BC-/AKL
Output: 
((A-(B/C))*((A/K)-L))
Explanation: 
The above output is its valid infix form.
Your Task:

Complete the function string preToInfix(string pre_exp), which takes a prefix string as input and return its infix form.

 

Expected Time Complexity: O(N).

Expected Auxiliary Space: O(N).

Constraints:

3<=|S|<=104

 
"""
class Solution:
    def isOperator(self, c):
        if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
            return True
        else:
            return False

    def preToInfix(self, pre_exp):
        # Code here
        stack = []
     
        # read prefix in reverse order
        i = len(prefix) - 1
        while i >= 0:
            if not self.isOperator(prefix[i]):
                 
                # symbol is operand
                stack.append(prefix[i])
                i -= 1
            else:
               
                # symbol is operator
                str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
                stack.append(str)
                i -= 1
         
        return stack.pop()
     
