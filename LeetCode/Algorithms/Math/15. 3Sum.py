# Given an array nums of n integers, 
# are there elements a, b, c in nums such that a + b + c = 0? 
# Find all unique triplets in the array which gives the sum of zero.

# Note:
# The solution set must not contain duplicate triplets.

# Example:
# Given array nums = [-1, 0, 1, 2, -1, -4],
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

class Solution(object):
     def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # M1. 双指针法
        # 固定其中一位，转化为双指针问题
        res = set() # 去除重复结果
        nums.sort()

        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            low, high = i + 1, len(nums) - 1
            while low < high:
                s = nums[i] + nums[low] + nums[high]
                if s > 0:
                    high -= 1
                elif s < 0:
                    low += 1
                else:
                    res.add((nums[i], nums[low], nums[high]))
                    low += 1
                    high -= 1

        return list(res)