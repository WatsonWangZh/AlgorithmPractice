# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time. 
# The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
# Note: m and n will be at most 100. 

# Example 1:
# Input:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right

# Hints:
# The robot can only move either down or right. Hence any cell in the first row can only be reached from the cell left to it. However, if any cell has an obstacle, you don't let that cell contribute to any path. So, for the first row, the number of ways will simply be
# if obstacleGrid[i][j] is not an obstacle
#      obstacleGrid[i,j] = obstacleGrid[i,j - 1] 
# else
#      obstacleGrid[i,j] = 0
# You can do a similar processing for finding out the number of ways of reaching the cells in the first column.
# For any other cell, we can find out the number of ways of reaching it, by making use of the number of ways of reaching the cell directly above it and the cell to the left of it in the grid. This is because these are the only two directions from which the robot can come to the current cell.
# Since we are making use of pre-computed values along the iteration, this becomes a dynamic programming problem.
# if obstacleGrid[i][j] is not an obstacle
#      obstacleGrid[i,j] = obstacleGrid[i,j - 1]  + obstacleGrid[i - 1][j]
# else
#      obstacleGrid[i,j] = 0

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # 动态规划 O(mn)
        # 类似于62题Unique Paths，每一个网格都可以由该网格左边或上边的网格转移过来，
        # 因此到达某一点的路径数等于到达它上一点的路径数与它左边的路径数之和，
        # 不同的是，当某个网格有障碍时，到达该网格的路径数维0。
        # 这还是一个递推问题，考虑用动态规划。
        # 动态规划数组dp[i][j] = 起点到点(i, j)的路径总数。
        # 于是我们就得到递推关系式：
        # 当网格为0时，dp[i][j] = dp[i][j-1] + dp[i-1][j]；
        # 当网格为1（说明该网格是障碍物），dp[i][j]=0。

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if not m or not n:
            return 0

        dp = [[0 for _ in range(101)]for _ in range(101)]
        dp[0][0] = 1 - obstacleGrid[0][0]

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] += dp[i-1][j]
                    if j > 0:
                        dp[i][j] += dp[i][j-1]
                    
        return dp[m-1][n-1]