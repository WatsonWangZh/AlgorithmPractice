# Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given points.

# Example 1:
# Input: [[1,1],[-1,1]]
# Output: true

# Example 2:
# Input: [[1,1],[-1,-1]]
# Output: false

# Follow up:
# Could you do better than O(n^2) ?

import collections
class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        # 按y值分组，寻找x轴中心值，看对称与否
        if not points:
            return True

        group_by_y = collections.defaultdict(list)
        min_x, max_x = float("inf"), float("-inf")

        for point in points:
            group_by_y[point[1]].append(point[0])
            min_x = min(min_x, point[0])
            max_x = max(max_x, point[0])

        mid = min_x + max_x

        for group in group_by_y.values():
            for item in group:
                if mid - item not in group:
                    return False

        return True
