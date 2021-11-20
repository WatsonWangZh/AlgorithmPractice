# Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)
# (Recall that an integer is prime if and only if it is greater than 1, 
# and cannot be written as a product of two positive integers both smaller than it.)
# Since the answer may be large, return the answer modulo 10^9 + 7.

# Example 1:
# Input: n = 5
# Output: 12
# Explanation: For example [1,2,5,4,3] is a valid permutation, 
# but [5,2,3,4,1] is not because the prime number 5 is at index 1.

# Example 2:
# Input: n = 100
# Output: 682289015
 
# Constraints:
# 1 <= n <= 100

# Hints:
# Solve the problem for prime numbers and composite numbers separately.
# Multiply the number of permutations of prime numbers over prime indices 
# with the number of permutations of composite numbers over composite indices.
# The number of permutations equals the factorial.

import math
class Solution(object):
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 排列 
        # 将数字分为质数和非质数两部分。
        # 假设有 p 个质数，答案就是 p!⋅(n−p)!。
        # 时间复杂度
        # 需要求质数的个数，暴力的做法需要 O(n^3/2) 的时间，可以采用欧拉线性筛法在 O(n) 的时间内求出。
        # 空间复杂度
        # 暴力仅需要常数空间，线性筛法需要O(n)的空间。

        # M1. 暴力求质数个数 O(nlgn) O(1)
        # mod  = 10 ** 9 + 7
        # def factorial(n):
        #     res = 1
        #     for i in range(2, n+1):
        #         res *= i % mod
        #     return res
        # def isPrime(n):
        #     if n <= 1:
        #         return False
        #     for i in range(2, int(math.sqrt(n))+1):
        #         if n % i == 0:
        #             return False
        #     return True
        # p = 0
        # for i in range(1, n+1):
        #     if isPrime(i):
        #         p += 1
        # return factorial(p) * factorial(n-p) %mod

        # M2. 欧拉线性筛法求质数个数 O(n) O(n)
        def oulashai(n):
            prime = [0 for i in range(n+1)]
            res = []  
            for i in range(2,n+1): 
                if prime[i] == 0: 
                    res.append(i)      
                for j in res:
                    if i * j > n:
                        break
                    prime[i * j]=1
                    if i % j==0:      
                        break;
            return res

        mod  = 10 ** 9 + 7
        def factorial(n):
            res = 1
            for i in range(2, n+1):
                res *= i % mod
            return res

        p = len(oulashai(n))
        return factorial(p) * factorial(n-p) % mod