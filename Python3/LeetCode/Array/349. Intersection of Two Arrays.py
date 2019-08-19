# Given two arrays, write a function to compute their intersection.

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]

# Note:
# Each element in the result must be unique.
# The result can be in any order.

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # M1. 暴力求解
        # 最直观的办法是，对数组1中的每个数，遍历检查数组2中是否有相同的数。
        # 时间复杂度 O(m) * O(n)

        # result = []
        # for num in nums1:
        #     if num not in result and num in nums2:
        #         result.append(num)

        # return result

        # M2. 用字典统计第一个列表都出现了哪些数，
        # 然后顺序遍历第二个列表，发现同时出现的数则加入到结果列表中。
        # 时间复杂度 O(m) + O(n)

        result = []
        memo = {}
        for num in nums1:
            memo[num] = memo[num]+1 if num in memo else 1
        for num in nums2:
            if num in memo and memo[num] > 0:
                result.append(num)
                memo[num] = 0

        return result
        