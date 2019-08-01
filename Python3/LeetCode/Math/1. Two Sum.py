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
        if len(nums) < 2:
            return []
        dic = {}
        for cur_index,cur_value in enumerate(nums):
            to_find = target - cur_value
            if to_find in dic:
                return [dic[to_find],cur_index]
            else:
                dic[cur_value] = cur_index 

def main():
    print(Solution().twoSum([2,7,11,15],9))

if __name__ == '__main__': 
    main()