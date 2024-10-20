"""
Q2. Count Substrings With K-Frequency Characters I 
5 pt. 
Given a string s and an integer k, return the total number of substrings of s where at least one character appears at least k times. 
A substring is a contiguous non-empty sequence of characters within a string. 
Example 1: Input s = "abacb" , k = 2 Output: 4 Explanation: The valid substrings are: • "aba" (character 'a' appears 2 times). • "abac" (character 'a' appears 2 times). 


• "abacb" (character 'a' appears 2 times). • "bacb" (character 'b' appears 2 times). Example 2: Input s = "abcde", k = 1 Output: 15 Explanation: All substrings are valid because every character appears at least once. 
Constraints: 
• 1 a s. length <= 3000 • 1 a k a s. length • s consists only of lowercase English letters. 


def numberOfSubstrings(self, s: str, k: int) -> int:

We can make use of a sliding window technique along with character frequency counting to improve efficiency. Instead of checking every substring explicitly, we can maintain a dynamic window and expand it while tracking the frequency of characters. Here's the plan:

Sliding Window: We'll maintain a window using two pointers, start and end. The end pointer will expand the window, and we'll update the frequency of characters within the window.
Frequency Map: We maintain a count of characters using a frequency map (dictionary). When the count of any character in the window reaches k, we know that the window (and all subsequent windows) will contain a valid substring.
Efficient Counting: Once we encounter a valid window, we can count all substrings that start from the current start position and end at any index greater than or equal to end. Instead of recalculating frequencies for each possible substring, we just slide the window and make incremental updates.

Explanation of Optimizations:
Sliding Window:
We use the end pointer to expand the window by adding characters to the frequency map.
If a character's frequency in the window reaches k, we calculate how many valid substrings can be formed with the current window.
Count Substrings:
Once we know the window is valid (i.e., contains a character appearing at least k times), all substrings from start to end are valid. We add n - end to the count, which is the number of valid substrings that can be formed from this window.
Shrinking the Window:
After counting, we move the start pointer to shrink the window and keep searching for new valid windows.
Example Walkthrough:
For s = "abacb", k = 2:

Start at index 0 (start = 0), expand the window by moving end:
end = 0, window is "a" → no character appears k times.
end = 1, window is "ab" → no character appears k times.
end = 2, window is "aba", 'a' appears 2 times. We count all substrings from start = 0 to end = 2: aba, abac, abacb.
Move start to 1 and continue.
Continue this process until all valid substrings are counted.

"""

from collections import defaultdict
class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        count = 0  
        start = 0  
        freq = defaultdict(int)  

        for end in range(n):
            # Expand the window by including s[end]
            freq[s[end]] += 1

            # Shrink the window if any character in the window appears >= k times
            while any(freq[char] >= k for char in freq):
                # Count all substrings from 'start' to 'end'
                count += n - end
                # Shrink the window from the left
                freq[s[start]] -= 1
                start += 1

        return count
