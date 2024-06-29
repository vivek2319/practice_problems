"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.

"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Assumes the input list of strings is not empty
        # The outer loop goes through each character of the first string
        for index in range(len(strs[0])):
            # Inner loop checks the character at the current position across all other strings
            for string in strs[1:]:
                # Checks if we have reached the end of any string or a character mismatch is found
                if index >= len(string) or string[index] != strs[0][index]:
                    # return the common longest prefix found so far
                    return strs[0][:index]
        # if no early return happened, the first string itself is the commmon prefix
        return strs[0]
