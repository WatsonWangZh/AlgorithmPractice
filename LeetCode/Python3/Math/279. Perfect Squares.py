# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

# Example 1:
# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.

# Example 2:
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # M1. 普通DP O(n^1.5)
        # 令 dp[i] 表示通过平方数组成 i 所需要的最少数量。
        # 则 dp[i]=min(dp[i−j∗j]+1)，其中 1≤j≤i^0.5。
        # dp[n] 即为最终答案。

        dp = [n] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            j = 1 
            while j*j <= i:
                dp[i] = min(dp[i], dp[i-j*j]+1)
                j += 1
        return dp[n]

        # M2. BFS优化DP O(n^1.5)
        # 通过 BFS 来优化动态规划的效率，可以将整个过程看做一张图，每个数字都是一个点，两个数字之间差距为平方数时有一条单向边。
        # 使用 BFS 来求从 0 到 n 的最短路。
        # 时间复杂度
        # BFS的时间复杂度为 O(n+m)，这里的点数，也就是数字个数 n，边数同算法1中的分析是 O(i^0.5)，
        # 故总时间复杂度仍然是 O(n^1.5)，但由于BFS可能能快速找到到结点 n 的路径，常数会比较优。
        dp = [n] * (n+1)
        dp[0] = 0
        q = []
        q.append(0)
        while len(q) > 0:
            s = q.pop()
            if s > n:
                break
            i = 1
            while s+i*i <= n:
                if dp[s+i*i] > dp[s]+1:
                    dp[s+i*i] = dp[s] + 1
                    q.append(s+i*i)
                i += 1
        return dp[n]