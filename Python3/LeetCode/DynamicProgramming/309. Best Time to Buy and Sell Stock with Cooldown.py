# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like 
# (ie, buy one and sell one share of the stock multiple times) with the following restrictions:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

# Example:
# Input: [1,2,3,0,2]
# Output: 3 
# Explanation: transactions = [buy, sell, cooldown, buy, sell]

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # M1. https://www.youtube.com/watch?v=Ggzbo9eVrLU
        if not prices or len(prices)<2: 
            return 0

        n=len(prices)
        unhold, hold = [0] * n, [0] * n

        hold[0] = -prices[0]
        hold[1] = max(-prices[0], -prices[1])
        unhold[1] = max(0, prices[1]-prices[0])

        for i in range(2,n):
            hold[i] = max(hold[i-1], unhold[i-2] - prices[i])
            unhold[i] = max(unhold[i-1], hold[i-1] + prices[i])

        return unhold[n-1]

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # M2. 另一种DP
        # 设计状态
        #   f[i]表示第i天，当前不持有股票且当前没有发生卖出交易的最大收益；
        #   g[i]表示第i天，不持有股票，且当前刚刚卖出股票的最大收益；
        #   h[i]表示当前持有股票的最大收益。
        # 状态转移为
        #   f[i] = max(f[i - 1], g[i - 1])，表示构成第i天不持有股票且当天无交易有两种方式，
        #       一种是前一天也不持有且前一天没有卖出交易，另一种是前一天持有且前一天刚刚卖出股票；二者取最大值。
        #   g[i] = h[i - 1] + prices[i]，表示构成第i天不持有股票且当天有交易仅有一种方式，
        #       即当天卖出前一天持有的股票。
        #   h[i] = max(h[i - 1], f[i - 1] - prices[i])，表示构成第i天持有股票有两种方式，
        #       一种是前一天持有，另一种是前一天不持有且前一天无交易，但这一天刚刚买入。
        # 最终答案为max(f[n - 1], g[n - 1])，即最后一天不持有股票的两种情况。

        if not prices:
            return 0
        f = [0 for i in range(len(prices))]
        g = [0 for i in range(len(prices))]
        h = [0 for i in range(len(prices))]
        res = 0
        f[0] = 0
        g[0] = -9999999
        h[0] = -prices[0]
        for i in range(1, len(prices)):
            f[i] = max(g[i-1], f[i-1])
            g[i] = h[i-1] + prices[i]
            h[i] = max(h[i-1], f[i-1] - prices[i])
        return max(f[len(prices)-1], g[len(prices)-1])
