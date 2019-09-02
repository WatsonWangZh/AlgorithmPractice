# Given an unsorted array nums, 
# reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]...

# Example:
# Input: nums = [3,5,2,1,6,4]
# Output: One possible answer is [3,5,1,6,2,4]

class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # M1. 排序交换 O(nlgn)
        # 先给数组排个序，
        # 然后我们只要每次把第三个数和第二个数调换个位置，第五个数和第四个数调换个位置，
        # 以此类推直至数组末尾，这样我们就能完成摆动排序了。

        # nums.sort()
        # if len(nums) <= 2:
        #     return nums
        # for i in range(2, len(nums), 2):
        #     nums[i], nums[i-1] = nums[i-1], nums[i]

        # M2. 遍历规律 O(n)
        # 如果偶数index的值比下一个值大, 则交换位置; 
        # 如果奇数index的值比下一个值小, 则交换位置.

        for i in range(len(nums)-1):
            if i%2 == 1 and nums[i]< nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
            elif i%2 == 0 and nums[i]> nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
