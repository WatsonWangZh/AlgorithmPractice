# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

# Example 1:
# Input: [1, 2, 2, 3, 1]
# Output: 2
# Explanation: 
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.

# Example 2:
# Input: [1,2,2,3,1,4,2]
# Output: 6

# Note:
# nums.length will be between 1 and 50,000.
# nums[i] will be an integer between 0 and 49,999.

# Hints:
# Say 5 is the only element that occurs the most number of times - for example, nums = [1, 5, 2, 3, 5, 4, 5, 6]. What is the answer?

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 统计各元素起始、终结位置及频数
        # 在频数最多的待选项中更新最终结果
        left, right, count = {}, {}, {}
        for i, num in enumerate(nums):
            if num not in left:
                left[num] = i
            right[num] = i
            count[num] = count.get(num, 0) + 1
        
        res = len(nums)
        degree = max(count.values())
        for num in count:
            if count[num] == degree:
                res = min(res, right[num] - left[num] + 1)
        return res