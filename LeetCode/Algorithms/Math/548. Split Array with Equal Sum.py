# Given an array with n integers, 
# you need to find if there are triplets (i, j, k) which satisfies following conditions:
# 0 < i, i + 1 < j, j + 1 < k < n - 1
# Sum of subarrays (0, i - 1), (i + 1, j - 1), (j + 1, k - 1) and (k + 1, n - 1) should be equal.
# where we define that subarray (L, R) represents a slice of the original array 
# starting from the element indexed L to the element indexed R.

# Example:
# Input: [1,2,1,2,1,2,1]
# Output: True
# Explanation:
# i = 1, j = 3, k = 5. 
# sum(0, i - 1) = sum(0, 0) = 1
# sum(i + 1, j - 1) = sum(2, 2) = 1
# sum(j + 1, k - 1) = sum(4, 4) = 1
# sum(k + 1, n - 1) = sum(6, 6) = 1

# Note:
# 1 <= n <= 2000.
# Elements in the given array will be in range [-1,000,000, 1,000,000].

import collections
class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # M1. 蛮力算法 O(n^4) O(1) TLE
        # 找出n,i,j,k的约束（变动范围）,然后蛮力搜索对应区间的字段和，看是否存在满足条件的结果。
        # 1 ≤ i ≤ n-6
        # i+2 ≤ j ≤ n-4
        # j+2 ≤ k ≤ n-2

        # n = len(nums)
        # if n < 7:
        #     return False
        # for i in range(1, n - 5):
        #     sum1 = sum(nums[:i])
        #     for j in range(i+2, n-3):
        #         sum2 = sum(nums[i+1:j])
        #         for k in range(j+2, n-1):
        #             sum3 = sum(nums[j+1:k])
        #             sum4 = sum(nums[k+1:])
        #             if sum1 == sum2 == sum3 == sum4:
        #                 return True
        # return False

        # M2. 前缀和数组 O(n^3) O(n) TLE
        # 优化上一步中的sum子串和操作。
        # n = len(nums)
        # if n < 7:
        #     return False

        # cum_sum = [0 for i in range(n)]
        # cum_sum[0] = nums[0]
        # for i in range(1, n):
        #     cum_sum[i] = cum_sum[i - 1] + nums[i]

        # for i in range(1, n - 5):
        #     sum1 = cum_sum[i-1]
        #     for j in range(i+2, n-3):
        #         sum2 = cum_sum[j-1] - cum_sum[i]
        #         for k in range(j+2, n-1):
        #             sum3 = cum_sum[k-1] - cum_sum[j]
        #             sum4 = cum_sum[n-1] - cum_sum[k]
        #             if sum1 == sum2 == sum3 == sum4:
        #                 return True
        # return False

        # M3. 前缀和数组 O(n^3) O(n) TLE
        # 早发现，早治疗。减少无谓的求解操作。
        # n = len(nums)
        # if n < 7:
        #     return False

        # cum_sum = [0 for i in range(n)]
        # cum_sum[0] = nums[0]
        # for i in range(1, n):
        #     cum_sum[i] = cum_sum[i - 1] + nums[i]

        # for i in range(1, n - 5):
        #     sum1 = cum_sum[i-1]
        #     for j in range(i+2, n-3):
        #         sum2 = cum_sum[j-1] - cum_sum[i]
        #         # 早发现，早治疗。减少无谓的求解操作。
        #         if sum1 != sum2:
        #             continue
        #         for k in range(j+2, n-1):
        #             sum3 = cum_sum[k-1] - cum_sum[j]
        #             sum4 = cum_sum[n-1] - cum_sum[k]
        #             if sum1 == sum2 == sum3 == sum4:
        #                 return True
        # return False

        # M4. 前缀和数组 + HashTable 减小搜索空间
        # O(n^3) O(n) TLE
        # n = len(nums)
        # if n < 7:
        #     return False
        # table = collections.defaultdict(list)
        # cum_sum = tot = 0
        # for i in range(n):
        #     cum_sum += nums[i]
        #     table[cum_sum].append(i)
        #     tot += nums[i]
        # cum_sum = nums[0]

        # for i in range(1, n-5):
        #     if 2*cum_sum + nums[i] in table.keys():
        #         for j in table[2*cum_sum + nums[i]]:
        #             j += 1
        #             if j > i + 1 and j < n-3 and 3*cum_sum + nums[i] + nums[j] in table.keys():
        #                 for k in table[3*cum_sum + nums[i] + nums[j]]:
        #                     k += 1
        #                     if k > j+1 and k < n - 1 and 4 * cum_sum + nums[i] + nums[j] + nums[k] == tot:
        #                         return True
        #     cum_sum += nums[i]
        # return False
        
        # M5. 前缀和数组 + HashTable + 找中点 分两段
        # O(n^2) O(n) TLE
        n = len(nums)
        if n < 7:
            return False
        cum_sum = [0 for i in range(n)]
        cum_sum[0] = nums[0]
        for i in range(1, n):
            cum_sum[i] = cum_sum[i-1] + nums[i]

        for j in range(3, n-3):
            table = set()
            for i in range(1, j-1):
                if cum_sum[i-1] == cum_sum[j-1] - cum_sum[i]:
                    table.add(cum_sum[i-1])
            for k in range(j+2, n-1):
                if cum_sum[n-1] - cum_sum[k] == cum_sum[k-1] - cum_sum[j] and cum_sum[k-1] - cum_sum[j] in table:
                    return True
        return False
