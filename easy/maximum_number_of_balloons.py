"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0
 

Constraints:

1 <= text.length <= 104
text consists of lower case English letters only.

"""

from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        target = "balloon"
        s_count = Counter(text)
        target_count = Counter(target)

        max_rearrangements = len(text)
        for char in target:
            if char in s_count:
                max_rearrangements = min(max_rearrangements, s_count[char] // target_count[char])     
            else:
                return 0
        
        return max_rearrangements
