# Implement next permutation, which rearranges numbers 
# into the lexicographically next greater permutation of numbers.

# If such arrangement is not possible, 
# it must rearrange it as the lowest possible order (ie, sorted in ascending order).

# The replacement must be in-place and use only constant extra memory.
# Here are some examples.
# Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

class Solution(object):
    def nextPermutation(self, nums):

        n = len(nums)
        i,j = n-1, n-1

        # From right to left, find the first decreasing number
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1 
        
        # [3,2,1] -> [1,2,3]
        if i==0: 
            nums[:]=nums[::-1]
            return nums

        # From right to left, finding number just larget than the first decreasing number
        for j in range(n-1, i-1, -1):
            if nums[j] > nums[i-1]:
                break 
             
        # Swap 
        nums[j], nums[i-1] = nums[i-1], nums[j]

        # Reversing the backend numbers
        nums[i:] = nums[i:][::-1]

        return nums
