"""
You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.

 

Example 1:

Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
Example 2:

Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.
 

Constraints:

2 <= s.length <= 1000
s.length is even.
s consists of uppercase and lowercase letters.

"""

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        N = len(s)
        if N % 2 != 0:
            return False
        mid = N // 2

        first = s[:mid]
        second = s[mid:]

        def check_vowels(s):
            total_sum = 0
            for i in s:
                vowels = "aeiouAEIOU"
                if i in vowels:
                    total_sum = total_sum + 1
            return total_sum
        
        if check_vowels(first) == check_vowels(second):
            return True
        return False
