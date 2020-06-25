# Given a set of distinct positive integers, 
# find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:
# Si % Sj = 0 or Sj % Si = 0.
# If there are multiple solutions, return any subset is fine.

# Example 1:
# Input: [1,2,3]
# Output: [1,2] (of course, [1,3] will also be ok)

# Example 2:
# Input: [1,2,4,8]
# Output: [1,2,4,8]

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        if not nums:
            return []
            
        nums = sorted(nums)
        dp = [[x] for x in nums]
        res = []
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]%nums[j] == 0 and len(dp[j])+1 > len(dp[i]):
                    # dp[i]  = dp[j] + nums[i]
                    # TypeError: can only concatenate list (not "int") to list
                    
                    dp[i]  = dp[j] + nums[i:i+1]
                    
            if len(dp[i]) > len(res):
                res = dp[i]
                
        return res
