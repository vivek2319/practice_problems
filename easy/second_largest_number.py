class Solution:
	def print2largest(self,arr, n):
	    if n < 2:
            return -1
        
        largest = float('-inf')
        second_largest = float('-inf')
        
        for i in range(n):
            if arr[i] > largest:
                second_largest = largest
                largest = arr[i]
            elif arr[i] > second_largest and arr[i] != largest:
                second_largest = arr[i]
                
        return second_largest if second_largest != float('-inf') else -1
