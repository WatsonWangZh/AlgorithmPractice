# Given an array of integers that is already sorted in ascending order, 
# find two numbers such that they add up to a specific target number.
# The function twoSum should return indices of the two numbers 
# such that they add up to the target, where index1 must be less than index2.

# Note:
# Your returned answers (both index1 and index2) are not zero-based.
# You may assume that each input would have exactly one solution 
# and you may not use the same element twice.

# Example:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # M1. 哈希表 O(n)
        # 循环一遍 nums 数组，在每步循环中我们做两件事：
            # 判断 target−nums[i] 是否在哈希表中；
            # 将 nums[i] 插入哈希表中；
        # 解释：由于数据保证有且仅有一组解，假设是 [i,j](i<j)，则我们循环到 j 时，nums[i]一定在哈希表中，
        #      且有 nums[i]+nums[j]==target， 所以我们一定可以找到解。
        # 时间复杂度：
        #   由于只扫描一遍，且哈希表的插入和查询操作的复杂度是 O(1)，所以总时间复杂度是 O(n).

        # if len(numbers) < 2:
        #     return []

        # dic = {}

        # for cur_index, cur_value in enumerate(numbers):
        #     to_find = target - cur_value
        #     if to_find in dic:
        #         return [dic[to_find] + 1, cur_index + 1]
        #     else:
        #         dic[cur_value] = cur_index

        # M2. 双指针扫描 O(n)
        # 用两个指针 i,j 分别从数组首尾往中间扫描，
        #   每次将 i 后移一位，然后不断前移 j，直到 numbers[i]+numbers[j]≤target 为止。
        #   如果 numbers[i]+numbers[j]==target，则找到了一组方案。
        # 时间复杂度分析：
        #   两个指针总共将数组扫描一次，所以时间复杂度是 O(n)。

        i = 0
        j = len(numbers) - 1
        while(i or j):
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            elif  numbers[i] + numbers[j] < target:
                i = i+1
            else:
                j = j-1
