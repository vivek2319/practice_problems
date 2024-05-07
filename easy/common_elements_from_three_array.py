class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        # your code here
        i, j, k = 0, 0, 0
        common_elements = []
        prev = float('-inf')
        
        #Iterate through three arrays while all arrays have elements
        while (i < n1 and j < n2 and k < n3):
            # If x = y and y = z, print any of them and move ahead
            # in all arrays
            if (A[i] == B[j] and B[j] == C[k] and A[i] != prev):
                if (A[i] not in common_elements):
                    common_elements.append(A[i])
                    prev = A[i]
                    i += 1
                    j += 1
                    k += 1
                
         
            # x < y
            elif A[i] < B[j]:
                i += 1
                 
            # y < z
            elif B[j] < C[k]:
                j += 1
                 
            # We reach here when x > y and z < y, i.e., z is smallest
            else:
                k += 1
        return common_elements if common_elements else [-1]
