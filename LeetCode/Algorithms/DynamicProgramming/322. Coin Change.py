# You are given coins of different denominations and a total amount of money amount. 
# Write a function to compute the fewest number of coins 
# that you need to make up that amount. 
# If that amount of money cannot be made up by any combination of the coins, 
# return -1.

# Example 1:
# Input: coins = [1, 2, 5], amount = 11
# Output: 3 
# Explanation: 11 = 5 + 5 + 1

# Example 2:
# Input: coins = [2], amount = 3
# Output: -1

# Note:
# You may assume that you have an infinite number of each kind of coin.

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # 动态规划 O(nm)
        # 完全背包问题。
        # 相当于有 n 种物品，每种物品的体积是硬币面值，价值是1。问装满背包最少需要多少价值的物品？
        # 状态表示： f[i] 表示凑出 i 价值的钱，最少需要多少个硬币。
        # 第一层循环枚举不同硬币，
        # 第二层循环从大到小枚举所有价值（由于每种硬币有无限多个，所以要从小到大枚举），
        # 然后用第 i 种硬币更新 f[i]：f[i] = min(f[i], f[i - coins[i]] + 1)。
        # 时间复杂度分析：
        # 令 n 表示硬币种数，m 表示总价钱，则总共两层循环，所以时间复杂度是 O(nm)。

        f = [float('inf') for i in range(amount+1)]
        f[0] = 0

        for i in range(len(coins)):
            for j in range(coins[i],amount+1):
                f[j] = min(f[j], f[j-coins[i]] + 1)

        if f[amount] == float('inf'):
            return -1

        return f[amount]
