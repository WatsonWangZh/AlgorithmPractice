# Given a sequence of n integers a1, a2, ..., an, 
# a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. 
# Design an algorithm that takes a list of n numbers as input 
# and checks whether there is a 132 pattern in the list.
# Note: n will be less than 15,000.

# Example 1:
# Input: [1, 2, 3, 4]
# Output: False
# Explanation: There is no 132 pattern in the sequence.

# Example 2:
# Input: [3, 1, 4, 2]
# Output: True
# Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

# Example 3:
# Input: [-1, 3, 2, 0]
# Output: True
# Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].

class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # M1. 蛮力算法 O(n^3) [Time Limit Exceeded]
        # for i in range(len(nums)-2):
        #     for j in range(i+1, len(nums)-1):
        #         for k in range(j+1, len(nums)):
        #             if nums[k] > nums[i] and nums[j] > nums[k]:
        #                 return True
        # return False

        # M2. 单调栈 O(n)
        if len(nums) < 3:
            return False
        
        stack = [[nums[0], nums[0]]]
        
        minimum = nums[0]
        
        for num in nums[1:]:
            if num <= minimum:
                minimum = num
            else:
                while stack and stack[-1][0] < num:
                    if num < stack[-1][1]:
                        return True
                    else:
                        stack.pop()
                stack.append([minimum, num])
        return False