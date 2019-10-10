# Given an array consisting of n integers, 
# find the contiguous subarray whose length is greater than or equal to k that has the maximum average value. 
# And you need to output the maximum average value.

# Example 1:
# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75
# Explanation:
# when length is 5, maximum average value is 10.8,
# when length is 6, maximum average value is 9.16667.
# Thus return 12.75.

# Note:
# 1 <= k <= n <= 10,000.
# Elements of the given array will be in range [-10,000, 10,000].
# The answer with the calculation error less than 10-5 will be accepted.

import numpy as np
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # M1. 蛮力算法 双重循环 O(n^2) O(1) Time Limit Exceeded
        # res = float('-inf')
        # for s in range(len(nums) - k + 1):
        #     temp_sum = 0
        #     for i in range(s, len(nums)):
        #         temp_sum += nums[i]
        #         if i - s + 1 >= k:
        #             res = max(res, temp_sum * 1.0 / (i-s+1))
        # return res
        
        # M2. 折半查找 + 滑动窗口(尺举法) O(n) O(n)
        # with numpy
        # low, high = min(nums), max(nums)
        # nums = np.array([0]+nums)
        # while high - low > 1e-5:
        #     mid = nums[0] = (low + high) >> 1
        #     pre_sums = (nums - mid).cumsum()
        #     pre_mins = np.minimum.accumulate(pre_sums)

        #     if (pre_sums[k:] - pre_mins[:k]).max() > 0:
        #         low = mid
        #     else:
        #         high = mid
        # return low # or high

        # M2. 折半查找 + 滑动窗口(尺举法) O(n) O(1)
        # without numpy 
        low, high = min(nums), max(nums)
        while high - low > 1e-5:
            mid = (low + high) / 2.
            if self.larger_than_mid(mid, nums, k):
                low = mid
            else:
                high = mid
        return low # or high

    def larger_than_mid(self, aver, nums, k):
        sum_so_far = 0
        for i in range(k):
            sum_so_far += nums[i] - aver
        if sum_so_far > 0:
            return True

        min_prev, min_so_far = 0., 0.
        for i in range(k, len(nums)):
            sum_so_far += nums[i] - aver
            min_prev += nums[i-k] - aver
            min_so_far = min(min_so_far, min_prev)
            if sum_so_far - min_so_far >= 0:
                return True
        return False