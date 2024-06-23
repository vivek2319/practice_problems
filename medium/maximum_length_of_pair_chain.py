"""
You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.

A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.

Return the length longest chain which can be formed.

You do not need to use up all the given intervals. You can select pairs in any order.

 

Example 1:

Input: pairs = [[1,2],[2,3],[3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4].
Example 2:

Input: pairs = [[1,2],[7,8],[4,5]]
Output: 3
Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].
 

Constraints:

n == pairs.length
1 <= n <= 1000
-1000 <= lefti < righti <= 1000

"""

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # Initialize the variable to store the length of the longest chain
        longest_chain_length = 0
        # the current end of value of the last pair in the chain
        current_end = float('-inf')
        # Sort the pairs based on their second element since we want to ensure 
        # we pick the next pair with the smallest possible end value.
        for start, end in sorted(pairs, key=lambda x: x[1]):
            # If the current start is greater than the last stored end,
            # it means we can append the current pair to the chain.
            if current_end < start:
                current_end = end # Update the end to the current pair's end
                longest_chain_length += 1 # Increase the length of the chain
        # Return the length of the longest chain found
        return longest_chain_length


        
