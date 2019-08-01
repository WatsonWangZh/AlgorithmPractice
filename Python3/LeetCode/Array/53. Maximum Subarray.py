# Given an integer array nums, find the contiguous subarray (containing at least one number) 
# which has the largest sum and return its sum.

# Example:
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Follow up:
# If you have figured out the O(n) solution, try coding another solution 
# using the divide and conquer approach, which is more subtle.

# 动态规划 O(n)
# 定义两个变量maxsum和currsum，其中maxsum保存最终要返回的结果，
# 即最大的子数组之和，currsum初始值为nums[0]，每遍历一个数字num，
# 比较currsum + num和num中的较大值存入currsum，
# 然后再把maxsum和currsum中的较大值存入maxsum，以此类推直到遍历完整个数组，
# 可得到最大子数组的值存在maxsum中。

# class Solution(object):
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if not nums:
#             return 0
        
#         currsum = maxsum = nums[0]
#         for x in nums[1:]:
#             currsum = max(currsum + x,x)
#             maxsum = max(maxsum, currsum)
#         return maxsum

# 分治算法 O(nlogn)
# 思路类似于二分搜索法，把数组一分为二，分别找出左边和右边的最大子数组之和，
# 然后还要从中间开始向左右分别扫描，求出最大值
# 分别和左右两边得出的最大值相比较取最大的那一个
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        else:
            return self.helper(nums, 0, len(nums)-1)

    def helper(self, nums, left, right):
        if left >= right:
            return nums[left]
        mid = ( left + right ) // 2
        lmax = self.helper(nums, left, mid)
        rmax = self.helper(nums, mid+1, right)
        temp = mmax = nums[mid]
        for i in range(mid-1, left-1, -1):
            temp += nums[i]
            mmax = max(mmax, temp)
        temp = mmax
        for i in range(mid+1, right+1, 1):
            temp += nums[i]
            mmax = max(mmax, temp)
        return max(lmax, mmax, rmax)
        





