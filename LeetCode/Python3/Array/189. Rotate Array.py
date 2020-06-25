# Given an array, rotate the array to the right by k steps, where k is non-negative.

# Example 1:
# Input: [1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Example 2:
# Input: [-1,-100,3,99] and k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

# Note:
# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
# Could you do it in-place with O(1) extra space?

# Hints:
# The easiest solution would use additional memory and that is perfectly fine.
# The actual trick comes when trying to solve this problem without using any additional memory. 
# This means you need to use the original array somehow to move the elements around. 
# Now, we can place each element in its original location and shift all the elements around it 
# to adjust as that would be too costly and most likely will time out on larger input arrays.
# One line of thought is based on reversing the array (or parts of it) to obtain the desired result. 
# Think about how reversal might potentially help us out by using an example.
# The other line of thought is a tad bit complicated but essentially it builds on the idea of placing 
# each element in its original position while keeping track of the element originally in that position. 
# Basically, at every step, we place an element in its rightful position and 
# keep track of the element already there or the one being overwritten in an additional variable. 
# We can't do this in one linear pass and the idea here is based on cyclic-dependencies between elements.

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # M1. 辅助数组 模拟 O(n) O(n)
        if k == 0:
            return
        n = len(nums)
        res = [0] * n
        for i in range(0, n):
            index = (i + k) % n
            res[index] = nums[i]
        nums[:] = res

        # M2. 翻转数组 O(n) O(1)
        n = len(nums)
        k = k % len(nums)
        self.reverse(nums, 0, n-k-1)
        self.reverse(nums, n-k, n-1)
        self.reverse(nums, 0, n-1)

    def reverse(self, array, i, j):
        while i < j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

        # M3. 直接交换 O(n) O(1)
        k = k % len(nums)
        nums[:k], nums[k:] = nums[len(nums)-k:], nums[:len(nums)-k]

        # M4. 直接组合 O(n) O(n)
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]