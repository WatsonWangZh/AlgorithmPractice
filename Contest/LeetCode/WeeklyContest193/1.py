# 5453. Running Sum of 1d Array
# User Accepted:7626
# User Tried:7659
# Total Accepted:7837
# Total Submissions:8134
# Difficulty:Easy
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

# Example 2:
# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

# Example 3:
# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]
 
# Constraints:
# 1 <= nums.length <= 1000
# -10^6 <= nums[i] <= 10^6

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        S = [0]*(n+1)
        
        for i,x in enumerate(nums):
            S[i+1] = S[i] + x

        return S[1:]