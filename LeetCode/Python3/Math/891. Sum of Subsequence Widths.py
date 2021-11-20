# Given an array of integers A, consider all non-empty subsequences of A.
# For any sequence S, let the width of S be the difference between the maximum and minimum element of S.
# Return the sum of the widths of all subsequences of A. 
# As the answer may be very large, return the answer modulo 10^9 + 7.

# Example 1:
# Input: [2,1,3]
# Output: 6
# Explanation:
# Subsequences are [1], [2], [3], [2,1], [2,3], [1,3], [2,1,3].
# The corresponding widths are 0, 0, 0, 1, 1, 2, 2.
# The sum of these widths is 6.
 
# Note:
# 1 <= A.length <= 20000
# 1 <= A[i] <= 20000

class Solution(object):
    def sumSubseqWidths(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # 数学 O(nlogn)
        # 由于只求每个子集的最大最小值，首先对数组进行排序。
        # 数组表示为a[0],a[1],…,a[n−1].
        # 思路1：用(i,j) pair来给划分子集。
        # 每一个(i,j)对表示一组min=a[i], max=a[j]的子集，
        # 相当于在数组中固定a[i]和a[j]两端，中间的点任意选。
        # 这组子集一共有2^(j−i−1)个子集，每个子集的宽度是(a[j]−a[i])，
        # 那么这组子集的总宽度为(a[j]−a[i])*2^(j−i−1).

        # 思路2(优化版)：用j来划分子集。
        # 每一组子集都是以a[j]结尾，相当于对思路1做i的压缩。
        # 由思路1的分析可得，
        # result=(a[j]−a[0])*2^(j−0−1)+(a[j]−a[1])∗2^(j−1−1)+…+(a[j]−a[j−1])*2^(j−j+1−1)
        # 可表示为 result=X−Y, 其中
        # X=a[j] * (2^(j−1) + 2^(j−2) + … + 2^0) = a[j]*(2^j−1),
        # Y=a[0]*2^(j−1)+a[1]*2^(j−2)+…+a[j−1]*2^0.
        # 简化计算 result=X−Y
        # X的计算只需要在一次循环中遍历a[j]和维护p=2^j即可得。
        # 观察可得，Y[j+1]=Y[j]+a[j]。

        # 复杂度分析 O(nlogn)
        # 排序O(nlogn), 求X和Y都在一个循环中完成，O(n)。

        mod = 10 ** 9 + 7
        A.sort()
        res = 0
        # power : 2^j
        power = 1
        y = 0
        for x in A:
            res = (res + x * (power - 1) - y) % mod
            y = (y * 2 + x) % mod
            power = power * 2 % mod
        # for the last exceed chance
        return res % mod
