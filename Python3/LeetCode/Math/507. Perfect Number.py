# We define the Perfect Number is a positive integer 
# that is equal to the sum of all its positive divisors except itself.
# Now, given an integer n, write a function t
# hat returns true when it is a perfect number and false when it is not.

# Example:
# Input: 28
# Output: True
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
# Note: The input number n will not exceed 100,000,000. (1e8)

import math
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # M1. 暴力枚举 O(n) TLE
        # if num == 1:
        #     return False
        # div_sum = 0
        # for i in range(1, num):
        #     if num % i == 0:
        #         div_sum += num
        # return num == div_sum

        # M2. 枚举优化 O(根号n) 
        # 从 i=2 开始，逐一枚举 num 的正因数，直到 根号num 为止。
        # 若 num % i = 0，则找到了一个正因子；
        # 同时，若 i**2 != num，则另外找到了 n/i 为正因子。
        # 最后求和时需要统计上正因子 1。注意 n 为 1 的特殊情况。

        if num == 1:
            return False
        div_sum = 0
        i = 2
        while i**2 <= num:
            if num % i == 0:
                div_sum += i
                if i**2 != num:
                    div_sum += num / i
            i += 1
        return div_sum + 1 == num
