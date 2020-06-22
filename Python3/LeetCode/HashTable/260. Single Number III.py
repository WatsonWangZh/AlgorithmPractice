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
        from collections import Counter
        count = Counter(nums)
        return [x for x in count if count[x] == 1]    

        # M2. 滚动增删
        res = []
        for num in nums:
            if num in res:
                res.remove(num)
            else:
                res.append(num)
        return res

        # https://leetcode.com/problems/single-number-iii/solution/
        # M3. Awesome XOR Bit Manipulation!
        # difference between two numbers (x and y) which were seen only once
        bitmask = 0
        for num in nums:
            bitmask ^= num
        # print(bin(bitmask)[2:])
        # rightmost 1-bit diff between x and y
        diff = bitmask & (-bitmask)
        # print(bin(diff)[2:])
        x = 0
        for num in nums:
            # bitmask which will contain only x
            if num & diff:
                x ^= num
        
        return [x, bitmask^x]

