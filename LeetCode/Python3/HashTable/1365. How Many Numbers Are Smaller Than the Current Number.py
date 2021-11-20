# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. 
# That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
# Return the answer in an array.

# Example 1:
# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]
# Explanation: 
# For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
# For nums[1]=1 does not exist any smaller number than it.
# For nums[2]=2 there exist one smaller number than it (1). 
# For nums[3]=2 there exist one smaller number than it (1). 
# For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

# Example 2:
# Input: nums = [6,5,4,8]
# Output: [2,1,0,3]

# Example 3:
# Input: nums = [7,7,7,7]
# Output: [0,0,0,0]
 
# Constraints:
# 2 <= nums.length <= 500
# 0 <= nums[i] <= 100

# Hints:
# Brute force for each array element.
# In order to improve the time complexity, we can sort the array and get the answer for each array element.

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # M1. 模拟 O(n^2) O(1)
        res = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if i != j and nums[i] > nums[j]:
                    count += 1
            res.append(count)
        
        return res

        # M2. 分桶 前缀和数组 O(n) O(n)
        bucket = [0] * 101
        for num in nums:
            bucket[num] += 1
            
        accu = [0] * 101
        for i in range(1, 101):   # 1 ~ 100
            accu[i] = accu[i-1] + bucket[i-1]
            
        return [ accu[num] for num in nums ]