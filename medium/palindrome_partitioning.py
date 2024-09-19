"""
Given a string s, partition s such that every 
substring
 of the partition is a 
palindrome
. Return all possible palindrome partitioning of s.


Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 
Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.
"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(start_index: int):
            if start_index == length:
                res.append(sol.copy())
                return
          
            # Iterate over the substring starting from start_index
            for end_index in range(start_index, length):
                # If the substring s[start_index:end_index+1] is a palindrome,
                # we proceed to add it to the current partition and recurse
                if palindrome_flags[start_index][end_index]:
                    sol.append(s[start_index:end_index + 1])
                    dfs(end_index + 1)  # Recurse with the next starting index
                    sol.pop()  # Backtrack

        # Get the length of the input string
        length = len(s)
      
        # Initialize a 2D list to store palindrome flags
        palindrome_flags = [[True] * length for _ in range(length)]
      
        # Fill the palindrome_flags list in reverse order
        for i in range(length - 1, -1, -1):
            for j in range(i + 1, length):
                # A substring is a palindrome if the first and last characters are the same,
                # and if the substring between them is also a palindrome
                palindrome_flags[i][j] = s[i] == s[j] and palindrome_flags[i + 1][j - 1]
              
        # Initialize the result list and the list to store the current partition
        res = []
        sol = []
      
        # Start the DFS traversal from index 0
        dfs(0)
      
        return res
