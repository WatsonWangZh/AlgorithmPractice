# Given an array of size n, find the majority element. 
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and the majority element always exist in the array.

# Example 1:
# Input: [3,2,3]
# Output: 3

# Example 2:
# Input: [2,2,1,1,1,2,2]
# Output: 2
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # M1. 排序后取正中间
        # nums.sort()
        # return nums[len(nums)/2]

        # M2. moore 投票算法, 也叫同归于尽法
        candidate = None
        count = 0
        for num in nums:
            if num == candidate:
                count += 1
            elif count > 0:
                count -= 1
            else:
                candidate, count = num, 1
        return candidate
