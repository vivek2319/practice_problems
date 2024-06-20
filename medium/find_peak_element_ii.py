"""
A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left, right, top, and bottom.

Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the length 2 array [i,j].

You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.

You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.

Input: mat = [[1,4],[3,2]]
Output: [0,1]
Explanation: Both 3 and 4 are peak elements so [1,0] and [0,1] are both acceptable answers.

Input: mat = [[10,20,15],[21,30,14],[7,16,32]]
Output: [1,1]
Explanation: Both 30 and 32 are peak elements so [1,1] and [2,2] are both acceptable answers.
"""

from typing import List
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])

        def findMaxIndex(row):
            maxVal = -1
            maxInd = -1
            for i in range(len(row)):
                if row[i] > maxVal:
                    maxVal = row[i]
                    maxInd = i
            return maxInd
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            ind = findMaxIndex(mat[mid])
            up = mat[mid - 1][ind] if mid - 1 >= 0 else -1
            down = mat[mid + 1][ind] if mid + 1 < n else -1
            if up < mat[mid][ind] > down:
                return [mid, ind]
            elif up > mat[mid][ind]:
                high = mid-1
            else:
                low = mid+1
        return [-1, -1]
