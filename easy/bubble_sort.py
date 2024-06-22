"""
Iterate through adjacent elements (i and i+1) in the unsorted subarray.
If the current element (i) is greater than the next element (i+1), swap their positions.
"""
class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr, n):
        # code here
        for i in range(n-1):
            for j in range(n-i-1):
                if(arr[j] > arr[j+1]):
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
        
