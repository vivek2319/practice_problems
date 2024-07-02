"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

from collections import defaultdict

class Solution:
    def group_anagrams(self, strs):
        # A dictionary that automatically creates a new list entry for each new key
        anagrams = defaultdict(list)
      
        # Iterate through each string in the provided list
        for s in strs:
            # Sort the string to create a key for the anagrams
            # Since sorted returns a list of characters, join them to form a string
            key = "".join(sorted(s))
          
            # Append the original string to the list of anagrams with the same key
            anagrams[key].append(s)
      
        # Convert the dictionary values to a list and return it
        return list(anagrams.values())
