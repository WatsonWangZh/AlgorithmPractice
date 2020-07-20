# 1512. Number of Good Pairs
# User Accepted:6599
# User Tried:6708
# Total Accepted:6739
# Total Submissions:7354
# Difficulty:Easy
# Given an array of integers nums.
# A pair (i,j) is called good if nums[i] == nums[j] and i < j.
# Return the number of good pairs.

# Example 1:
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

# Example 2:
# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.

# Example 3:
# Input: nums = [1,2,3]
# Output: 0

# Constraints:
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100

from collections import  defaultdict
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # 模拟
        n = len(nums)
        res = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    res += 1
        return res

        # 计数统计
        cnt = defaultdict(int)
        for num in nums:
            cnt[num] += 1

        res = 0
        for v, c in cnt.items():
            res += c * (c - 1) // 2
        return res
