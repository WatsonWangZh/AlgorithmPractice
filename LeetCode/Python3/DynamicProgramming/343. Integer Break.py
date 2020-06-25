# Given a positive integer n, 
# break it into the sum of at least two positive integers and maximize the product of those integers. 
# Return the maximum product you can get.

# Example 1:
# Input: 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.

# Example 2:
# Input: 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.

# Note: You may assume that n is not less than 2 and not larger than 58.

# Hints:
# There is a simple O(n) solution to this problem.
# You may check the breaking results of n ranging from 7 to 10 to discover the regularities.

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        # M1. DP 
        dp = [0, 1]
        for m in range(2, n+1):
            j = m - 1
            i = 1
            max_product = 0
            while i <= j:
                max_product = max(max_product, max(i, dp[i]) * max(j, dp[j]))
                j -= 1
                i += 1
            dp.append(max_product)
        return dp[-1]

        # M2. 数学
        # 首先把一个正整数 N 拆分成若干正整数只有有限种拆法，所以存在最大乘积。
        # 假设 N=n1+n2+…+nk，并且 n1×n2×…×nk 是最大乘积。
        # 显然1不会出现在其中；
        # 如果对于某 i 有 ni≥5，那么把 ni 拆分成 3+(ni−3)，我们有 3(ni−3)=3ni−9>ni；
        # 如果 ni=4，拆成 2+2乘积不变，所以不妨假设没有4；
        # 如果有三个以上的2，那么 3×3>2×2×2，所以替换成3乘积更大；
        # 综上，选用尽量多的3，直到剩下2或者4时，用2。
        # 时间复杂度分析：当 n 比较大时，n 会被拆分成 ⌈n/3⌉ 个数，我们需要计算这么多次减法和乘法，所以时间复杂度是 O(n)。

        if n <= 3:
            return 1 * (n - 1)
        res = 1
        if n % 3 == 1:
            res = 4
            n -= 4
        elif n % 3 == 2:
            res = 2
            n -= 2
        while n:
            res *= 3
            n -= 3
        return res
