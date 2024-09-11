"""
Given a string s, return the maximum length of a 
substring
 such that it contains at most two occurrences of each character.
 

Example 1:

Input: s = "bcbbbcba"

Output: 4

Explanation:

The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".
Example 2:

Input: s = "aaaa"

Output: 2

Explanation:

The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".
 

Constraints:

2 <= s.length <= 100
s consists only of lowercase English letters.

"""

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = collections.Counter()
        ans = 0

        l = 0
        for r, c in enumerate(s):
            count[c] += 1
            while count[c] > 2:
                count[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)

        return ans
