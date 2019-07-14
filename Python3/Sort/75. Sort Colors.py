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
        # 经典荷兰国旗问题
        # M1. two-pass algorithm
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

        # M2.双指针法
        lred_idx, rblue_idx = 0, len(nums)-1
        cur = lred_idx
        # 用两个指针把红色元素移到最左边，蓝色元素移到最右边
        while cur <= rblue_idx:
            if nums[cur] == 0:
                nums[cur], nums[lred_idx] = nums[lred_idx], nums[cur]
                cur += 1
                lred_idx += 1
            elif nums[cur] == 2:
                nums[cur], nums[rblue_idx] = nums[rblue_idx], nums[cur]
                rblue_idx -= 1
            else:
                cur += 1
                
        