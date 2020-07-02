# You are given a sorted array consisting of only integers where every element appears exactly twice, 
# except for one element which appears exactly once. 
# Find this single element that appears only once.

# Example 1:
# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2

# Example 2:
# Input: [3,3,7,7,10,11,11]
# Output: 10
 
# Note: Your solution should run in O(log n) time and O(1) space.

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # M1. 位运算 O(n) O(1)
        res = 0
        for num in nums:
            res ^= num
        return res

        # M2. 折半查找 注意二分性质的发现 O(lgn) O(1)
        l, r = 0, len(nums) - 1   
        while l < r:
            mid = (l+r) >> 1
            tails_are_even = (r - mid + 1) % 2 == 1
            if nums[mid + 1] == nums[mid]:
                if tails_are_even:
                    l = mid + 2
                else:
                    r = mid - 1
            elif nums[mid - 1] == nums[mid]:
                if tails_are_even:
                    r = mid - 2
                else:
                    l = mid + 1
            else:
                return nums[mid]
        return nums[l]