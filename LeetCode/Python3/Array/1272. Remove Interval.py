# Given a sorted list of disjoint intervals, each interval intervals[i] = [a, b] represents the set of real numbers x such that a <= x < b.
# We remove the intersections between any interval in intervals and the interval toBeRemoved.
# Return a sorted list of intervals after all such removals.

# Example 1:
# Input: intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
# Output: [[0,1],[6,7]]

# Example 2:
# Input: intervals = [[0,5]], toBeRemoved = [2,3]
# Output: [[0,2],[3,5]]

# Constraints:
# 1 <= intervals.length <= 10^4
# -10^9 <= intervals[i][0] < intervals[i][1] <= 10^9

# Hints:
# Solve the problem for every interval alone.
# Divide the problem into cases according to the position of the two intervals.

class Solution(object):
    def removeInterval(self, intervals, toBeRemoved):
        """
        :type intervals: List[List[int]]
        :type toBeRemoved: List[int]
        :rtype: List[List[int]]
        """
        # 模拟 O(n)
        res = []
        for interval in intervals:
            start, end = interval[0], interval[1]
            if start > toBeRemoved[1] or end < toBeRemoved[0]:
                res.append(interval)
            else:
                if start < toBeRemoved[0]:
                    res.append([start, toBeRemoved[0]])
                if end > toBeRemoved[1]:
                    res.append([toBeRemoved[1],end])
        return res