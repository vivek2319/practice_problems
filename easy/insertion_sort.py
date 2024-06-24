#Sort the array using insertion sort

class Solution:
    def insert(self, alist, index, n):
        #code here
        # Get the element to be inserted
        temp = alist[index]

        # Move elements of alist[0..i-1], that are greater than temp, to one position ahead
        # of their current position
        i = index - 1
        while i >= 0 and alist[i] > temp:
            alist[i + 1] = alist[i]
            i -= 1

        # Put the element at its correct position
        alist[i + 1] = temp
        
    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, alist, n):
        #code here
        # One by one move boundary of unsorted subarray
        for i in range(1, n):
            # Call insert() to insert element at correct position
            self.insert(alist, i, n)


#{ 
 # Driver Code Starts

if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
    
        Solution().insertionSort(arr,n)
    
        for i in range(n):
            print(arr[i],end=" ")
    
        print()
# } Driver Code Ends
