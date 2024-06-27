"""
Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.

 

Example 1:

Input: s = "(1+(2*3)+((8)/4))+1"

Output: 3

Explanation:

Digit 8 is inside of 3 nested parentheses in the string.

Example 2:

Input: s = "(1)+((2))+(((3)))"

Output: 3

Explanation:

Digit 3 is inside of 3 nested parentheses in the string.

Example 3:

Input: s = "()(())((()()))"

Output: 3

 

Constraints:

1 <= s.length <= 100
s consists of digits 0-9 and characters '+', '-', '*', '/', '(', and ')'.
It is guaranteed that parentheses expression s is a VPS.

"""
class Solution:
    def maxDepth(self, s: str) -> int:
        # Initialize variables to store the current depth and maximum depth
        max_depth = current_depth = 0
      
        # Iterate through each character in the string
        for char in s:
            if char == '(':  # If the character is an opening bracket
                current_depth += 1  # Increase the current depth by 1
                max_depth = max(max_depth, current_depth)  # Update the max depth if needed
            elif char == ')':  # If the character is a closing bracket
                current_depth -= 1  # Decrease the current depth by 1
              
        # Return the maximum depth encountered
        return max_depth
