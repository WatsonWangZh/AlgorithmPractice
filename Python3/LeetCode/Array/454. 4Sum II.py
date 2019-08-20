# Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are 
# such that A[i] + B[j] + C[k] + D[l] is zero.
# To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. 
# All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 2^31 - 1.

# Example:
# Input:
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]

# Output:
# 2

# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        # 哈希表 转化为两数之和为0 O(n^2)
        # 建立哈希表，存储数组A和数组B所有数对求和出现的次数。
        # 枚举数组C和数组D的所有数对，查询哈希表中 -c - d出现的次数，累计到答案中。
        # 时间复杂度
        # 枚举数对的时间复杂度为O(n^2)，哈希表单次操作时间复杂度为O(1)，故总时间复杂度为O(n^2)。

        hash_sum_freq = {}
        result = 0
        
        for a in A:
            for b in B:
                if a+b in hash_sum_freq:
                    hash_sum_freq[a+b] += 1
                else:
                    hash_sum_freq[a+b] = 1

        for c in C:
            for d in D:
                if (-c-d) in hash_sum_freq:
                    result += hash_sum_freq[-c-d]
        return result
