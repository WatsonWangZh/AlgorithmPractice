# Given a set of distinct integers, nums, return all possible subsets (the power set).
# Note: The solution set must not contain duplicate subsets.

# Example:
# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

class Solution(object):
    # M1.递归
    # def subsets(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     res = [[]]
    #     self.dfs(nums, [], res)
    #     return res

    # def dfs(self, nums, temp, res):
    #     if not nums:
    #         return
    #     for i in range(len(nums)):
    #         temp.append(nums[i])
    #         res.append(temp[:]) # deepcopy
    #         self.dfs(nums[i+1:], temp, res)
    #         temp.pop()

    # M2.非递归
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """    
        res = [[]]
        for num in nums:
            # print("before:",res)
            res += [temp + [num] for temp in res]
            # print("after:",res)
        return res