# Given an integer array nums, find the contiguous subarray within an array 
# (containing at least one number) which has the largest product.

# Example 1:
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Example 2:
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

class Solution(object):
    def maxProduct(self, nums) -> int:

        # 递归
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        
        numofNeg = 0
        result = 1
        negIndex = []
        zeroIndex = []
        
        for i in range(len(nums)):
            result *= nums[i]
            if nums[i] == 0:
                zeroIndex.append(i)
            if nums[i] < 0:
                negIndex.append(i)
                numofNeg += 1
                
        if len(zeroIndex) != 0:
            temp = max(self.maxProduct(nums[:zeroIndex[0]]), self.maxProduct(nums[zeroIndex[0]+1:]))
            if temp > 0:
                return temp
            else:
                return 0
                
        if numofNeg % 2 == 0:
            return result
        else:
            return max(self.maxProduct(nums[negIndex[0]+1:]), self.maxProduct(nums[:negIndex[-1]]))


        # 动态规划
        if not nums:
            return 0
        res, curmax, curmin = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            premax, premin = curmax, curmin
            curmax = max(nums[i], premax*nums[i], premin*nums[i])
            curmin = min(nums[i], premax*nums[i], premin*nums[i])
            res = max(res, curmax)
        return res
