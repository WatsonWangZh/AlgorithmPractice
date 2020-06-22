# Given a non-empty array of integers, 
# every element appears twice except for one. Find that single one.
# Note:
# Your algorithm should have a linear runtime complexity. 
# Could you implement it without using extra memory?

# Example 1:
# Input: [2,2,1]
# Output: 1

# Example 2:
# Input: [4,1,2,1,2]
# Output: 4

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        # M1.字典增删，留一即为
        times_seen_dict = {}
        for i in range(len(nums)):
            if nums[i] in times_seen_dict:
                times_seen_dict[nums[i]] += 1
            else:
                times_seen_dict[nums[i]] = 1
        
        for key, value in times_seen_dict.items():
            if value == 1:
                return key
        '''
        # M2.空间为1，位运解决
        xor = 0
        for num in nums:
            xor ^= num
             
        return xor
        