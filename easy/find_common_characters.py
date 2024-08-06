"""
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.

"""

from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        char_count = Counter(words[0])

        for word in words:
            current_count = Counter(word)
            
            for char in list(char_count):
                char_count[char] = min(char_count[char], current_count[char])
        
        common_characters = []

        for char, count in char_count.items():
            common_characters.extend([char] * count)

        return common_characters

