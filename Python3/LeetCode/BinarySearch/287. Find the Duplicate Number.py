# Given an array nums containing n + 1 integers where each integer is 
# between 1 and n (inclusive), prove that at least one duplicate number must exist. 
# Assume that there is only one duplicate number, find the duplicate one.

# Example 1:
# Input: [1,3,4,2,2]
# Output: 2

# Example 2:
# Input: [3,1,3,4,2]
# Output: 3
# Note:
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated more than once.

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # M1.set去重
        # L = set()
        # for i in range(len(nums)):
        #     if nums[i] in L:
        #         return nums[i]
        #     L.add(nums[i])
        # return True

        # M2.抽屉原理 构造两段性 O(nlgn)
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            count = 0
            for n in nums:
                if n <= mid:
                    count += 1
            if count <= mid:
                l = mid + 1
            else:
                r = mid
        return l
        