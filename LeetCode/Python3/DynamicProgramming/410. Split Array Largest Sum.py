# Given an array which consists of non-negative integers and an integer m, 
# you can split the array into m non-empty continuous subarrays. 
# Write an algorithm to minimize the largest sum among these m subarrays.
# Note:
# If n is the length of array, assume the following constraints are satisfied:
# 1 ≤ n ≤ 1000
# 1 ≤ m ≤ min(50, n)

# Examples:
# Input:
# nums = [7,2,5,10,8]
# m = 2
# Output:
# 18

# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.

class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        # M1. 二分贪心 O(n)
        def valid(mid):
            cnt = 0
            current = 0
            for num in nums:
                current += num
                if current > mid:
                    cnt += 1
                    if cnt >= m:
                        return False
                    current = num
            return True 
        
        l, r = max(nums), sum(nums)
        while l < r:
            mid = l + r >> 1
            if valid(mid):
                r = mid
            else:
                l = mid + 1
        return l

        # M2. DP O(m*n^2)
        n = len(nums)
        # dp[i][j] 表示将数组中前i个数字分成j组所能得到的最小的各个子数组中最大值
        dp = [[float('inf')] * (m+1) for _ in range(n+1)]
        dp[0][0] = 0
        
        pre_sum = [0] * (n+1)
        for i in range(n):
            pre_sum[i+1] = pre_sum[i] + nums[i]
            
        for i in range(1, n+1):
            for j in range(1, m+1):
                for k in range(i):
                    dp[i][j] = min(dp[i][j], max(dp[k][j-1], pre_sum[i] - pre_sum[k]))
        return dp[n][m]