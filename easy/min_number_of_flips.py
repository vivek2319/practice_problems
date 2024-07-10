"""
Given a binary string, that is it contains only 0s and 1s. We need to make this string a sequence of alternate characters by flipping some of the bits, our goal is to minimize the number of bits to be flipped.

Example 1:

Input:
S = "001"
Output: 1
Explanation: 
We can flip the 0th bit to 1 to have
101.


Example 2:

Input:
S = "0001010111" 
Output: 2
Explanation: We can flip the 1st and 8th bit 
bit to have "0101010101"
101.

Your Task:
You don't need to read input or print anything. Your task is to complete the function minFlips() which takes the string S as input and returns the minimum number of flips required.


Expected Time Complexity: O(|S|).
Expected Auxiliary Space: O(1).


Constraints:
1<=|S|<=105

 
"""
class Solution:
    def minFlips(self, S):
        # Code here
        n = len(S)

        # Initialize two counts to track the minimum flips needed for starting with either 0 or 1
        count0, count1 = 0, 0
    
        # Iterate through the string, maintaining counts for alternating sequences
        for i in range(n):
            if (i % 2 == 0 and S[i] == '1') or (i % 2 == 1 and S[i] == '0'):
                count0 += 1  # Flip needed for alternating with 0 at start
            elif (i % 2 == 0 and S[i] == '0') or (i % 2 == 1 and S[i] == '1'):
                count1 += 1  # Flip needed for alternating with 1 at start
    
        # Return the minimum of flips needed for either starting sequence
        return min(count0, count1)
