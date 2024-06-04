"""
Print GFG n times without the loop.

Example:

Input:
5
Output:
GFG GFG GFG GFG GFG
"""
class Solution:
    def printGfg(self,n):
        # Code here
        if n == 0:
            return
        print('GFG', end = ' ')
        self.printGfg(n - 1)
