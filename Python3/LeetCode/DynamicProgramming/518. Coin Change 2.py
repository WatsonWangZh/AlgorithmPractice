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
        # 动态规划，完全背包 O(amount⋅n)
        # 将总金额视为背包容量，将硬币的面额视为重量，价值视为 1，此题就是变种的固定容量完全背包问题。
        # 设计状态 f(j) 表示硬币总面额为 j 时的方案数，
        # 对于每一种硬币面额 coins(i)，j 从 coins(i) 枚举到 amount，
        # 累计转移 f(j)=f(j)+f(j−coins(i))。
        # 初始时 f(0)=1，最终答案为 f(amount)。
        # 时间复杂度
        # 状态数为 O(amount)，转移总数为O(n)，
        # 每次转移的时间复杂度为 O(1)，故总时间复杂度为 O(amount⋅n)。

        f = [0 for _ in range(amount + 1)]
        f[0] = 1

        for i in range(len(coins)):
            for j in range(coins[i], amount + 1):
                f[j] += f[j - coins[i]]

        return f[amount]
