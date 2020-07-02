# You are a professional robber planning to rob houses along a street. 
# Each house has a certain amount of money stashed. 
# All houses at this place are arranged in a circle. 
# That means the first house is the neighbor of the last one. 
# Meanwhile, adjacent houses have security system connected and 
# it will automatically contact the police if two adjacent houses were broken into 
# on the same night.
# Given a list of non-negative integers representing the amount of money of each house, 
# determine the maximum amount of money you can rob tonight without alerting the police.

# Example 1:
# Input: [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
#              because they are adjacent houses.

# Example 2:
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        if n == 0:
            return 0 
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        # rob the first house
        rob=nums[0]
        not_rob=0
        for i in range(1,n-1):
            prev_not_rob = not_rob
            not_rob = max(rob,not_rob)
            rob = prev_not_rob+nums[i]
        res = max(rob,not_rob)

        # not rob the first house
        rob=nums[1]
        not_rob=0
        for i in range(2,n):
            prev_not_rob = not_rob
            not_rob = max(rob,not_rob)
            rob = prev_not_rob+nums[i]
        res = max(res, rob, not_rob)
        return res
