# There are a row of n houses, 
# each house can be painted with one of the three colors: red, blue or green. 
# The cost of painting each house with a certain color is different. 
# You have to paint all the houses such that no two adjacent houses have the same color.
# The cost of painting each house with a certain color is represented by a n x 3 cost matrix. 
# For example, 
# costs[0][0] is the cost of painting house 0 with color red; 
# costs[1][2] is the cost of painting house 1 with color green, 
# and so on... Find the minimum cost to paint all houses.

# Note:
# All costs are positive integers.

# Example:
# Input: [[17,2,17],[16,16,5],[14,3,19]]
# Output: 10
# Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue. 
#              Minimum cost: 2 + 5 + 3 = 10.

class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        # 动态规划 O(nm)
        # 维护一个二维的动态数组dp，其中dp[i][j]表示刷到第i+1房子用颜色j的最小花费，递推式为:
        # dp[i][j] = dp[i][j] + min(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3])；
        # 这个也比较好理解，如果当前的房子要用红色刷，那么上一个房子只能用绿色或蓝色来刷，
        # 那么我们要求刷到当前房子，且当前房子用红色刷的最小花费就等于当前房子用红色刷的钱加上刷到上一个房子用绿色和刷到上一个房子用蓝色的较小值，
        # 这样当我们算到最后一个房子时，我们只要取出三个累计花费的最小值即可。

        # if not costs or not costs[0]:
        #     return 0

        # dp = costs
        # for i in range(1, len(dp)):
        #     for j in range(3):
        #         dp[i][j] += min(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3])

        # return min(min(dp[-1][0], dp[-1][1]), dp[-1][2])

        # 更直观的写法

        if not costs or not costs[0]:
            return 0
        
        preR, preB, preG = costs[0]
        
        for i in range(1, len(costs)):
            curR, curB, curG = costs[i]
            curR += min(preG, preB)
            curB += min(preR, preG)
            curG += min(preR, preB)
            preR, preG, preB = curR, curG , curB

        return min(preR, preG, preB)