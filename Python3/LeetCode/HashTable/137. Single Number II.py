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


# 二刷 HashMap   
from collections import Counter
class Solution:
    def singleNumber(self, nums):
        count = Counter(nums)
            
        for k in count.keys():
            if count[k] == 1:
                return k

# 二刷 HashSet   
class Solution:
    def singleNumber(self, nums):
        return (3 * sum(set(nums)) - sum(nums)) // 2


# https://leetcode.com/problems/single-number-ii/solution/
# Awesome  XOR Bit Manipulation!
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen_once = seen_twice = 0
        
        for num in nums:
            # first appearance: 
            # add num to seen_once 
            # don't add to seen_twice because of presence in seen_once
            
            # second appearance: 
            # remove num from seen_once 
            # add num to seen_twice
            
            # third appearance: 
            # don't add to seen_once because of presence in seen_twice
            # remove num from seen_twice
            seen_once = ~seen_twice & (seen_once ^ num)
            seen_twice = ~seen_once & (seen_twice ^ num)

        return seen_once