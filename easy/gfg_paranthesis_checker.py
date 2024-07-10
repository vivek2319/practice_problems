"""
Given an expression string x. Examine whether the pairs and the orders of {,},(,),[,] are correct in exp.
For example, the function should return 'true' for exp = [()]{}{[()()]()} and 'false' for exp = [(]).

Note: The drive code prints "balanced" if function return true, otherwise it prints "not balanced".

Example 1:

Input:
{([])}
Output: 
true
Explanation: 
{ ( [ ] ) }. Same colored brackets can form 
balanced pairs, with 0 number of 
unbalanced bracket.
Example 2:

Input: 
()
Output: 
true
Explanation: 
(). Same bracket can form balanced pairs, 
and here only 1 type of bracket is 
present and in balanced way.
Example 3:

Input: 
([]
Output: 
false
Explanation: 
([]. Here square bracket is balanced but 
the small bracket is not balanced and 
Hence , the output will be unbalanced.
Your Task:
This is a function problem. You only need to complete the function ispar() that takes a string as a parameter and returns a boolean value true if brackets are balanced else returns false. The printing is done automatically by the driver code.

Expected Time Complexity: O(|x|)
Expected Auixilliary Space: O(|x|)

Constraints:
1 ≤ |x| ≤ 32000
"""

class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,x):
        # code here
        stack = [] 
    
        #iterating over the string.
        for char in s:
            
            #if opening bracket is encountered, we push it into stack.
            if char in ['{','[','('] : 
                stack.append(char) 
            
            #if closing bracket is encountered, we compare it with top of stack.
            else:       
                
                if len(stack) == 0: 
                    return False
                
                #if top of stack has opening bracket of same type, we pop the
                #top element continue iterating else we return false.
    
                if char == '}':
                    if stack[-1] == '{':
                        stack.pop()
                        continue
                if char == ')':
                    if stack[-1] == '(':
                        stack.pop()
                        continue
                if char == ']':
                    if stack[-1] == '[':
                        stack.pop()
                        continue
                return False  
        
        #if stack becomes empty, we return true else false.       
        if len(stack): 
            return False
        return True
