class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        max_current = arr[0]
        global_sum = max_current
        for i in range(1, N):
            max_current = max(arr[i], max_current + arr[i])
            global_sum = max(max_current, global_sum)
        
        return global_sum
