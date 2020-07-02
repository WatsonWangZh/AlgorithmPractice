# A peak element is an element that is greater than its neighbors.
# Given an input array nums, where nums[i] ≠ nums[i+1], 
# find a peak element and return its index.
# The array may contain multiple peaks, 
# in that case return the index to any one of the peaks is fine.
# You may imagine that nums[-1] = nums[n] = -∞.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.

# Example 2:
# Input: nums = [1,2,1,3,5,6,4]
# Output: 1 or 5 
# Explanation: Your function can return either index number 1 where the peak element is 2, 
#              or index number 5 where the peak element is 6.
# Note:
# Your solution should be in logarithmic complexity.

class Solution(object):
    # 使用单调区间的变换点来寻找peek值:
    # 如果nums[mid]<nums[mid-1],那么在[0,mid-1]区间一定具有一个peek值，
    # 反之，在[mid,len（nums）-1]区间一定有一个peek值。
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1 or nums[0]>nums[1]:
            return 0
        l,r = 1,len(nums)-1
        while l<r:
            mid = l+(r-l+1)//2
            if nums[mid]<nums[mid-1]:
                r = mid-1
            else:
                l = mid
        return l
        