"""
Given two integer arrays nums1 and nums2, return an array of their 
intersection
. Each element in the result must be unique and you may return the result in any order.
"""
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []

        for i in nums1:
            if i in nums2:
                result.append(i)

        for i in nums2:
            if i in nums1:
                result.append(i)
        result = set(result)
        return result
