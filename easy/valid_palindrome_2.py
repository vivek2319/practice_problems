"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.

"""
class Solution:
    def validPalindrome(self, string: str) -> bool:
        # Helper function to check if substring string[left:right+1] is a palindrome
        def is_palindrome(left, right):
            while left < right:
                if string[left] != string[right]:
                    return False
                left, right = left + 1, right - 1
            return True

        left, right = 0, len(string) - 1  # Initialize pointers at both ends of the string

        # Iterate while the two pointers don't cross each other
        while left < right:
            # If the characters at the current pointers don't match
            if string[left] != string[right]:
                # Check for palindrome by removing one character - either from the left or right
                # If either case returns true, the function returns true
                return is_palindrome(left, right - 1) or is_palindrome(left + 1, right)
            # Move both pointers towards the center
            left, right = left + 1, right - 1

        # If the string is a palindrome or can be made into one by removing a single character
        return True

        
