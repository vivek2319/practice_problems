    # The last element is always a leader
class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        #Code here
        if N == 0:
            return []
        
        leaders = []
        max_right = A[N-1]
        
        # The last element is always a leader
        leaders.append(max_right)
        
        # traverse the array from right to left
        for i in range(N-2, -1, -1):
            if A[i] >= max_right:
                max_right = A[i]
                leaders.append(max_right)
                
        leaders.reverse()
        
        return leaders
