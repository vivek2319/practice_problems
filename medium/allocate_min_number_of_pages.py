"""
You have n books, each with arr[i] number of pages. m students need to be allocated contiguous books, with each student getting at least one book.
Out of all the permutations, the goal is to find the permutation where the sum of maximum number of pages in a book allotted to a student should be minimum, out of all possible permutations.

Note: Return -1 if a valid assignment is not possible, and allotment should be in contiguous order (see the explanation for better understanding).

 

Examples:

Input: n = 4, arr[] = {12,34,67,90}, m = 2
Output: 113
Explanation: Allocation can be done in following ways:
{12} and {34, 67, 90} Maximum Pages = 191
{12, 34} and {67, 90} Maximum Pages = 157
{12, 34, 67} and {90} Maximum Pages =113.
Therefore, the minimum of these cases is 113,
which is selected as the output.

Input: n = 3, arr[] = {15,17,20}, m = 2
Output: 32
Explanation: Allocation is done as {15,17} and {20}.

Expected Time Complexity: O(n logn)
Expected Auxilliary Space: O(1)


"""

class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self,n ,arr ,m):
        # book allocation impossible
        if m > n:
            return -1
    
        low = max(arr)
        high = sum(arr)
        while low <= high:
            mid = (low + high) // 2
            students = self.countStudents(arr, mid)
            if students > m:
                low = mid + 1
            else:
                high = mid - 1
        return low
        
    def countStudents(self, arr, pages):
        n = len(arr)  # size of array
        students = 1
        pagesStudent = 0
        for i in range(n):
            if pagesStudent + arr[i] <= pages:
                # add pages to current student
                pagesStudent += arr[i]
            else:
                # add pages to next student
                students += 1
                pagesStudent = arr[i]
        return students




#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        n = int(input())

        arr = [int(x) for x in input().strip().split()]
        m = int(input())

        ob = Solution()

        print(ob.findPages(n, arr, m))

# } Driver Code Ends
