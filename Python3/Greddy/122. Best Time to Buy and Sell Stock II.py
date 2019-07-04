# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. 
# You may complete as many transactions as you like 
# (i.e., buy one and sell one share of the stock multiple times).
# Note: You may not engage in multiple transactions at the same time 
# (i.e., you must sell the stock before you buy again).

# Example 1:
# Input: [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
#              Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

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

class Solution:

    # 这道题由于可以无限次买入和卖出。我们都知道炒股想挣钱当然是低价买入高价抛出，
    # 那么这里我们只需要从第二天开始，如果当前价格比之前价格高，则把差值加入利润中，
    # 因为我们可以昨天买入，今日卖出，若明日价更高的话，还可以今日买入，明日再抛出。
    # 以此类推，遍历完整个数组后即可求得最大利润。
    def maxProfit(self, prices):
        maxprofit = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                maxprofit += prices[i+1] - prices[i]
        return maxprofit

    # 错误解法: 生硬划分为三段，
    # def maxProfit(self, prices):
    #     maxprofit = 0
    #     for i in range(len(prices)):
    #         for j in range(i+1,len(prices)):
    #             temppro = self.helper(prices[:i]) + self.helper(prices[i:j+1]) + self.helper(prices[j:])
    #         if  temppro > maxprofit:
    #             maxprofit = temppro
    #     return maxprofit
    
    # def helper(self, prices):
    #     maxProfit = 0
    #     minPrice = float('inf')
    #     for p in prices:
    #         minPrice = min(p, minPrice)
    #         profit = p - minPrice
    #         if profit > maxProfit:
    #             maxProfit = profit
    #     return maxProfit

def main():
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4]))
    print(s.maxProfit([1,2,3,4,5]))
    print(s.maxProfit([7,6,4,3,1]))

if __name__ == "__main__":
    main()