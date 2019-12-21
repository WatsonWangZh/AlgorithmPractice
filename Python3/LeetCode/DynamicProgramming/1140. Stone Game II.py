# Alex and Lee continue their games with piles of stones.  
# There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  
# The objective of the game is to end with the most stones. 
# Alex and Lee take turns, with Alex starting first.  Initially, M = 1.
# On each player's turn, that player can take all the stones in the first X remaining piles, 
# where 1 <= X <= 2M.  Then, we set M = max(M, X).
# The game continues until all the stones have been taken.
# Assuming Alex and Lee play optimally, return the maximum number of stones Alex can get.

# Example 1:
# Input: piles = [2,7,9,4,4]
# Output: 10
# Explanation:  If Alex takes one pile at the beginning, Lee takes two piles, 
# then Alex takes 2 piles again. Alex can get 2 + 4 + 4 = 10 piles in total. 
# If Alex takes two piles at the beginning, then Lee can take all three piles left. 
# In this case, Alex get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 

# Constraints:
# 1 <= piles.length <= 100
# 1 <= piles[i] <= 10 ^ 4

# Hints:
# Use dynamic programming: the states are (i, m) for the answer of piles[i:] and that given m.

class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        # 动态规划 O(n^3)
        # f(i,j) 表示当前位于第 i 个位置且 M 为 j 时，先手能取到的最大的石子数量。
        # 从后往前转移，因为最后的状态我们都是可以直接得到的。维护后缀和 sum。
        # 有效位置的下标从 0 到 n−1，M 的下标从 1 到 n。
        # 初始化：对于所有的 1≤j≤n，f(n,j)=0。这是边界情况。
        # 转移时，我们需要枚举这一次先手取多少个石子 k，满足 1≤k≤2∗j，且 i+k≤n（i+k=n 就是后边的石子全部取完），
        # 我们转移 f(i,j)=max(f(i,j),sum(i)−f(i+k,max(j,k)))。
        # 这里用 sum(i) 减的原因是，此时我们交换了先后手，被转移的先手 以当前状态的角度看是后手，所以需要从总和里去除。
        # 最后答案就是 f(0,1)，表示当前在第 0 个位置，且 M 为 1 时先手能取到的最大值。
        # 时间复杂度
        # 状态数为 O(n^2) 个，转移需要 O(n) 的时间，故时间复杂度为 O(n^3)。
        # 空间复杂度
        # 需要 O(n^2) 的数组记录状态，故空间复杂度为 O(n^2)。
        
        n = len(piles)
        postsum = [0] * (n+1)
        dp = [[0] * (n+1) for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            postsum[i] = postsum[i+1] + piles[i]

        for i in range(n-1, -1, -1):
            for j in range(1, n+1):
                for k in range(1, min(j*2+1, n-i+1)):
                    dp[i][j] = max(dp[i][j], postsum[i] - dp[i+k][max(j, k)])
        return dp[0][1]