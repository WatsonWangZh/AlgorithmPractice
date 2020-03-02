# On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
# Once you pay the cost, you can either climb one or two steps. 
# You need to find minimum cost to reach the top of the floor, 
# and you can either start from the step with index 0, or the step with index 1.

# Example 1:
# Input: cost = [10, 15, 20]
# Output: 15
# Explanation: Cheapest is start on cost[1], pay that cost and go to the top.

# Example 2:
# Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# Output: 6
# Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].

# Note:
# cost will have a length in the range [2, 1000].
# Every cost[i] will be an integer in the range [0, 999].

# Hints:
# Say f[i] is the final cost to climb to the top from step i. Then f[i] = cost[i] + min(f[i+1], f[i+2]).

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # DP1. dp[i] 表示爬到第i层的最小 cost
        res = 0
        n = len(cost)
        dp = [0] * (n + 1)
        for i in range(2, n+1):
            dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])
        return dp[n]

        # 空间优化
        one_step, two_steps = 0, 0
        n = len(cost)
        for i in range(2, n+1):
            cur = min(one_step + cost[i-1], two_steps + cost[i-2])
            one_step, two_steps = cur, one_step
        return cur

        # DP2. dp[i] 表示到第 i+1 层的最小 cost，分别初始化 dp[0] 和 dp[1] 为 cost[0] 和 cost[1]
        res = 0
        n = len(cost)
        dp = [0] * (n + 1)
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i- 1], dp[i - 2])
        return min(dp[n-1], dp[n-2])

        # 空间优化
        one_step, two_steps = 0, 0
        n = len(cost)
        for i in range(n):
            cur = cost[i] + min(one_step, two_steps)
            one_step, two_steps = cur, one_step
        return min(one_step, two_steps)