"""
You are given a positive integer n.

A binary string x is valid if all 
substrings
 of x of length 2 contain at least one "1".

Return all valid strings with length n, in any order.

 

Example 1:

Input: n = 3

Output: ["010","011","101","110","111"]

Explanation:

The valid strings of length 3 are: "010", "011", "101", "110", and "111".

Example 2:

Input: n = 1

Output: ["0","1"]

Explanation:

The valid strings of length 1 are: "0" and "1".

 

Constraints:

1 <= n <= 18
"""

class Solution:
    def validStrings(self, n: int) -> List[str]:
        def dfs(n, current_string):
            # Base Case
            if len(current_string) == n:
                all_valid_strings.append(current_string)
                return
            
            # Recursive Case
            # If the last char is '0', only append '1' to avoid "00"
            if current_string and current_string[-1] == "0":
                dfs(n, current_string + "1")
            else: 
                dfs(n, current_string + "0")
                dfs(n, current_string + "1")
        
        # Initialize the list to store all valid strings
        all_valid_strings = []

        # start the recursion with an empty string
        dfs(n, "")

        # return the list of all valid strings
        return all_valid_strings
