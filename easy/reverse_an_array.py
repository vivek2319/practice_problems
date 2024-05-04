class Solution(object):
    def reverse_an_array(self, num_arr):
        """
        sample_arr = [11,0,3,24]
        output = [24,3,0,11]
        """
        result = []
        # brute force approach
        for i in range(-1, -len(num_arr)-1, -1):
            result.append(num_arr[i])
        return result


solution_instance = Solution()
arr = [11,0,3,24]
output = solution.reverse_an_array(arr)
print(output)

