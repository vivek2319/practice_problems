"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 

Constraints:

0 <= x <= 231 - 1


WHY WE ARE USING LEFT + RIGHT + 1??


Conceptual Understanding
Avoiding Infinite Loops:

When performing binary search, especially when narrowing down the range to find a value, you need to ensure that the loop doesn't get stuck in a situation where left and right are very close (e.g., differing by 1).
Normally, the midpoint is calculated using mid = (left + right) // 2. If left and right are adjacent (e.g., left = 2 and right = 3), this formula gives mid = 2, which might not move left forward, potentially leading to an infinite loop.
Biasing Towards the Upper Half:

Using mid = (left + right + 1) // 2 shifts the midpoint slightly towards the upper half of the current range. This is particularly useful when you need to test the higher midpoint first (e.g., when finding the maximum possible value that satisfies a condition).
How to Remember
Rule of Thumb:

When the condition in the binary search loop (if mid <= condition) means you want to search for the highest possible value that still satisfies the condition, use left + right + 1.


"""




class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        while left < right:
            mid = (left + right + 1) // 2
            if mid <= x // mid:
                left = mid
            else:
                right = mid - 1
        return left
