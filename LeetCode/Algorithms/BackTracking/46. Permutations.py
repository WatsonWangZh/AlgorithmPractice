# Given a collection of distinct integers, return all possible permutations.
# Example:
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

class Solution(object):
    # 回溯 O(n×n!)
    # 我们从前往后，一位一位枚举，每次选择一个没有被使用过的数。
    # 选好之后，将该数的状态改成“已被使用”，同时将该数记录在相应位置上，然后递归。
    # 递归返回时，不要忘记将该数的状态改成“未被使用”，并将该数从相应位置上删除。
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        temp = []
        visited = [False] * len(nums)
        self.dfs(nums, 0, temp, res, visited)
        return res

    def dfs(self, nums, pos, temp, res, visited):
        if pos == len(nums):
            res.append(temp[:])
            return 

        for i in range(len(nums)):
            if not visited[i]:
                visited[i] = True
                temp.append(nums[i])
                self.dfs(nums, pos+1, temp, res, visited)
                visited[i] = False
                temp.pop()
