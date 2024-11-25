"""
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

 

Example 1:

Input: word = "USA"
Output: true
Example 2:

Input: word = "FlaG"
Output: false
 

Constraints:

1 <= word.length <= 100
word consists of lowercase and uppercase English letters.

"""

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capital_count = sum(c.isupper() for c in word)

        return capital_count == len(word) or capital_count == 0 or capital_count == 1 and word[0].isupper()