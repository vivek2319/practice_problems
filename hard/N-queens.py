"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]
 

Constraints:

1 <= n <= 9
""'

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        state = [ ["."] * n for _ in range(n)]
        res = []

        visited_cols = set()
        visited_diagonals = set()
        visited_antidiagonals = set()

        def dfs(row):
            if row == n:
                res.append(["".join(row) for row in state])
                return
            for col in range(n):
                diagonal_difference = row - col
                diagonal_sum = row + col

                if not (col in visited_cols or diagonal_difference in visited_diagonals or
                    diagonal_sum in visited_antidiagonals):

                    visited_cols.add(col)
                    visited_diagonals.add(diagonal_difference)
                    visited_antidiagonals.add(diagonal_sum)
                    state[row][col] = 'Q'
                    dfs(row + 1)
                    
                    visited_cols.remove(col)
                    visited_diagonals.remove(diagonal_difference)
                    visited_antidiagonals.remove(diagonal_sum)
                    state[row][col] = '.'
        dfs(0)
        return res
