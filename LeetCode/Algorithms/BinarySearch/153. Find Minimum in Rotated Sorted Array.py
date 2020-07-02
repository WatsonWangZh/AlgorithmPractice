# Suppose an array sorted in ascending order is 
# rotated at some pivot unknown to you beforehand.
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
# Find the minimum element.
# You may assume no duplicate exists in the array.

# Example 1:
# Input: [3,4,5,1,2] 
# Output: 1

# Example 2:
# Input: [4,5,6,7,0,1,2]
# Output: 0

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # M1.朴素想法
        # if not nums:
        #     return -1
        # 没有rotate的情况
        # if nums[0] <= nums[-1]:
        #     return nums[0]
        # for i in range(len(nums)):
        #     if nums[i+1] < nums[i]:
        #         return nums[i+1]

        # M2.折半查找
        if not nums: 
            return -1
        # 没有rotate的情况
        if nums[0] <= nums[-1]: 
            return nums[0]

        l, r = 1, len(nums) - 1
        while l < r:
            mid = l + (r - l)//2
            if nums[mid] > nums[0]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
      
        