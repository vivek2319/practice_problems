class Solution:
     def reverseWord(self, str: str) -> str:
        # In-place string reversal using slicing
        rev = ""
        for i in range(len(str)-1, -1, -1):
            rev += str[i]
        return rev

