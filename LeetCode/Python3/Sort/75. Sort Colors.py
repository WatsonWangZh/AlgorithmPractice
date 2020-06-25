# Given an array with n objects colored red, white or blue, 
# sort them in-place so that objects of the same color are adjacent,
# with the colors in the order red, white and blue.
# Here, we will use the integers 0, 1, and 2 
# to represent the color red, white, and blue respectively.
# Note: You are not suppose to use the library's sort function for this problem.

# Example:
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Follow up:
# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
# Could you come up with a one-pass algorithm using only constant space?
# from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # M1. 计数排序
        # 首先遍历一遍原数组，分别记录 红色(0)，白色(1)，蓝色(2) 的个数。
        # 然后更新原数组，按个数分别赋上 红色(0)，白色(1)，蓝色(2)。

        # count = Counter(nums)
        # for i in range(len(nums)):
        #     if i < count[0]:    
        #         nums[i] = 0
        #     elif i < count[0] + count[1]:
        #         nums[i] = 1
        #     else:
        #         nums[i] = 2

        # M2.三指针法 p0, p2, curr
        # https://leetcode.com/problems/sort-colors/solution/

        # for all idx < p0 : nums[idx < p0] = 0
        # curr is an index of element under consideration
        p0 = curr = 0
        # for all idx > p2 : nums[idx > p2] = 2
        p2 = len(nums) - 1

        while curr <= p2:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1

        # M3. 冒泡排序
        
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]