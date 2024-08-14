"""
Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.

An alphanumeric string is a string consisting of lowercase English letters and digits.

 

Example 1:

Input: s = "dfa12321afd"
Output: 2
Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.
Example 2:

Input: s = "abc1111"
Output: -1
Explanation: The digits that appear in s are [1]. There is no second largest digit. 
 

Constraints:

1 <= s.length <= 500
s consists of only lowercase English letters and/or digits.
"""

class Solution:
    def secondHighest(self, s: str) -> int:
        first = -1
        second = -1

        for i in s:
            if i.isdigit():
                num = int(i)
                if num > first:
                    second = first
                    first = num
                elif first > num > second:
                    second = num

        return second
