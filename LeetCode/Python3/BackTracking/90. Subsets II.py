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

class Solution(object):
    # M1.递归
    # DFS，在78题基础上将nums排序。然后判断当前元素nums[i]是否和nums[i-1]相等，若相等，跳出此次循环继续下一次循环。
    # def subsetsWithDup(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: List[List[int]]
    #     """
    #     nums.sort()
    #     res = [[]]
    #     self.dfs(nums, [], res)
    #     return res
    
    # def dfs(self, nums, temp, res):
    #     if not nums:
    #         return
    #     for i in range(len(nums)):
    #         if i > 0 and nums[i] == nums[i-1]:
    #             continue
    #         temp.append(nums[i])
    #         res.append(temp[:])
    #         self.dfs(nums[i+1:], temp, res)
    #         temp.pop()

    # M2.非递归
    # 类似于层次添加元素[] → [1] → [2], [1, 2] → [1,2], [2,2]....
    # 若当前元素和上一个元素相等，则本轮 应该从[添加上一个元素]之后的位置添加该元素。
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = [[]]
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                l = len(res)
            for path in res[len(res)-l:]:
                res.append(path + [nums[i]])
        return res


