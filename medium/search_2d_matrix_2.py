"""
Search a 2 D Matrix 2
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        m, n = len(matrix), len(matrix[0])  # Get number of rows (m) and columns (n)
        row, col = 0, n - 1  # Start from top-right corner

        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                # Move down if target is greater, as elements increase downwards
                row += 1  
            else:
            # Move left if target is smaller, as elements decrease to the left
                col -= 1  

        return False
        
