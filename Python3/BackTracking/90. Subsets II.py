# Given a collection of integers that might contain duplicates, nums, 
# return all possible subsets (the power set).
# Note: The solution set must not contain duplicate subsets.

# Example:
# Input: [1,2,2]
# Output:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]
import collections
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        nums.sort()
        self.helper(nums, res, [], 0)
        return res
    
    def helper(self, nums, temp, res, startIdx):
        if not nums:
            return
        # res.append(temp[:])
        for i in range(startIdx, len(nums)):
            if i != startIdx and nums[i] == nums[i-1]:
                continue
            res.append(temp[:])
            temp.append(nums[i])
            self.helper(nums, temp, res, i + 1)
            temp.pop()
