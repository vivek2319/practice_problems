"""
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

 

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100
 
"""
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])  # Get number of rows (m) and columns (n)
        row, col = m - 1, 0  # Start from bottom-left corner

        count = 0
        while row >= 0 and col < n:
            if grid[row][col] < 0:
                # All elements to the right in the current row are negative
                count += n - col
                row -= 1  # Move up a row
            else:
                col += 1  # Move right a column

        return count
        
