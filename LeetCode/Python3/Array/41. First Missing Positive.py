# Given an unsorted integer array, find the smallest missing positive integer.

# Example 1:
# Input: [1,2,0]
# Output: 3

# Example 2:
# Input: [3,4,-1,1]
# Output: 2

# Example 3:
# Input: [7,8,9,11,12]
# Output: 1

# Note:
# Your algorithm should run in O(n) time and uses constant extra space.

# Hints:
# Think about how you would solve the problem in non-constant space. 
# Can you apply that logic to the existing space?
# We don't care about duplicates or non-positive integers.
# Remember that O(2n) = O(n)

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 桶排序 O(n)
        # 不用额外空间的桶排序：
        # 保证1出现在nums[0]的位置上，2出现在nums[1]的位置上，…，n出现在nums[n-1]的位置上，其他的数字不管。
        # 例如[3,4,-1,1]将被排序为[1,-1,3,4]
        # 遍历nums，找到第一个不在应在位置上的1到n的数。
        # 例如，排序后的[1,-1,3,4]中第一个 nums[i] != i + 1 的是数字2（注意此时i=1）。
        # 时间复杂度分析：
        # 代码中while循环，每循环一次，会将一个数放在正确的位置上，所以总共最多执行 n 次，所以总时间复杂度 O(n)。

        length = len(nums)

        for i in range(length):
            while 0 < nums[i] <= length and \
              nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(length):
            if i + 1 != nums[i]:
                return i + 1

        return length + 1