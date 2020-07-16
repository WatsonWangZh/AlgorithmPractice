# Implement pow(x, n), which calculates x raised to the power n (xn).

# Example 1:
# Input: 2.00000, 10
# Output: 1024.00000

# Example 2:
# Input: 2.10000, 3
# Output: 9.26100

# Example 3:
# Input: 2.00000, -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25

# Note:
# -100.0 < x < 100.0
# n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # M0. 自带库
        return x ** n

        # M1. 蛮力算法 O(n) TLE
        if x == 0:
            return 0
        if n < 0:
            x = 1/x
            n = -n

        res = 1
        for i in range(n):
            res *= x
        return res

        # M2. 二分法 O(lgn)
        if x == 0:
            return 0
        if n < 0:
            x = 1/x
            n = -n

        res = 1
        while n >= 1:
            if n%2 == 1:
                res *= x
            x *= x
            n >>= 1
        return res

        # M3. 快速幂
        if x == 0:
            return 0
        if n < 0:
            x = 1 / x
            n = -n

        res = 1
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res
