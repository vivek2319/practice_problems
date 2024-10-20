"""
You are given a string target . Alice is going to type target on her computer using a special keyboard that has only two keys: • Key 1 appends the character "a" to the string on the screen. • Key 2 changes the last character of the string on the screen to its next character in the English alphabet. For example, "c" changes to "d" and "z" changes to "a" . Note that initially there is an empty string "" on the screen, so she can only press key 1. 
Return a list of all strings that appear on the screen as Alice types target, in the order they appear, using the minimum key presses. 
Example 1: Input target = "abc" Output: ["a","aa","ab","aba","abb","abc"] Explanation: The sequence of key presses done by Alice are: 

• Press key 1. and the string on the screen becomes "a" . • Press key 1. and the string on the screen becomes "aa" . • Press key 2. and the string on the screen becomes "ab" . • Press key 1. and the string on the screen becomes "aba" . • Press key 2. and the string on the screen becomes "abb" . • Press key 2. and the string on the screen becomes "abc" . Example 2: Input: target = "he" Output: [a", "b""c", "d""e", "f","g", "h""ha""hb""hc", "hd", "he] 
Constraints: • 1 <= target. length <= 400 • target consists only of lowercase English letters. 




def stringsequence(self, target:str) -> List[str]


To implement the stringsequence function, the idea is to simulate Alice's keypresses and generate the strings on the screen step by step. The two keys work as follows:

Key 1: Appends 'a' to the current string.
Key 2: Changes the last character to the next character in the alphabet.
We want to build up to the target string using the fewest key presses. Here's how we can think about solving this:

Start with an empty string.
Keep track of each step and every intermediate string that Alice types by pressing the appropriate key.
Append 'a' (Key 1) at each step, and if needed, use Key 2 to change the last character to match the next character in the target string.
Plan:
For each character in the target, simulate the necessary keypresses to match that character.
For every character, append 'a' using Key 1.
If the current character in the string on the screen doesn't match the target, use Key 2 until it matches.
"""

from typing import List

class Solution:
    def stringsequence(self, target: str) -> List[str]:
        result = []   # To store all intermediate strings
        current_string = ""  # The string on the screen

        for char in target:
            # Append 'a' (Key 1 press)
            current_string += 'a'
            result.append(current_string)  # Add the current string after Key 1 press
            
            # Use Key 2 to change the last character to the target character
            while current_string[-1] != char:
                current_string = current_string[:-1] + chr(((ord(current_string[-1]) - ord('a') + 1) % 26) + ord('a'))
                result.append(current_string)  # Add the string after each Key 2 press

        return result
