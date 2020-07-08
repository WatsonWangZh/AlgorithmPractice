# Given an array of integers, return indices of the two numbers 
# such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # M1. 枚举 O(n^2)

        if len(nums) < 2:
            return []

        res = []
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] + nums[j] == target:
                    res.append(i)
                    res.append(j)
                    break
            if len(res) > 0:
                break
        return res

        
        # M2. 哈希表 检查，快速确定互补下标 O(n)

        if len(nums) < 2:
            return []

        d = {}

        for idx, num in enumerate(nums):
            to_find = target - num
            if to_find in d:
                return [d[to_find], idx]
            else:
                d[num] = idx 
                
        return []

