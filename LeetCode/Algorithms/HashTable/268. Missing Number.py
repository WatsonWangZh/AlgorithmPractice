# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
# find the one that is missing from the array.

# Example 1:
# Input: [3,0,1]
# Output: 2

# Example 2:
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
# Note:
# Your algorithm should run in linear runtime complexity.
# Could you implement it using only constant extra space complexity?

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # M1.数学方法
        # n = len(nums)
        # sum1 = sum(nums)
        # sums = (n+1) * n / 2
        # return sums - sum1
        # M2.位运算方法 缺失数组异或完整数组
        missing =  len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing 

