class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # First approach
        """
        nums1.sort()
        nums2.sort()
        first_pointer = 0
        second_pointer = 0
        result = []
        while first_pointer < len(nums1) and second_pointer < len(nums2):
            if nums1[first_pointer] == nums2[second_pointer]:
                result.append(nums1[first_pointer])
                result.append(nums2[second_pointer])
                first_pointer = first_pointer + 1
                second_pointer = second_pointer + 1
            elif nums1[first_pointer] < nums2[second_pointer]:
                first_pointer = first_pointer + 1
            elif nums1[first_pointer] > nums2[second_pointer]:
                second_pointer = second_pointer + 1
        return result if result else [0,0]
        """ 
        # The caveat is that the length could be diff
        # Use a set to efficiently store unique elements from the shorter array
        set_of_nums1 = set(nums1)
        set_of_nums2 = set(nums2)

        result = [0,0]

        for i in nums1:
            if i in set_of_nums2:
                result[0] = result[0] + 1
        
        for i in nums2:
            if i in set_of_nums1:
                result[1] = result[1] + 1

        return result
