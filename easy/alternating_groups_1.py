"""
There is a circle of red and blue tiles. You are given an array of integers colors. The color of tile i is represented by colors[i]:

colors[i] == 0 means that tile i is red.
colors[i] == 1 means that tile i is blue.
Every 3 contiguous tiles in the circle with alternating colors (the middle tile has a different color from its left and right tiles) is called an alternating group.

Return the number of alternating groups.

Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.

 

Example 1:

Input: colors = [1,1,1]

Output: 0

Explanation:



Example 2:

Input: colors = [0,1,0,0,1]

Output: 3

Explanation:
Alternating groups:
Constraints:

3 <= colors.length <= 100
0 <= colors[i] <= 1
"""

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        
        n = len(colors)
        
        if n < 3:
            return 0  # There can't be alternating groups if there are fewer than 3 colors
        
        start = 0
        end = 2
        count = 0

        while start < n:
            # To handle circular indexing, use modulo to wrap around
            if colors[start] == colors[end % n] and colors[(start + 1) % n] != colors[start]:
                count += 1

            start += 1
            end += 1

        return count
