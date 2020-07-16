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


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        # 滑动窗口 始终保持窗口内最多只有一个0
        n = len(nums)
        res = 0
        l, r = 0, 0
        zero_count = 0
        while r < n:
            if nums[r] == 0:
                zero_count += 1
            while zero_count > 1 and l < n:
                zero_count -= int(not nums[l])
                l += 1
            res = max(res, r - l + 1 - 1)
            r += 1
        return res