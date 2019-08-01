# Given a non-empty array of integers, every element appears three times except for one, 
# which appears exactly once. Find that single one.
# Note:

# Your algorithm should have a linear runtime complexity. 
# Could you implement it without using extra memory?

# Example 1:
# Input: [2,2,3,2]
# Output: 3

# Example 2:
# Input: [0,1,0,1,0,1,99]
# Output: 99

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # M1.hash
        # rep = {}
        # for num in nums:
        #     if not rep.get(num):
        #         rep[num] = 1
        #         continue
        #     rep[num] += 1
        #     if rep[num] == 3:
        #         del rep[num]
        # return int(rep.keys()[0])

        # M2.数学方法
        # s = sum(nums)
        # t = sum(set(nums))
        # return (t*3-s) / 2

        # M3.位运算方法
        # one = 0
        # two = 0
        # three = 0
        # for num in nums:
        #     two = two | (one & num)
        #     one = one ^ num
        #     three = one & two
        #     two = two & (~three)
        #     one = one & (~three)
        # return one
        