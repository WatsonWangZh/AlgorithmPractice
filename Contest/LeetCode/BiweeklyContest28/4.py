# 1478. Allocate Mailboxes
# User Accepted:342
# User Tried:594
# Total Accepted:364
# Total Submissions:1061
# Difficulty:Hard
# Given the array houses and an integer k. where houses[i] is the location of the ith house along a street, your task is to allocate k mailboxes in the street.
# Return the minimum total distance between each house and its nearest mailbox.
# The answer is guaranteed to fit in a 32-bit signed integer.

# Example 1:
# Input: houses = [1,4,8,10,20], k = 3
# Output: 5
# Explanation: Allocate mailboxes in position 3, 9 and 20.
# Minimum total distance from each houses to nearest mailboxes is |3-1| + |4-3| + |9-8| + |10-9| + |20-20| = 5 

# Example 2:
# Input: houses = [2,3,5,12,18], k = 2
# Output: 9
# Explanation: Allocate mailboxes in position 3 and 14.
# Minimum total distance from each houses to nearest mailboxes is |2-3| + |3-3| + |5-3| + |12-14| + |18-14| = 9.

# Example 3:
# Input: houses = [7,4,6,1], k = 1
# Output: 8

# Example 4:
# Input: houses = [3,6,14,10], k = 4
# Output: 0
 
# Constraints:
# n == houses.length
# 1 <= n <= 100
# 1 <= houses[i] <= 10^4
# 1 <= k <= n
# Array houses contain unique integers.
 
class Solution:
    def minDistance(self, houses: List[int], m: int) -> int:
        # dp[i][j]表示从1到i，最多划分为k个段，所对应的距离之和的最小值
        houses.sort()
        n = len(houses)
        dp = [[0] * (m + 1) for _ in range(n)]
        cost = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(i, n):
                for k in range(i, j + 1):
                    cost[i][j] += abs(houses[k] - houses[i + (j - i + 1) // 2])

        for i in range(n):
            dp[i][0] = 1e8

        for i in range(1, n):
            for j in range(1, m + 1):
                dp[i][j] = 1e8
                for k in range(i + 1):
                    t = 0
                    if k:
                        t = dp[k - 1][j - 1]
                    dp[i][j] = min(dp[i][j], t + cost[k][i])
        return dp[n - 1][m]



