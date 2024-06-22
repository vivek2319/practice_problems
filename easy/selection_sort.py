#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        """
        Finds the index of the minimum element in the unsorted subarray starting from index i.

        Args:
            arr: The unsorted array.
            i: The starting index of the unsorted subarray.

        Returns:
            The index of the minimum element in the unsorted subarray.
        """
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        return min_index

    
    def selectionSort(self, arr,n):
        #code here
        """
        Sorts the array arr in ascending order using selection sort.

        Args:
            arr: The unsorted array.
            n: The size of the array.
        """

        for i in range(n):
            # Find the index of the minimum element in the unsorted subarray
            min_index = self.select(arr, i)

            # Swap the minimum element with the first element of the unsorted subarray
            arr[i], arr[min_index] = arr[min_index], arr[i]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
