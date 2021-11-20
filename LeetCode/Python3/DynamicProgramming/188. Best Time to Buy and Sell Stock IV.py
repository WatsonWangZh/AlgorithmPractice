# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete at most k transactions.
# Note:
# You may not engage in multiple transactions at the same time 
# (ie, you must sell the stock before you buy again).

# Example 1:
# Input: [2,4,1], k = 2
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

# Example 2:
# Input: [3,2,6,5,0,3], k = 2
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
#              Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """

        # M1. DP法1
        # dp[i][j]表示第j天完成i次交易的最大收益。（买入+卖出一个来回才算一次交易。）
        # dp[i][j]包含下面两种情况：
            # ① 第j天不交易 dp[i][j-1]
            # ② 第j天交易，即第j天卖出。假设第m天买入，则为prices[j] - prices[m] + dp[i-1][m-1]，m=1,2…j-1 
            # → 计算max(-prices[m] + dp[i-1][m-1]) 
            # → 遍历的同时，maxTemp = max(maxTemp, -prices[j] + dp[i-1][j-1])
            # 状态方程为：dp[i][j] = max(dp[i][j-1],prices[j] + maxTemp)
        
        # if not prices:
        #     return 0

        # 当k>n/2时，相当于多次交易（无数次交易），解法是122. Best Time to Buy and Sell Stock II，
        # 只需关注递增的差值，求和。

        # n = len(prices)
        # if k > (n>>1):
        #     return self.helper(prices)
        
        # dp = [[0] * n for _ in range(k+1)] # dp[i][j]表示第j天完成i次交易的最大收益
        # for i in range(1, k+1):
        #     maxTemp = -prices[0]
        #     for j in range(1, n):
        #         maxTemp = max(maxTemp, -prices[j] + dp[i-1][j-1])
        #         dp[i][j] = max(dp[i][j-1], prices[j] + maxTemp)
        # return dp[-1][-1]

    # def helper(self, prices):
    #     res = 0
    #     buy = prices[0]
    #     for price in prices[1:]:
    #         if price > buy:
    #             res += price - buy
    #         buy = price
    #     return res
    

    # M2. DP法2
    # 类似123. Best Time to Buy and Sell Stock III的解法2，有k种状态。
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        # 当k>n/2时，相当于多次交易（无数次交易），解法是122. Best Time to Buy and Sell Stock II，
        # 只需关注递增的差值，求和。
        n = len(prices)
        if k > (n>>1):
            return self.helper(prices)

        buy = [float('-inf')] * (k+1)
        sell = [0] * (k+1)
        for price in prices:
            for j in range(1, k+1):
                buy[j] = max(buy[j], sell[j-1] - price)
                sell[j] = max(sell[j], buy[j] + price)
        return sell[-1]

    def helper(self, prices):
        res = 0
        buy = prices[0]
        for price in prices[1:]:
            if price > buy:
                res += price - buy
            buy = price
        return res
