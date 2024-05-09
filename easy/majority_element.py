class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return_dict = {}
        half = len(nums) / 2
        for i in nums:
            if i not in return_dict:
                return_dict[i] = 0
            else:
                return_dict[i] = return_dict[i] + 1
        return max(return_dict, key=lambda k: return_dict[k])
