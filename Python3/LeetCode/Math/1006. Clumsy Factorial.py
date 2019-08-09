# Normally, the factorial of a positive integer n is the product of all positive integers less than 
# or equal to n.  For example, factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1.
# We instead make a clumsy factorial: 
# using the integers in decreasing order, 
# we swap out the multiply operations for a fixed rotation of operations: 
# multiply (*), divide (/), add (+) and subtract (-) in this order.
# For example, clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1.  
# However, these operations are still applied using the usual order of operations of arithmetic: 
# we do all multiplication and division steps before any addition or subtraction steps, 
# and multiplication and division steps are processed left to right.
# Additionally, the division that we use is floor division such that 10 * 9 / 8 equals 11.  
# This guarantees the result is an integer.
# Implement the clumsy function as defined above: given an integer N, it returns the clumsy factorial of N.

# Example 1:
# Input: 4
# Output: 7
# Explanation: 7 = 4 * 3 / 2 + 1

# Example 2:
# Input: 10
# Output: 12
# Explanation: 12 = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1
 
# Note:
# 1 <= N <= 10000
# -2^31 <= answer <= 2^31 - 1  (The answer is guaranteed to fit within a 32-bit integer.)

class Solution:
    def clumsy(self, N: int) -> int:
        # M1. 直接计算 O(n)
        # 由题目描述可知，从N开始往后，都是先乘除，后加减，所以我们可以先计算第一个乘除和加，
        # 然后每四个运算符一个循环，来计算余下的式子，最后不足4个运算符的时候单独计算。
        # 时间复杂度分析: 从N到1，每个元素参与计算一遍，所以时间复杂度为O(n)
        # if N == 1:
        #     return 1
        # if N == 2:
        #     return 2 * 1
        # if N == 3:
        #     return 3 * 2 // 1
        # ans = 0
        # ans = N * (N - 1) // (N - 2) + N - 3
        # N -= 4
        # while N >= 4:
        #     ans -= N * (N - 1) // (N - 2)
        #     ans += N - 3
        #     N -= 4
        # if N == 0:
        #     return ans
        # if N == 1:
        #     return ans - 1
        # if N == 2:
        #     return ans - 2 * 1
        # if N == 3:
        #     return ans - 3 * 2 // 1

        # M2. 利用字符串计算函数eval O(n)
        # 根据题意生成符合输入的字符串算式，由字符串计算函数计算出结果。
        # 时间复杂度分析: 同上一种方法一样也是O(n)。
        ss = [str(x) for x in range(N, 0, -1)]
        s = ss[0]
        sr = ['*', '//', '+', '-']
        for i in range(1, N):
            s += sr[(i - 1) % 4]
            s += ss[i]
        return eval(s)
