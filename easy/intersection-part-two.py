"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must 
appear as many times as it shows in both arrays and you may return the result in any order.
"""
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result_dict = {}

        for i in nums1:
            if i not in result_dict:
                result_dict[i] = 1
            else:
                result_dict[i] = result_dict[i] + 1
        
        intersection = []
        for i in nums2:
            if i in result_dict and result_dict[i] > 0:
                intersection.append(i)
                result_dict[i] = result_dict[i] - 1
        
        return intersection 
