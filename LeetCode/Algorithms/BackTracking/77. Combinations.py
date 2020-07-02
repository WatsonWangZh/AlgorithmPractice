# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

# Example:
# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        # DFS 
        # 深度优先搜索，每层枚举第 u 个数选哪个，一共枚举 k 层。
        # 由于这道题要求组合数，不考虑数的顺序，所以我们需要再记录一个值 start，表示当前数需要从几开始选，来保证所选的数递增。

        if k > n:
            return []

        res = []
        def dfs(n, k, res, cur, start):
            if len(cur) == k:
                res.append(cur[:])
                return
            for i in range(start, n+1):
                cur.append(i)
                dfs(n, k, res, cur, i+1)
                cur.pop()
        dfs(n, k, res, [], 1)

        return res