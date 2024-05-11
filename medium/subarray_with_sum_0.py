# Given an array of integers. Find if there is a subarray (of size at-least one) with 0 sum. 
# You just need to return true/false depending upon whether there is a subarray present with 0-sum or not.
class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        ##Your code here
        #Return true or false
        current_sum = 0
        prefix_sum = {}
        for i in range(n):
            current_sum += arr[i]
            
            if current_sum == 0 or current_sum in prefix_sum:
                return True
            
            prefix_sum[current_sum] = i
        
        return False
