"""
Given a string s consisting only of opening and closing parenthesis 'ie '('  and ')', find out the length of the longest valid(well-formed) parentheses substring.
NOTE: The length of the smallest valid substring ( ) is 2.

Example 1:

Input: s = "(()("
Output: 2
Explanation: The longest valid 
substring is "()". Length = 2.
Example 2:

Input: s = "()(())("
Output: 6
Explanation: The longest valid 
substring is "()(())". Length = 6.

Your Task:  
You don't need to read input or print anything. Complete the function findMaxLen() which takes s as input parameter and returns the maxlength.


Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)   


Constraints:
1 <= |s| <= 105

 
"""
class Solution:
    def findMaxLen(ob, S):
        # code here
        stack = []
        last = len(S)
        
        result = 0
        
        for i in range(len(S)):
            if S[i] == '(':
                stack.append(i)
            else:
                if stack and S[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(i)
        while stack:
            now = stack.pop()
            result = max(result, last - now - 1)
            last = now
            
        return max(result, last)

