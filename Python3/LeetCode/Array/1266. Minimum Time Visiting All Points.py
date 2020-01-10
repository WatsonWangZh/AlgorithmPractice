# On a plane there are n points with integer coordinates points[i] = [xi, yi]. Your task is to find the minimum time in seconds to visit all points.
# You can move according to the next rules:
# In one second always you can either move vertically, 
# horizontally by one unit or diagonally (it means to move one unit vertically and one unit horizontally in one second).
# You have to visit the points in the same order as they appear in the array.

# Example 1:
# Input: points = [[1,1],[3,4],[-1,0]]
# Output: 7
# Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]   
# Time from [1,1] to [3,4] = 3 seconds 
# Time from [3,4] to [-1,0] = 4 seconds
# Total time = 7 seconds

# Example 2:
# Input: points = [[3,2],[-2,2]]
# Output: 5
 
# Constraints:
# points.length == n
# 1 <= n <= 100
# points[i].length == 2
# -1000 <= points[i][0], points[i][1] <= 1000

class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # 画图找规律遍历 O(n)
        # 设两点横坐标的差值为 dx，纵坐标的差值为 dy，则最少的步数为 max(dx, dy)。
        # 时间复杂度
        #   遍历数组一次，故时间复杂度为 O(n)。
        # 空间复杂度
        #   仅需要常数的额外空间。

        res = 0
        x, y = points[0][0], points[0][1]
        for i in range(1, len(points)):
            res += max(abs(x-points[i][0]), abs(y-points[i][1]))
            x = points[i][0]
            y = points[i][1]
        return res
