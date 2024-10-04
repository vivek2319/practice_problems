"""
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

 

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
 

Constraints:

1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
words[i] and chars consist of lowercase English letters.
"""

from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total = 0
        chars_count = Counter(chars)

        # first - part - Let's form a dictionary
        for word in words:
            dictionary = {}
            word_count = Counter(word)
            
            can_form_word = False
            for letter in word:
                if word_count[letter] > chars_count.get(letter, 0):
                    break  # If any letter count exceeds chars_count, break the loop
            else:
                can_form_word = True # Set True only if all letters are valid
            
            if can_form_word:
                total = total + len(word)

        return total
