# Given an array of n positive integers and a positive integer s, 
# find the minimal length of a contiguous subarray of which the sum ≥ s. 
# If there isn't one, return 0 instead.

# Example: 
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.
# Follow up:
# If you have figured out the O(n) solution, 
# try coding another solution of which the time complexity is O(n log n). 

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # 滑动窗口 遍历
        res = len(nums) + 1
        total, left = 0, 0
        for i in range(len(nums)):
            total += nums[i]
            while total >= s:
                right = i
                res = min(res, right-left+1)
                total -= nums[left]
                left += 1
        return res if res <= len(nums) else 0
