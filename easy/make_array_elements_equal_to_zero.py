"""
You are given an integer array ruts . 
Start by selecting a starting position CJ rr such that nums [curr] == 0, and choose a movement direction of either left or right. 
After that, you repeat the following process: • If curr is out of the range [0, n - 1] , this process ends. • If nums [curl-] == 0. move in the current direction by incrementing curr if you are moving right, or decrementing curr if you are moving left. 
• Else if nums [curr] > 0: • Decrement nums ECU r r] by 1. 
• Reverse your movement direction (left becomes right and vice versa). 
• Take a step in your new direction. 
A selection of the initial position curr and movement direction is considered valid if every element in tlJTS becomes 0 by the end of the process. 
Return the number of possible valid selections. 


Example 1: Input: nums = [1,0,2,0,3] Output: 2 Explanation: The only possible valid selections are the following: 
• Choose curr = 
3, and a movement direction to the left. 
• [1,0,2,1,3] -> [1,0,2,0,3] -> [1,0,1,0,3] -> [1,0,1,0,3] -> [1,0,1,0,2] -> [1,0,1,0,2] -> [1,0,0,0,2] -> [1,0,0,0,21 -> [1,0,0,0,1] -> [1,0,0,0,1] -> [1,Q,0,0,1] -> [1,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,0]. • Choose curr = 3, and a movement direction to the right. • [1,0,2,1,3] -> [1,0,2,0,31 -> [1,0,2,0,2] -> [1,0,2,0,2] -> [1,0,1,0,2] -> [1,0,1,0,2] -> [1,0,1,0,1] -> [1,0,1,0,11 -> [1,0,0,0,1] -> [1,0,0,0,1] -> [1,0,0,1,0] -> [1,0,0,0,0] -> [1,0,0,0,0] -> [1,0,0,0,0] -> [0,0,0,0,0]. 
• 


Example 2: Input: nums = [2,3,4,0,4,1,0] Output: 0 Explanation: There are no possible valid selections. 
Constraints: • 1 <= nums. length <= • 0 <= nums (1) <= 100 • There is at least one element 2. where nuns [1) == 0. 

"""

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        def can_zero_out(start, direction):
            temp_nums = nums[:]
            curr = start

            while 0 <= curr < len(temp_nums):
                if temp_nums[curr] == 0:
                    curr = curr + direction
                else:
                    temp_nums[curr] = temp_nums[curr] - 1
                    direction = direction * (-1)
                    curr = curr + direction
            return all(x==0 for x in temp_nums)
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if can_zero_out(i, -1):
                    count = count + 1
                if can_zero_out(i, 1):
                    count = count + 1
        return count
