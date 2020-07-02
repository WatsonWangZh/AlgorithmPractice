# Given n balloons, indexed from 0 to n-1. 
# Each balloon is painted with a number on it represented by array nums. 
# You are asked to burst all the balloons. 
# If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. 
# Here left and right are adjacent indices of i. 
# After the burst, the left and right then becomes adjacent.
# Find the maximum coins you can collect by bursting the balloons wisely.

# Note:
# You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
# 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

# Example:
# Input: [3,1,5,8]
# Output: 167 
# Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
#              coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 动态规划 O(n^3)
        # 状态： dp[i][j]表示戳爆从第i到第j个气球得到的最大金币数。
        # 状态转移方程： dp[i][j]=max(dp[i][j], 
        #                           dp[i][k−1] + num[i−1] * nums[k] * nums[j+1] + dp[k+1][j])
        #                       其中，k可以理解成[i,j]范围里最后戳破的一个气球。    
        # 时间复杂度O(n^3): 三层循环
        # 空间复杂度O(n^2): dp[i][j]数组的大小是(n+2)*(n+2)

        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[0 for _ in range(n+2)] for _ in range(n+2)]

        for i in range(1, n+1):
            dp[i][i] = nums[i-1] * nums[i] * nums[i+1]

        for i in range(1, n):
            for l in range(1, n):
                r = l + i
                if r > n:
                    continue
                temp = 0
                for k in range(l, r+1):
                    temp = max(temp, dp[l][k-1] + nums[l-1] * nums[k] * nums[r+1] + dp[k+1][r])
                dp[l][r] = temp
                
        return dp[1][n]
