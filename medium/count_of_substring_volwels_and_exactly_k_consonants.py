"""
You are given a string word and a non-negative integer k . 
Return the total number of substrings of word that contain every vowel ( 'a ' , 'e' , ' i' , 'o' , and 'u ' ) at least once and exactly k consonants. 
Example 1: Input: word = "aeioqq", k = 1 Output: 0 Explanation: There is no substring with every vowel. 


Example 2: Input: word = "aeiou", k = 0 Output: 1 Explanation: 
The only substring with every vowel and zero consonants is word [0..4] , which is "aeiou" . 
Example 3: Input: word = "ieaouqqieaouqq", k = 1 Output: 3 Explanation: The substrines with every vowel and one consonant are: 

Example 3: Input: word = "ieaouqqieaouqq", k = 1 Output: 3 Explanation: The substrings with every vowel and one consonant are: • word [0..5] , which is "ieaouq" . • word [6..11] , which is "gieaou" . • word [7..12] which is "ieaouq" 
"""

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:       
        vowels = {'a', 'e', 'i', 'o', 'u'}
        total_substrings = 0
        
        for start in range(len(word)):
            found_vowels = set()
            consonant_count = 0
            
            # Expand the window from 'start' to the end of the string
            for end in range(start, len(word)):
                char = word[end]
                
                # Check if the character is a vowel
                if char in vowels:
                    found_vowels.add(char)
                else:
                    consonant_count += 1
                
                # Check if the window has all vowels and exactly k consonants
                if len(found_vowels) == 5 and consonant_count == k:
                    total_substrings += 1
        
        return total_substrings
