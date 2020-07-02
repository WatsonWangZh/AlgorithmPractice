# A group of two or more people wants to meet and minimize the total travel distance. 
# You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. 
# The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

# Example:
# Input: 
# 1 - 0 - 0 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0
# Output: 6 
# Explanation: Given three people living at (0,0), (0,4), and (2,2):
#              The point (0,2) is an ideal meeting point, as the total travel distance 
#              of 2+2+2=6 is minimal. So return 6.

# Hints:
# Try to solve it in one dimension first. How can this solution apply to the two dimension case?

class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # https://leetcode.com/problems/best-meeting-point/solution/
        # 排序  O(mnlogmn) 曼哈顿距离各维度相互独立，二维问题等价于一维问题相加。
        # Time complexity : O(mnlogmn). 
        # Since there could be at most m×nm×n points, therefore the time complexity is O(mnlogmn) due to sorting.
        # Space complexity : O(mn).

        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        rows = []
        cols = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)

        rows.sort()
        cols.sort()

        res = 0
        x = rows[len(rows) // 2]
        y = cols[len(cols) // 2]

        for i in range(len(rows)):
            res += abs(rows[i] - x)
            res += abs(cols[i] - y)

        return res 
        