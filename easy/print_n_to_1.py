"""
Print numbers from N to 1 (space separated) without the help of loops.

Example 1:

Input:
N = 10
Output: 10 9 8 7 6 5 4 3 2 1
"""
class Solution:
    def printNos(self, n):
        # Code here
        # base case
        if n == 0:
            return
        print(n, end=' ')
        self.printNos(n-1)
