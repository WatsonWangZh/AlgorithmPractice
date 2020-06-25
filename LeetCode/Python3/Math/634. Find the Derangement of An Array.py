# In combinatorial mathematics, a derangement is a permutation of the elements of a set, 
# such that no element appears in its original position.
# There's originally an array consisting of n integers from 1 to n in ascending order, 
# you need to find the number of derangement it can generate.
# Also, since the answer may be very large, you should return the output mod 10^9 + 7.

# Example 1:
# Input: 3
# Output: 2
# Explanation: The original array is [1,2,3]. The two derangements are [2,3,1] and [3,1,2].

# Note:
# n is in the range of [1, 106].

class Solution(object):
    def findDerangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        # DP 组合数学 错排问题公式 O(n) O(n)
        # if n < 2:
        #     return 0
        # dp = [0] * (n+1)
        # dp[1] = 0
        # dp[2] = 1
        # for i in range(3, n+1):
        #     dp[i] = (i-1)*(dp[i-1]+dp[i-2]) % (10**9 + 7)
        # return dp[n]

        # DP 组合数学 错排问题公式 空间优化 O(n) O(1)
        if n < 2:
            return 0
        pre_pre = 0
        pre = 1
        res = 1
        for i in range(3, n+1):
            res = (i-1) * (pre + pre_pre) % 1000000007
            pre_pre = pre
            pre = res
        return res 
