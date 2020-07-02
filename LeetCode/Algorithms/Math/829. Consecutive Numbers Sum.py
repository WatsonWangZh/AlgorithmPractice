# Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?

# Example 1:
# Input: 5
# Output: 2
# Explanation: 5 = 5 = 2 + 3

# Example 2:
# Input: 9
# Output: 3
# Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4

# Example 3:
# Input: 15
# Output: 4
# Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5

import math
class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        # 数学 O(n^0.5)
        # 假设首项为 x，项数为 k，根据数列求和公式 sum = k(2x+k−1)/2。
        # 令 sum=n，则可以枚举 2n 的约数，将其分为两部分的乘积，
        # 较小的那一部分作为 k，较大的部分作为 2x+k−1，如果解得 x 是正整数，则答案加一。
        # 时间复杂度
        # 枚举约数的个数，故时间复杂度为O(n^0.5)。

        res = 0
        i = 1
        N *= 2
        while i < math.sqrt(N):
            if N % i == 0:
                s = i
                l = N / i + 1 - i
                if l % 2 == 0 and l >= 0:
                    res += 1
            i += 1
        return res 

        # 数学 O(n^0.5)
        # 对于一个正整数N，如果能写成K个连续正整数相加的形式，则有，
        # N = (x+1) + (x+2) + … + (x+K)
        # N = K * x + (1+K) * K / 2
        # 于是，N能够写成K个连续正整数相加的条件是，(N − K * (K+1) / 2)能够被K整除。
        # 时间复杂度分析：K个连续正整数相加，K的取值从1开始，且满足(N − K * (K+1) / 2)大于等于0。
        # K的可取值范围为n^0.5量级。

        res = 0
        k = 1
        while k * (k+1) <= 2 * N:
            if (N-k*(k+1)/2) % k == 0:
                res += 1
            k += 1
        return res 
