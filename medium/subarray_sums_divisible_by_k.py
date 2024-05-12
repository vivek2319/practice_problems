class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_dict = {0:1}
        result = 0
        current = 0

        for n in nums:
            current = current + n
            remainder = current % k

            if remainder in prefix_dict:
                result = result + prefix_dict[remainder]
                prefix_dict[remainder] = prefix_dict[remainder] + 1
            else:
                prefix_dict[remainder] = 1
        return result
