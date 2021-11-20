# 1493. Longest Subarray of 1's After Deleting One Element
# User Accepted:3497
# User Tried:3867
# Total Accepted:3616
# Total Submissions:6849
# Difficulty:Medium
# Given a binary array nums, you should delete one element from it.
# Return the size of the longest non-empty subarray containing only 1's in the resulting array.
# Return 0 if there is no such subarray.

# Example 1:
# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

# Example 2:
# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, 
# [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

# Example 3:
# Input: nums = [1,1,1]
# Output: 2
# Explanation: You must delete one element.

# Example 4:
# Input: nums = [1,1,0,0,1,1,1,0,1]
# Output: 4

# Example 5:
# Input: nums = [0,0,0]
# Output: 0
 
# Constraints:
# 1 <= nums.length <= 10^5
# nums[i] is either 0 or 1.

# TLE
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if sum(nums) == len(nums):
            return sum(nums) - 1
        
        def helper(nums):
            cnt = 0
            res = 0
            for i in range(len(nums)):
                if nums[i] == 1:
                    cnt += 1
                if nums[i] == 0:
                    res = max(res, cnt)
                    cnt = 0
                res = max(res, cnt)
            return res
        
        t = 0
        r = 0
        fwd = [0] * len(nums)
        bwd = [0] * len(nums)
        leave = [0] * len(nums)
        
        for i in range(len(nums)):   
            fwd[i] = helper(nums[:i])
            bwd[i] = helper(nums[i+1:])
            leave[i] = helper(nums[:i]+nums[i+1:])
            
        res = [0] * len(nums)
        if nums[0] == 0:
            res[0] = bwd[0]
        if nums[-1] == 0:
            res[0] = fwd[0]
            
        tmp = [1] * len(nums)
        if nums[0] == 0 and nums[1] == 0:
            tmp[0] = 0
        if nums[-1] == 0 and nums[-2] == 0:
            tmp[0] = 0
        for i in range(1, len(nums)-1):
            if (nums[i] == 0 and nums[i+1] == 0) or (nums[i] == 0 and nums[i-1] == 0):
                tmp[i] = 0
                
        # print(tmp)
        for i in range(1, len(nums)-1):
            if nums[i] == 0 and tmp[i]:
                res[i] = leave[i]
            elif nums[i] == 0:
                res[i] = max(fwd[i], bwd[i])
            if nums[i] == 1:
                res[i] = max(fwd[i], bwd[i])
                
        # for i in range(len(nums)):
        #     res[i] *= tmp[i]
            
        # print(fwd, bwd, res)
        return max(res)