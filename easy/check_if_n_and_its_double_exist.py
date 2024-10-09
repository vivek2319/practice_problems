"""
Given an array arr of integers, check if there exist two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
 

Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
Example 2:

Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.
 

Constraints:

2 <= arr.length <= 500
-103 <= arr[i] <= 103
"""

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()

        for i in range(len(arr)):
            product = arr[i] * 2
            left = 0
            right = len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == product and mid != i:
                    return True
                elif arr[mid] < product:
                    left = left + 1
                else:
                    right = right - 1
        return False
