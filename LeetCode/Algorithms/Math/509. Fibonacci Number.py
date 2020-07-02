# The Fibonacci numbers, commonly denoted F(n) form a sequence, 
# called the Fibonacci sequence, such that each number is the sum of the two preceding ones, 
# starting from 0 and 1. That is,
# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), for N > 1.
# Given N, calculate F(N).

# Example 1:
# Input: 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

# Example 2:
# Input: 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

# Example 3:
# Input: 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 
# Note:
# 0 ≤ N ≤ 30.

class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        # M1. 原始递归 
        # 时间复杂度: O(2^n) 递归树分析
        # 空间复杂度: O(n) 栈帧分析

        # if N == 0:
        #     return 0
        # if N < 3:
        #     return 1
        # return self.fib(N-2) + self.fib(N-1)

        # M2. 尾递归
        # 时间复杂度: O(n) 尾递归过程分析
        # 空间复杂度: O(n) 栈帧分析

        # def helper(first, second, N):
        #     if N == 0:
        #         return 0
        #     if N < 3:
        #         return 1
        #     if N == 3:
        #         return first + second
        #     return helper(second, first+second, N-1)
        # return helper(1, 1, N)

        # M3. DP循环
        # 时间复杂度: O(n) 
        # 空间复杂度: O(n) 

        # import numpy as np
        # if N == 0:
        #     return 0
        # tmp = np.zeros(N+1, dtype=int)
        # tmp[0] = 0
        # tmp[1] = 1
        # for i in range(2, N+1):
        #     tmp[i] = tmp[i-1] + tmp[i-2]
        # return tmp[N]


        # M4. DP循环 空间优化
        # 时间复杂度: O(n) 
        # 空间复杂度: O(1)

        if N == 0:
            return 0
        if N < 3:
            return 1
        first, second = 0, 1
        res = 0
        for i in range(2, N+1):
            res = first + second
            first = second
            second = res 
        return res