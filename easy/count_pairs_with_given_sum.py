# count total pairs that match to given target
class Solution:
    def getPairsCount(self, arr, n, k):
        count = 0
        
        for i in range(0,n):
            for j in range(i+1,n):
                if arr[i] + arr[j] == k:
                    count = count + 1
        return count
          
