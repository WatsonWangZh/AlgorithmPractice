# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time. 
# The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# How many possible unique paths are there?
# Above is a 7 x 3 grid. How many possible unique paths are there?
# Note: m and n will be at most 100.

# Example 1:
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right

# Example 2:
# Input: m = 7, n = 3
# Output: 28

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # # M1. 递归 O(2^m+n)
        # 每一个网格都可以由该网格左边或上边的网格转移过来，
        # 因此到达某一点的路径数等于到达它上一点的路径数与它左边的路径数之和，
        # 其实这是一个递推问题，即(m, n)的路径数等于(m, n-1)和(m-1, n)的路径之和，
        # 再考虑边界情况，就是当网格长/宽==1时，只有一条路径。
        # 递推公式即
        # T(m,n)==  1 , if m == 1 or n == 1
        #           T(m−1,n)+T(m,n−1) , else

        # Time Limit Exceeded
        # if m == 1 or n == 1:
        #      return 1 
        # return self.uniquePaths(m, n - 1) + self.uniquePaths(m - 1, n)

        # 但由于直接递归会产生大量重复计算导致复杂度很高，当m, n较大时容易超时，
        # 因此需要数组记录一下中间值，这样再次需要用到时查表即可，用数组记录后复杂度变为O(mn)。

    #     self.record = [[0 for _ in range(101)]for _ in range(101)]
    #     return self.help(m, n)
        
    # def help(self, m, n):
    #     if m == 1 or n == 1:
    #         return 1
    #     if self.record[m][n]: 
    #         # 说明有记录
    #         return self.record[m][n]
    #     self.record[m][n] = self.help(m - 1, n) + self.help(m, n - 1)
    #     return self.record[m][n]

        # M2. 动态规划 O(mn)
        # 如上所述，这是一个递推问题, 因此可以考虑动态规划。
        # 动态规划数组dp[i][j] = 起点到点(i, j)的路径总数。
        # 于是我们就得到递推关系式：dp[i][j] = dp[i][j-1] + dp[i-1][j]。
        # 再考虑边界情况，当i == 1 || j == 1时，dp[i][j] = 1。

        # dp = [[0 for _ in range(101)]for _ in range(101)]
        # for i in range(1, m+1):
        #     for j in range(1, n+1):
        #         if i == 1 or j == 1:
        #             dp[i][j] = 1
        #         else:
        #             dp[i][j] = dp[i][j-1] + dp[i-1][j]
        # return dp[m][n]

        # 上述做法需要一个大小为m x n的二维数组，空间复杂度为O(mn)，
        # 但其实dp[i][j]只会用到dp[i-1][j]和dp[i][j-1]，不会用到之前的数据，因此可以用滚动数组减小空间复杂度。

        # dp = [0 for _ in range(101)]
        # dp[1] = 1
        # for i in range(1,m+1):
        #     for j in range(2, n+1):
        #         dp[j] += dp[j-1]
        # return dp[n]

        # M3. (组合数学) O(n)O(n)
        # 从网格左上角到网格右下角一共要走m+n-2步，在这些步数中，一共会向下走m-1步，向右走n-1步，
        # 因此就是经典的组合问题，结果就是Cn−1m+n−2。这样空间复杂度为O(1)，时间复杂度为O(n)。

        totalStep = m + n - 2
        step = max(m , n)
        result = 1
        for i in range(step, totalStep+1): 
            result *= i
        for i in range(1, totalStep - step + 2):
            result /= i
        return result
