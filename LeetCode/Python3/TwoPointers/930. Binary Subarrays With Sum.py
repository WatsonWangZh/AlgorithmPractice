# In an array A of 0s and 1s, how many non-empty subarrays have sum S?

# Example 1:
# Input: A = [1,0,1,0,1], S = 2
# Output: 4
# Explanation: 
# The 4 subarrays are bolded below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
 
# Note:
# A.length <= 30000
# 0 <= S <= A.length
# A[i] is either 0 or 1.

import collections
class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """

        # M1. 记录A中1的下标，找到满足S的基本结果，然后泛化
        # for [1,0,1,0,1]
        # indexes = [-1, 0, 2, 4, 5]
        # [-1] and [len(A)] 处理左右边界情况

        # indexes = [-1] + [ix for ix, v in enumerate(A) if v] + [len(A)]
        # res = 0
        # # 特别处理S=0的情况
        # if S == 0:
        #     for i in range(len(indexes) - 1):
        #         # w: number of zeros between two consecutive ones
        #         w = indexes[i+1] - indexes[i] - 1
        #         res += w * (w+1) / 2
        #     return res

        # for i in range(1, len(indexes) - S):
        #     j = i + S - 1
        #     # left和right分别存储两侧可能的变化数量
        #     left = indexes[i] - indexes[i-1]
        #     right = indexes[j+1] - indexes[j]
        #     res += left * right
        # return res

        # M2. 前缀和 counts数组
        n = len(A)
        pre_sums = [0] * (n + 1)  # 错一位
        counts = [0] * (n + 1)  # index 表示和，counts[index]记录total中出现和为index的个数
        counts[0] = 1

        res = 0
        for i in range(0, n):
            pre_sums[i + 1] = pre_sums[i] + A[i]
            cur_sum = pre_sums[i + 1]
            if cur_sum >= S:
                res += counts[cur_sum - S]
            counts[cur_sum] += 1
        return res

        # M3. Three Pointers TODO
