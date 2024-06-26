class Solution:
    def partition(self,arr,low,high):
        # code here
        pivot = arr[high]  # Choose the last element as the pivot
        i = low - 1  # Index of smaller element

        # Move elements smaller than pivot to the left partition
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        # Place the pivot in its correct position
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1  # Return the pivot's final index
    
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        # code here
        if low < high:
        # pi is partitioning index, arr[p] is now at right place
            pi = self.partition(arr, low, high)

            # Recursively sort elements before and after partition
            self.quickSort(arr, low, pi - 1)
            self.quickSort(arr, pi + 1, high)
