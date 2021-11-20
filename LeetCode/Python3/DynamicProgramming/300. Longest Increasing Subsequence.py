# Given an unsorted array of integers, find the length of longest increasing subsequence.

# Example:
# Input: [10,9,2,5,3,7,101,18]
# Output: 4 
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

# Note:
# There may be more than one LIS combination, it is only necessary for you to return the length.
# Your algorithm should run in O(n2) complexity.
# Follow up: Could you improve it to O(n log n) time complexity?

class Solution(object):
    # 看到最大，最长 → 想到DP。

    # M1. - dp[i]表示以nums[i]结尾的最长递增子序列的长度；
        # 初始状态：dp = [1] * len(nums)；
        # 状态方程：dp[i] = max(dp[i], dp[j] + 1) if nums[j] < nums[i] 对于j=0,1…i-1；
    # 时间复杂度O(n^2)。
    
    # def lengthOfLIS(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """

    #     if not nums:
    #         return 0

    #     dp = [1] * len(nums)    # dp[i]表示以i结尾的最长递增子序列的长度
    #     for i in range(len(nums)):
    #         for j in range(i):
    #             if nums[j] < nums[i]:
    #                 dp[i] = max(dp[i], dp[j] + 1)
    #     return max(dp)

    # 优化，时间复杂度(nlogn)
    # 对于一个上升子序列，显然当前最后一个元素越小，越有利于添加新的元素，这样LIS长度自然更长。
    # 维护一arr数组，数组元素表示长度为i+1的LIS结尾元素的最小值(保证每一位都是最小值)， 
    # 此时arr数组的长度就是LIS的长度
    # 对于每一个num，如果≥arr[-1], 直接插入尾部；否则找到arr第一个大于num的位置, 替换
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = []
        for num in nums:
            if not arr or num > arr[-1]:
                arr.append(num)
            else:
                pos = self.getFirstLarger(arr, num)
                arr[pos] = num
        return len(arr)

    def getFirstLarger(self, arr, num):
        l = 0
        r = len(arr) - 1
        while l <= r:
            mid = (l + r) >> 1
            if arr[mid] < num:
                l = mid + 1
            else:
                if mid > 0 and arr[mid-1] > num:
                    r = mid - 1
                else:
                    return mid
