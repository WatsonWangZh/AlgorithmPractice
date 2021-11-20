# Given an array of integers, return indices of the two numbers 
# such that they add up to a specific target.
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.
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
        首先判断数组长度是否符合条件
        将list映射为[值：下标]形式，逐个查找
        """
        # M1. 暴力枚举 O(n^2)
        # 两重循环枚举下标 i,j，然后判断 nums[i]+nums[j] 是否等于 target。
        # 时间复杂度：由于有两重循环，所以复杂度是 O(n^2).

        # result = []
        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[i] + nums[j] == target:
        #             result.append(i)
        #             result.append(j)
        #             break
        #     if len(result) > 0:
        #         break
        # return result
        
        # M2. 哈希表 O(n)
        # 循环一遍 nums 数组，在每步循环中我们做两件事：
            # 判断 target−nums[i] 是否在哈希表中；
            # 将 nums[i] 插入哈希表中；
        # 解释：由于数据保证有且仅有一组解，假设是 [i,j](i<j)，则我们循环到 j 时，nums[i]一定在哈希表中，
        #      且有 nums[i]+nums[j]==target， 所以我们一定可以找到解。
        # 时间复杂度：
        #   由于只扫描一遍，且哈希表的插入和查询操作的复杂度是 O(1)，所以总时间复杂度是 O(n).

        if len(nums) < 2:
            return []

        dic = {}

        for cur_index, cur_value in enumerate(nums):
            to_find = target - cur_value
            if to_find in dic:
                return [dic[to_find], cur_index]
            else:
                dic[cur_value] = cur_index 

