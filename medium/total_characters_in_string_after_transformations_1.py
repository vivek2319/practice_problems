"""
You are given a string s and an integer t, representing the number of transformations to
perform. In one transformation, every character in s is replaced according to the following rules:
© Ifthe character is 'z', replace it with the string "ab".
© Otherwise, replace it with the next character in the alphabet. For example, 'a' is replaced with
‘b', 'b' is replaced with 'c', and so on,
Return the length of the resulting string after exactly t transformations.
Since the answer may be very large, return it modulo 109 + 7.
Example 1:
Input:s = "abcyy", t = 2
Output: 7
Explanation:
* First Transformation (t = 1):
* 'a' becomes 'b'


* 'h' becomes 'c'

* 'c' becomes 'd'

e 'y' becomes 'z'

e 'y' becomes 'z'

© String after the first transformation: “bcdzz"
© Second Transformation (t = 2):

* 'h' becomes 'c'

* 'c' becomes 'd'

« 'd' becomes '‘e'

© 'z' becomes “ab"

© 'z' becomes “ab"

© String after the second transformation: “cdeabab"
© Final Length of the string: The string is "“cdeabab" . which has 7 characters.

Example 2:
Input:s = "azbk", t = 1
Output: 5
Explanation:
© First Transformation (t = 1):
* ‘at becomes '‘h'
© 'z' becomes "ab"
© 'h' becomes 'c'
* 'k' becomes ‘1°
© String after the first transformation: "babcl"
¢ Final Length of the string: The string is "babc1", which has 5 characters.

Constraints:

¢ 1 <= s.length <= 10°

© s consists only of lowercase English letters,
e 1<st <= 105


class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
"""

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        char_counts = [0] * 26
        for c in s:
            char_counts[ord(c) - ord('a')] += 1

        for _ in range(t):
            new_counts = [0] * 26
            for i in range(25):
                new_counts[i + 1] += char_counts[i]
            new_counts[0] += char_counts[25]
            new_counts[1] += char_counts[25]
            char_counts = new_counts

        return sum(char_counts) % MOD
