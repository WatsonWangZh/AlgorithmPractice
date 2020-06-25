# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete at most two transactions.
# Note: You may not engage in multiple transactions at the same time 
# (i.e., you must sell the stock before you buy again).

# Example 1:
# Input: [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
#              Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

# Example 2:
# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
#              Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
#              engaging multiple transactions at the same time. You must sell before buying again.

# Example 3:
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # M1. 两轮贪心，一个从前往后，一个从后往前。
        # 首先，从前往后遍历，保留最小值buy → 记录截止第i天(包含第i天)的maxProfit；
        # 然后，从后往前遍历，保留最大值sell → 记录第i天之后(不包含第i天)的maxProfit。
        # 注意 - 可能只交易1次，所以保留遍历一趟后profit的值。

        # if not prices:
        #     return 0

        # # Record min-buy
        # profits = [0]
        # buy, profit = prices[0], 0
        # for price in prices[1:]:
        #     buy = min(buy, price)
        #     profit = max(profit, price-buy)
        #     profits.append(profit)

        # # Record max-sell - Note remember the value of profit
        # sell = prices[-1]
        # temp = 0
        # for i in range(len(prices)-1, 0, -1):
        #     sell = max(sell, prices[i])
        #     temp = max(temp, sell - prices[i])
        #     profit = max(profit, temp + profits[i-1])
        # return profit


        # M2. DP
        # 第i天有4种状态：第一笔交易买入状态最大收益buy1和第一笔交易卖出状态最大收益sell1，第二笔交易买入状态最大收益buy2和第二笔交易卖出状态最大收益sell2。
        # 则有下列状态方程：
            # sell2[i] = max(sell2[i-1], buy2[i-1] + prices[i])
            # buy2[i] = max(buy2[i-1], sell1[i-1] - prices[i])
            # sell1[i] = max(sell1[i-1], buy1[i-1] + prices[i])
            # buy1[i] = max(buy1[i-1], - prices[i])

        buy1 = buy2 = float('-inf')
        sell1 = sell2 = 0
        for price in prices:
            buy1 = max(buy1, -price)
            sell1 = max(sell1, buy1 + price)
            buy2 = max(buy2, sell1 - price)
            sell2 = max(sell2, buy2 + price)
        return sell2
