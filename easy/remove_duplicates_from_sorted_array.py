class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # Initialize pointer i to track the last unique element
        i = 0
        
        # Iterate through the array with pointer j
        for j in range(1, len(nums)):
            # If nums[j] is different from nums[i], update nums[i+1]
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        # Return the count of unique elements (i+1)
        return i + 1
        
