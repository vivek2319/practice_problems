"""
Given a string s, return the maximum number of unique substrings that the given string can be split into.

You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "ababccc"
Output: 5
Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.
Example 2:

Input: s = "aba"
Output: 2
Explanation: One way to split maximally is ['a', 'ba'].
Example 3:

Input: s = "aa"
Output: 1
Explanation: It is impossible to split the string any further.
 

Constraints:

1 <= s.length <= 16

s contains only lower case English letters.


"""

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def dfs(start_index, unique_count):
            if start_index == len(s):
                nonlocal max_unique_splits
                max_unique_splits = max(max_unique_splits, unique_count)
                return
            
            for end_index in range(start_index + 1, len(s) + 1):
                if s[start_index : end_index] not in seen_substrings:
                    seen_substrings.add(s[start_index : end_index])
                    dfs(end_index , unique_count + 1)
                    seen_substrings.remove(s[start_index : end_index])
        
        seen_substrings = set()
        max_unique_splits = 1
        dfs(0,0)
        return max_unique_splits
