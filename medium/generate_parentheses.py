"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(sol,open_count,close_count):
            if len(sol)==2*n:
                res.append(''.join(sol))
                return
            
            if open_count < n:
                sol.append('(')
                dfs(sol,open_count+1,close_count)
                sol.pop()
            
            if open_count > close_count:
                sol.append(')')
                dfs(sol,open_count,close_count+1)
                sol.pop()
        
        res = []
        sol = []
        dfs(sol,0,0)
        return res
