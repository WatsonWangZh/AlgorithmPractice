# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
# You may assume that the intervals were initially sorted according to their start times.

# Example 1:
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

# Example 2:
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

# NOTE: input types have been changed on April 15, 2019. 
# Please reset to default code definition to get new method signature.

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        # 区间合并 O(n)
        # 对于新区间左边和右边的、与新区间没有重叠的区间，直接将它们按顺序插入；
        # 对于与新区间相交的区间，我们维护合并后区间的左端点和右端点，最后再将合并后的区间插入适当的位置。
        # 时间复杂度分析：每个区间只会遍历一次，所以总时间复杂度是 O(n)。

        i = 0
        j = len(intervals) - 1
        start = newInterval[0]
        end = newInterval[1]

        while i <= j:
            if start > intervals[i][1]:
                i += 1
            else:
                break
        if i == len(intervals):
            return intervals + [newInterval]
        
        while i <= j:
            if end < intervals[j][0]:
                j -= 1
            else:
                break
        if j == -1:
            return [newInterval] + intervals
        
        if i > j:
            return intervals[:i] + [newInterval] + intervals[i:]
        else:
            intervals[j][0] = min(intervals[i][0], start)
            intervals[j][1] = max(intervals[j][1], end)
            del(intervals[i:j])
            return intervals
