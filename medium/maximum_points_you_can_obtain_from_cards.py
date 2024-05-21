"""
There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.
In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.
Your score is the sum of the points of the cards you have taken.
Given the integer array cardPoints and the integer k, return the maximum score you can obtain.
"""

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # Initialize the window
        left_pointer = 0
        right_pointer = len(cardPoints) - k
        total = sum(cardPoints[right_pointer:])
        result = total

        while right_pointer < len(cardPoints):
            total = total + (cardPoints[left_pointer] - cardPoints[right_pointer])
            result = max(result,total)
            left_pointer = left_pointer + 1
            right_pointer = right_pointer + 1
        return result
