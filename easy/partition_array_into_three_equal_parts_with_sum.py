"""
Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i + 1 < j with (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])

 

Example 1:

Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
Example 2:

Input: arr = [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false
Example 3:

Input: arr = [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
 

Constraints:

3 <= arr.length <= 5 * 104
-104 <= arr[i] <= 104

"""

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total_sum = sum(arr)
        if total_sum % 3 != 0:
            return False
        
        left_sum, right_sum = 0, 0
        left_index = 0
        right_index = len(arr) - 1

        while left_index < len(arr):
            left_sum = left_sum + arr[left_index]
            if left_sum == total_sum // 3:
                break
            left_index = left_index + 1
        
        while right_index > 0 :
            right_sum = right_sum + arr[right_index]
            if right_sum == total_sum // 3:
                break
            right_index = right_index - 1
        
        return left_index < right_index - 1
