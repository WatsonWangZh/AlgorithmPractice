# You are given coins of different denominations and a total amount of money. 
# Write a function to compute the number of combinations that make up that amount. 
# You may assume that you have infinite number of each kind of coin.

# Example 1:
# Input: amount = 5, coins = [1, 2, 5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1

# Example 2:
# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.

# Example 3:
# Input: amount = 10, coins = [10] 
# Output: 1
 
# Note:
# You can assume that
# 0 <= amount <= 5000
# 1 <= coin <= 5000
# the number of coins is less than 500
# the answer is guaranteed to fit into signed 32-bit integer

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        
        # M1. 二维DP
        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        # dp[i][j]的含义：j代表所需要金额， i代表选到几种硬币，如i=0代表一种硬币都不用

        # 初始化状态
        for c in range(1, amount + 1):
            dp[0][c] = 0  # 没有任何一种硬币，不论需要多少金额，都没有对应的方案数

        for r in range(len(coins) + 1):
            dp[r][0] = 1  # 如果金额为0，对多少种硬币来说都是1种方案

        for r in range(1, len(coins) + 1):
            for c in range(1, amount + 1):
                dp[r][c] = dp[r - 1][c] + (dp[r][c - coins[r - 1]]\
                           if c - coins[r - 1] >= 0\
                           else 0)
                           
        return dp[-1][-1]

        # M2. 一维DP 空间优化
        # https://leetcode.com/problems/coin-change-2/solution/

        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] += dp[x - coin]
        return dp[-1]