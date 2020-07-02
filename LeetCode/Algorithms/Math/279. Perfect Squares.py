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


# 二刷 200627
# M1. 蛮力算法 TLE
class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = [i**2 for i in range(1, int(n**0.5)+1)]

        def minNumSquares(k):
            """ recursive solution """
            # bottom cases: find a square number
            if k in square_nums:
                return 1
            min_num = float('inf')

            # Find the minimal value among all possible solutions
            for square in square_nums:
                if k < square:
                    break
                new_num = minNumSquares(k-square) + 1
                min_num = min(min_num, new_num)
            return min_num

        return minNumSquares(n)

# M2. DP
class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = [i**2 for i in range(1, int(n**0.5)+1)]
        
        dp = [i for i in range(n+1)]
        # bottom case
        dp[0] = 0
        
        for i in range(1, n+1):
            for square in square_nums:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i-square] + 1)
        
        return dp[-1]


# M3. BFS
class Solution:
    def numSquares(self, n: int) -> int:

        from collections import deque
        queue = deque([n])
        step = 0
        visited = set()

        while(queue):
            step += 1
            for _ in range(len(queue)):
                tmp = queue.pop()
                for i in range(1, int(tmp**0.5)+1):
                    x = tmp- i**2
                    if x == 0:
                        return step
                    if x not in visited:
                        queue.appendleft(x)
                        visited.add(x)
        return step
