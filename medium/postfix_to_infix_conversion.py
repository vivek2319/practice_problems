"""
You are given a string that represents the postfix form of a valid mathematical expression. Convert it to its infix form.

Example:

Input:
ab*c+ 
Output: 
((a*b)+c)
Explanation: 
The above output is its valid infix form.
Your Task:

Complete the function string postToInfix(string post_exp), which takes a postfix string as input and returns its infix form.

 

Expected Time Complexity: O(N).

Expected Auxiliary Space: O(N).

Constraints:

3<=post_exp.length()<=104
"""

class Solution:
    def isOperand(self,x):
        return ((x >= 'a' and x <= 'z') or
            (x >= 'A' and x <= 'Z')) 
 
    # Get Infix for a given postfix 
    # expression 
    def postToInfix(self, postfix):
     
        s = [] 
     
        for i in postfix:     
             
            # Push operands 
            if (self.isOperand(i)) :         
                s.insert(0, i) 
                 
            # We assume that input is a 
            # valid postfix and expect 
            # an operator. 
            else:
             
                op1 = s[0] 
                s.pop(0) 
                op2 = s[0] 
                s.pop(0) 
                s.insert(0, "(" + op2 + i +
                                 op1 + ")") 
                 
        # There must be a single element in 
        # stack now which is the required 
        # infix. 
        return s[0]
