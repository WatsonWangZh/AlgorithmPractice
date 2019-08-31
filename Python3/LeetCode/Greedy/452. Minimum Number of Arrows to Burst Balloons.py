# There are a number of spherical balloons spread in two-dimensional space. 
# For each balloon, provided input is the start and end coordinates of the horizontal diameter. 
# Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice. 
# Start is always smaller than end. There will be at most 104 balloons.
# An arrow can be shot up exactly vertically from different points along the x-axis. 
# A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. 
# There is no limit to the number of arrows that can be shot. 
# An arrow once shot keeps travelling up infinitely. 
# The problem is to find the minimum number of arrows that must be shot to burst all balloons.

# Example:
# Input:
# [[10,16], [2,8], [1,6], [7,12]]
# Output:
# 2
# Explanation:
# One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) 
# and another arrow at x = 11 (bursting the other two balloons).

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        # 排序贪心 O(nlogn)
        # 此题可以考虑将区间求交集，最后必定是一些不重叠的独立的区间，独立的区间个数就是答案数。
        # 具体做法如下：
        # 首先将区间按照左端点从小到大排序，左端点相同的按照右端点从小到大排序。
        # 设立两个值left和right代表当前飞镖可以放置的范围。
        # 每当遇到一个新区间，若right小于新区间的起点，则需要一个新飞镖。
        # 否则原飞镖的区间left和新区间的起点取最大值，right和新区间的终点取最小值，即求交集。
        # 时间复杂度
        # 对所有区间排序一次，遍历一次，故总时间复杂度为O(nlogn)。

        n = len(points)
        if n <= 1:
            return n

        points.sort(key=lambda x:(x[0],x[1]))
        end = -1
        cnt = 0

        for left, right in points:
            if end < left:
                cnt += 1
                end = right
            else:
                end = min(end, right)

        return cnt
