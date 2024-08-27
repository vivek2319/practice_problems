"""
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

 

Example 1:


Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.
Example 2:

Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8
Example 3:

Input: mat = [[5]]
Output: 5
 

Constraints:

n == mat.length == mat[i].length
1 <= n <= 100
1 <= mat[i][j] <= 100

"""
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)

        primary_diagonal_sum = 0
        secondary_diagonal_sum = 0

        for i in range(n):
            primary_diagonal_sum = primary_diagonal_sum + mat[i][i]
            secondary_diagonal_sum = secondary_diagonal_sum + mat[i][n-i-1]
        
        # if n is odd that mean middle element got counted twice, subtract it
        if n % 2 == 1:
            middle_element = mat [n // 2][n // 2]
            return primary_diagonal_sum + secondary_diagonal_sum - middle_element
        else:
            return primary_diagonal_sum + secondary_diagonal_sum

