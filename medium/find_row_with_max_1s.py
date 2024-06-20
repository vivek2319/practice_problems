"""
Given a boolean 2D array of n x m dimensions, consisting of only 1's and 0's, where each row is sorted. Find the 0-based index of the first row that has the maximum number of 1's.

Example 1:

Input: 
N = 4 , M = 4
Arr[][] = {{0, 1, 1, 1},
           {0, 0, 1, 1},
           {1, 1, 1, 1},
           {0, 0, 0, 0}}
Output: 2
Explanation: Row 2 contains 4 1's (0-based
indexing).

Example 2:

Input: 
N = 2, M = 2
Arr[][] = {{0, 0}, {1, 1}}
Output: 1
Explanation: Row 1 contains 2 1's (0-based
indexing).

Your Task:  
You don't need to read input or print anything. Your task is to complete the function rowWithMax1s() which takes the array of booleans arr[][], n and m as input parameters and returns the 0-based index of the first row that has the most number of 1s. If no such row exists, return -1.
 

Expected Time Complexity: O(N+M)
Expected Auxiliary Space: O(1)


Constraints:
1 ≤ N, M ≤ 103
0 ≤ Arr[i][j] ≤ 1 

 
"""
#User function Template for python3
class Solution:
	def rowWithMax1s(self,arr, n, m):
	    cnt_max = 0
        index = -1
    
        # traverse the rows:
        for i in range(n):
            # get the number of 1's:
            cnt_ones = m - self.lowerBound(arr[i], m, 1)
            if cnt_ones > cnt_max:
                cnt_max = cnt_ones
                index = i
        return index
    
    def lowerBound(self, arr, n, x):
        low = 0
        high = n - 1
        ans = n
    
        while low <= high:
            mid = (low + high) // 2
            # maybe an answer
            if arr[mid] >= x:
                ans = mid
                # look for smaller index on the left
                high = mid - 1
            else:
                low = mid + 1  # look on the right
        return ans


