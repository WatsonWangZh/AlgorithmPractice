# Alex and Lee play a game with piles of stones.  
# There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].
# The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.
# Alex and Lee take turns, with Alex starting first.  
# Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.  
# This continues until there are no more piles left, at which point the person with the most stones wins.
# Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.

# Example 1:
# Input: [5,3,4,5]
# Output: true
# Explanation: 
# Alex starts first, and can only take the first 5 or the last 5.
# Say he takes the first 5, so that the row becomes [3, 4, 5].
# If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
# If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
# This demonstrated that taking the first 5 was a winning move for Alex, so we return true.
 
# Note:
# 2 <= piles.length <= 500
# piles.length is even.
# 1 <= piles[i] <= 500
# sum(piles) is odd.

class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        # M1. 数学分析 先手优势 + 奇数限制 O(1)

        # return True

        # M2. Min_Max: Both you and opponent take the best move.
        # 自底向上求解 TLE 26/46 passed 
        # 时间复杂度: O(2^n) 空间复杂度: O(n)

        # n = len(piles)
        # def score(s, l, r):
        #     if l > r:
        #         return 0
        #     if l == r:
        #         return s[l]
        #     return max(s[l] - score(s, l+1, r), # left
        #                s[r] - score(s, l, r-1)) # right
        # return score(piles, 0, n - 1) > 0

        # M3. Min_Max + 记忆化递归
        # 时间复杂度: O(n^2) 空间复杂度: O(n^2)

        # n = len(piles)
        # memo = [[float('-inf')] * n for i in range(n)]
        # def score(s, l, r):
        #     if l > r:
        #         return 0
        #     if l == r:
        #         return s[l]
        #     if memo[l][r] == float('-inf'):
        #         memo[l][r] = max(s[l] - score(s, l+1, r), # left
        #                        s[r] - score(s, l, r-1)) # right
        #     return memo[l][r]
        # return score(piles, 0, n-1)
       
        # M4. DP
        # 时间复杂度: O(n^2) 空间复杂度: O(n^2)

        # n = len(piles)
        # dp = [[0] * n for i in range(n)]
        # for i in range(n):
        #     dp[i][i] = piles[i]
        # for l in range(2, n+1):
        #     for i in range(n-l+1):
        #         j = i + l - 1
        #         dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
        # return dp[0][n-1] > 0

        # M5. DP + 滚动数组 空间优化
        # 时间复杂度: O(n^2) 空间复杂度: O(n)

        n = len(piles)
        dp = piles
        for l in range(2, n+1):
            for i in range(n-l+1):
                dp[i] = max(piles[i] - dp[i+1], piles[i+l-1] - dp[i])
        return dp[0] > 0
