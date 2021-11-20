# Given an array nums and a target value k, find the maximum length of a subarray that sums to k. 
# If there isn't one, return 0 instead.
# Note:
# The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

# Example 1:
# Input: nums = [1, -1, 5, -2, 3], k = 3
# Output: 4 
# Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.

# Example 2:
# Input: nums = [-2, -1, 2, 1], k = 1
# Output: 2 
# Explanation: The subarray [-1, 2] sums to 1 and is the longest.

# Follow Up:
# Can you do it in O(n) time?

# Hints:
# Try to compute a sum of a subsequence very fast, i.e in O(1) … Think of prefix sum array.
# Given S[i] a partial sum that starts at position 0 and ends at i, what can S[i - k] tell you ?
# Use HashMap + prefix sum array.

class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 前缀和数组, 边累加边处理,
        # 只保存第一个出现该累积和的位置，后面再出现直接跳过，
        # 这样算下来就是最长的子数组。
        
        pre_sum = {}
        tmp_sum = 0
        res = 0

        for idx, num in enumerate(nums):
            tmp_sum += num
            remain = tmp_sum - k
            if tmp_sum not in pre_sum:
                pre_sum[tmp_sum] = idx
            if tmp_sum == k:
                res = max(res, idx+1)
            elif remain in pre_sum:
                res = max(res, idx - pre_sum[remain])
            
        return res