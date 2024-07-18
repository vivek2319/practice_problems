"""
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

 

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
 

Constraints:

1 <= k <= num.length <= 105
num consists of only digits.
num does not have any leading zeros except for the zero itself.
"""

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # Initialize a stack to keep track of the digits
        stack = []
      
        # Number of digits to remain in the final number
        remaining_digits_count = len(num) - k
      
        # Iterate over each character in the input string
        for digit in num:
            # While we can still remove digits, and the stack is not empty,
            # and the current digit is smaller than the last digit in the stack:
            while k and stack and stack[-1] > digit:
                # Remove the last digit from the stack as it's greater than the current one
                stack.pop()
                # Decrease the count of digits we can remove
                k = k - 1
            # Add the current digit to the stack
            stack.append(digit)
      
        # Build the final number string from the stack up to the remaining digits
        final_number = ''.join(stack[:remaining_digits_count])
      
        # Strip leading zeros from the final number and return it, or return '0' if empty
        return final_number.lstrip('0') or '0'
        
