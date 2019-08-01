# Given a non-empty integer array, 
# find the minimum number of moves required to make all array elements equal, 
# where a move is incrementing a selected element by 1 or decrementing a selected element by 1.
# You may assume the array's length is at most 10,000.

# Example:
# Input:
# [1,2,3]
# Output:
# 2
# Explanation:
# Only two moves are needed (remember each move increments or decrements one element):
# [1,2,3]  =>  [2,2,3]  =>  [2,2,2]

class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 排序,分奇偶找中值，其他数到中值的距离之和即为res
        nums.sort()
        res = 0

        if len(nums)%2 == 0:
            mid = (nums[len(nums)//2-1] + nums[len(nums)//2]) // 2
        else:
            mid = nums[len(nums)//2]

        for num in nums:
            res += abs(num - mid)
        return res
        