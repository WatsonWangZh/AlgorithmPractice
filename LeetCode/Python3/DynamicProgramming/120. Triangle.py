# Given a triangle, find the minimum path sum from top to bottom. 
# Each step you may move to adjacent numbers on the row below.
# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

# Note:
# Bonus point if you are able to do this using only O(n) extra space, 
# where n is the total number of rows in the triangle.

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        # 动态规划 时间O(n^2) 空间O(1)
        # 点(i,j)的下一行的相邻数字是(i+1,j)和(i+1,j+1)。
        # f(i,j)表示从下往上走到位置(i,j)时的最小路径和，状态转移方程是
        # f(i,j)=minf(i+1,j),f(i+1,j+1)+(i,j)f(i,j)=minf(i+1,j),f(i+1,j+1)+(i,j)
        # 复杂度分析：
        # 直接把f(i,j)存在位置(i,j)处，不使用额外空间，因此空间复杂度为O(1)。
        # 两层for loop，第一次竖着遍历，第二次横着遍历，时间复杂度为O(n^2)。

        if len(triangle) == 0:
            return None
        if len(triangle) == 1:
            return triangle[0][0]

        for i in range(len(triangle)-2,-1,-1):
            for j in range(len(triangle[i])):
                triangle[i][j] = min(triangle[i+1][j], triangle[i+1][j+1]) + triangle[i][j]
                
        return triangle[0][0]
        