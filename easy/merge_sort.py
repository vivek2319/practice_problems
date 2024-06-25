"""
Given an array arr[], its starting position l and its ending position r. Sort the array using merge sort algorithm.
Example 1:

Input:
N = 5
arr[] = {4 1 3 9 7}
Output:
1 3 4 7 9
Example 2:

Input:
N = 10
arr[] = {10 9 8 7 6 5 4 3 2 1}
Output:
1 2 3 4 5 6 7 8 9 10

Your Task:
You don't need to take the input or print anything. Your task is to complete the function merge() which takes arr[], l, m, r as its input parameters and modifies arr[] in-place such that it is sorted from position l to position r, and function mergeSort() which uses merge() to sort the array in ascending order using merge sort algorithm.

Expected Time Complexity: O(nlogn) 
Expected Auxiliary Space: O(n)

Constraints:
1 <= N <= 105
1 <= arr[i] <= 105
"""
#User function Template for python3
class Solution:
    def merge(self,arr, l, m, r): 
        # code here
        n1 = m - l + 1  # Size of the first sub-array
        n2 = r - m  # Size of the second sub-array
    
        # Create temporary arrays to hold the sub-arrays
        left = [0] * n1
        right = [0] * n2
    
        # Copy data to temporary arrays
        for i in range(n1):
            left[i] = arr[l + i]
        for j in range(n2):
            right[j] = arr[m + 1 + j]
    
        # Merge the temporary arrays back into arr[l..r]
        i = 0  # Index for first sub-array
        j = 0  # Index for second sub-array
        k = l  # Index for merged sub-array
    
        # Merge while there are elements in both sub-arrays
        while i < n1 and j < n2:
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1  # Move k only after copying the element
    
        # Copy the remaining elements (if any)
        while i < n1:
            arr[k] = left[i]
            i += 1
            k += 1
        while j < n2:
            arr[k] = right[j]
            j += 1
            k += 1
    def mergeSort(self,arr, l, r):
        #code here
        if l < r:
            # Find the middle point
            m = l + (r - l) // 2

            # Sort first and second halves
            self.mergeSort(arr, l, m)
            self.mergeSort(arr, m + 1, r)

            # Merge the sorted halves
            self.merge(arr, l, m, r)

