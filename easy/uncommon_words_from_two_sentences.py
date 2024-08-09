"""
A sentence is a string of single-space separated words where each word consists only of lowercase letters.
A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

Example 1:

Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: s1 = "apple apple", s2 = "banana"
Output: ["banana"]
 

Constraints:

1 <= s1.length, s2.length <= 200
s1 and s2 consist of lowercase English letters and spaces.
s1 and s2 do not have leading or trailing spaces.
All the words in s1 and s2 are separated by a single space.

"""


from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # Split the sentences into words
        words1 = s1.split()
        words2 = s2.split()
        
        # Count occurrences of each word
        count1 = Counter(words1)
        count2 = Counter(words2)
        
        # Initialize a list to hold uncommon words
        uncommon_words = []
        
        # Check for uncommon words in the first sentence
        for word in count1:
            if count1[word] == 1 and word not in count2:
                uncommon_words.append(word)
        
        # Check for uncommon words in the second sentence
        for word in count2:
            if count2[word] == 1 and word not in count1:
                uncommon_words.append(word)
        
        return uncommon_words
