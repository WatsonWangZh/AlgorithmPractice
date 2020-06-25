# Given a sorted integer array without duplicates, return the summary of its ranges.

# Example 1:
# Input:  [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.

# Example 2:
# Input:  [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # 模拟 线性扫描 O(n)
        # 从前往后扫描整个数组，扫描时维护当前区间的起点 st 和终点 ed，
        # 如果当前数可以接在区间结尾，则更新 ed；
        # 否则打印 [st,ed]，
        # 然后将 st 和 ed 更新成当前数。
        # 时间复杂度分析：每个数仅被遍历一次，所以时间复杂度是 O(n)。

        if not nums:
            return []
        res = []
        st = ed = nums[0]
        for num in nums[1:]:
            if num == ed + 1:
                ed += 1
            else:
                res.append(str(st) if st == ed else str(st) + '->' + str(ed))
                st = ed = num
        # for the last case
        res.append(str(st) if st == ed else str(st) + '->' + str(ed))
        return res