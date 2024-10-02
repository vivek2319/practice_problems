"""
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.

 

Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]
 

Constraints:

1 <= s.length <= 12
s consists of lowercase English letters, uppercase English letters, and digits.
"""

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def dfs(s,index, sol):
            if index == len(s):
                res.append("".join(sol.copy()))
                return
            if s[index].isdigit():
                sol.append(s[index])
                dfs(s, index + 1, sol)
                sol.pop()
            else:
                c = s[index].upper()
                sol.append(c)
                dfs(s, index + 1, sol)
                sol.pop()
                
                c = s[index].lower()
                sol.append(c)
                dfs(s, index + 1, sol)
                sol.pop()

        res = []
        sol = []
        dfs(s, 0, [])
        return res
