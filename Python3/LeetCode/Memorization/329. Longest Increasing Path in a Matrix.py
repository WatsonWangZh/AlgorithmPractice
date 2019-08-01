# Given an integer matrix, find the length of the longest increasing path.
# From each cell, you can either move to four directions: left, right, up or down.
# You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

# Example 1:
# Input: nums = 
# [
#   [9,9,4],
#   [6,6,8],
#   [2,1,1]
# ] 
# Output: 4 
# Explanation: The longest increasing path is [1, 2, 6, 9].

# Example 2:
# Input: nums = 
# [
#   [3,4,5],
#   [3,2,6],
#   [2,2,1]
# ] 
# Output: 4 
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

class Solution:
    # 这道题给我们一个二维数组，让我们求矩阵中最长的递增路径，
    # 规定我们只能上下左右行走，不能走斜线或者是超过了边界。
    # 那么这道题的解法要用递归和DP来解，用DP的原因是为了提高效率，
    # 避免重复运算。我们需要维护一个二维动态数组dp，其中dp[i][j]表示数组中以(i,j)为起点的
    # 最长递增路径的长度，初始将dp数组都赋为0，当我们用递归调用时，遇到某个位置(x, y), 
    # 如果dp[x][y]不为0的话，我们直接返回dp[x][y]即可，不需要重复计算。
    # 我们需要以数组中每个位置都为起点调用递归来做，比较找出最大值。
    # 在以一个位置为起点用DFS搜索时，对其四个相邻位置进行判断，如果相邻位置的值大于上一个位置，
    # 则对相邻位置继续调用递归，并更新一个最大值，搜素完成后返回即可。


    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        M, N = len(matrix), len(matrix[0])
        dp = [[0]*N for i in range(M)]

        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(
                    dfs(i-1, j) if i and val > matrix[i-1][j] else 0,
                    dfs(i+1, j) if i < M-1 and val > matrix[i+1][j] else 0,
                    dfs(i, j-1) if j and val > matrix[i][j-1] else 0,
                    dfs(i, j+1) if j < N-1 and val > matrix[i][j+1] else 0
                )
            return dp[i][j]

        return max(dfs(x, y) for x in range(M) for y in range(N))
