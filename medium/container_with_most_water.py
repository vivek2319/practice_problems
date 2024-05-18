"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result = 0 # 
        left_pointer, right_pointer = 0, len(height) - 1
        
        while left_pointer < right_pointer:
            width = right_pointer - left_pointer
            area = width * min(height[left_pointer], height[right_pointer])
            # Update the maximum water capacity if the current container holds more water
            result = max(result, area)

            # Move the pointers towards each other
            if height[left_pointer] < height[right_pointer]:
                left_pointer = left_pointer + 1
            elif height[left_pointer] > height[right_pointer]:
                right_pointer = right_pointer - 1
            else:
                # they are equal
                right_pointer = right_pointer - 1
        return result
