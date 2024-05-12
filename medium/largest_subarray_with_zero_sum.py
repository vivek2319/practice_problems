class Solution:
    def maxLen(self, n, arr):
        #Code here
        maxLen = 0
        currsum = 0

        h = {} 

        for i in range(n): 
            currsum += arr[i] 

            if currsum == 0: 
                maxLen = i + 1

            if currsum in h: 
                maxLen = max(maxLen, i - h[currsum]) 
            else: 
                h[currsum] = i 
        return maxLen
