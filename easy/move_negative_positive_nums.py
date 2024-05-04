class Solution(object):
    def move_negative_and_positive(self, num_arr):
        result = []
        positive_nums = []
        negative_nums = []
        for i in range(len(num_arr)):
            if num_arr[i] < 0:
                negative_nums.append(num_arr[i])
            elif num_arr[i] > 0:
                positive_nums.append(num_arr[i])
        result = negative_nums + positive_nums
        return result


solution_instance = Solution()
arr = [-12, 11, -13, 1, 2, -5, 6, -7, 5, -3, -6]
output = solution_instance.move_negative_and_positive(arr)
print(output)

