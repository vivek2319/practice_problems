"""
You are given a string that represents the postfix form of a valid mathematical expression. Convert it to its prefix form.

Example 1:

Input: 
ABC/-AK/L-*
Output: 
*-A/BC-/AKL
Explanation: 
The above output is its valid prefix form.

Example 2:

Input: 
ab+
Output: 
+ab
Explanation: 
The above output is its valid prefix form.
Your Task:

Complete the function string postToPre(string post_exp), which takes a postfix string as input and returns its prefix form.

Expected Time Complexity: O(post_exp.length()).

Expected Auxiliary Space: O(post_exp.length()).

Constraints:

3<=post_exp.length()<=16000

"""
class Solution:
    def isOperator(self,x):
        if x == "+":
            return True
     
        if x == "-":
            return True
     
        if x == "/":
            return True
     
        if x == "*":
            return True
     
        return False
 
    # Convert postfix to Prefix expression
 
 
    def postToPre(self,post_exp):
        s = []
     
        # length of expression
        length = len(post_exp)
     
        # reading from right to left
        for i in range(length):
     
            # check if symbol is operator
            if (self.isOperator(post_exp[i])):
     
                # pop two operands from stack
                op1 = s[-1]
                s.pop()
                op2 = s[-1]
                s.pop()
     
                # concat the operands and operator
                temp = post_exp[i] + op2 + op1
     
                # Push string temp back to stack
                s.append(temp)
     
            # if symbol is an operand
            else:
     
                # push the operand to the stack
                s.append(post_exp[i])
 
    
        ans = ""
        for i in s:
            ans += i
        return ans
