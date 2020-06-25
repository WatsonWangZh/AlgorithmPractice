# Given a 2D binary matrix filled with 0's and 1's, 
# find the largest square containing only 1's and return its area.

# Example:
# Input: 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# Output: 4

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        # DP 时间O(mn) 空间O(mn)
        # 用dp[i][j]记录到达(i, j)位置所能组成的最大正方形的边长
        # 对于任意一点dp[i][j]，由于该点是正方形的右下角，
        # 所以该点的右边，下边，右下边都不用考虑，关心的就是左边，上边，和左上边，
        # 只有当前(i, j)位置为1，dp[i][j]才有可能大于0，否则dp[i][j]一定为0。当(i, j)位置为1，
        # 此时要看dp[i-1][j-1], dp[i][j-1]，和dp[i-1][j]这三个位置，我们找其中最小的值，并加上1，就是dp[i][j]的当前值了。
        # 最后再用dp[i][j]的值来更新结果maxlen的值即可。

        if not matrix or not matrix[0]:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * (cols+1) for _ in range(rows+1)]
        maxlen = 0
        for i in range(1, rows+1):
            for j in range(1, cols+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1
                    maxlen = max(maxlen, dp[i][j])
        return maxlen ** 2