# Given an array of numbers nums, in which exactly two elements appear 
# only once and all the other elements appear exactly twice. 
# Find the two elements that appear only once.

# Example:
# Input:  [1,2,1,3,2,5]
# Output: [3,5]

# Note:
# The order of the result is not important. 
# So in the above example, [5, 3] is also correct.
# Your algorithm should run in linear runtime complexity. 
# Could you implement it using only constant space complexity?

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # M1.hash计数 空间复杂度O(n)
        # M2.0^x=x; x^x=0
        tmp = 0
        for num in nums:
            tmp ^= num
        # find the rightmost '1' bit 
        i = 0
        # print(bin(tmp))
        while tmp & 1 == 0:
            tmp >>= 1
            i += 1
        tmp = 1 << i
        # compute in two seperate groups
        first, second = 0, 0
        for num in nums:
            if num & tmp:
                first ^= num
            else:
                second ^= num
        return [first, second]

