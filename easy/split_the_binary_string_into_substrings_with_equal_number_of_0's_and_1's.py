"""
Given binary string str of length N. The task is to find the maximum count of consecutive substrings str can be divided into such that all the substrings are balanced i.e. they have an equal number of 0s and 1s. If it is not possible to split str satisfying the conditions then return -1.

Example 1:

Input:
S = "0100110101"
Output: 4
Explanation: 
The required substrings are 01, 0011, 01 and 01.

Example 2:

Input:
S = "0111100010"
Output: 3
 

Your Task:  
You don't need to read input or print anything. Your task is to complete the function maxSubStr() which takes a string S and returns an integer as output.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

 

Constraints:
1 <= S.length <= 105
"""

#Back-end complete function Template for Python 3

class Solution:
    def maxSubStr(self,str):
        #Write your code here
        
        # To store the count of 0s and 1s
        count0 = 0
        count1 = 0
         
        # To store the count of maximum 
        # substrings str can be divided into
        cnt = 0
         
        for i in range(len(str)):
            if str[i] == '0':
                count0 += 1
            else:
                count1 += 1
                 
            if count0 == count1:
                cnt += 1
     
    # It is not possible to 
        # split the string
        if count0 != count1:
            return -1
                 
        return cnt
                




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        s=input()
        obj=Solution()
        ans=obj.maxSubStr(s)
        print(ans)
# } Driver Code Ends
