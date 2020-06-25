# Find all possible combinations of k numbers that add up to a number n, 
# given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
# Note:
# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.

# Example 1:
# Input: k = 3, n = 7
# Output: [[1,2,4]]

# Example 2:
# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]

class Solution(object):
    # DFS O(C9k)
    # 暴力搜索出所有从9个数中选k个的方案，记录所有和等于 n 的方案。
    # 为了避免重复计数，比如 {1, 2, 3} 和 {1, 3, 2} 是同一个集合，对集合中的数定序，每次枚举时，要保证同一方案中的数严格递增，
    # 即如果上一个选的数是 x，那我们从 x+1 开始枚举当前数
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        candidates = list(range(1, 10))
        self.dfs(candidates, 0, n, res, [], k)
        return res

    def dfs(self, nums, index, target, res, cur, k):
        if target < 0:
            return
        if target == 0:
            if len(cur) == k:
                res.append(cur)
            return
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            self.dfs(nums, i + 1, target - nums[i], res, cur + [nums[i]], k)
