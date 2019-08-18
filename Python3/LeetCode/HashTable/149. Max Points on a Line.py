# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

# Example 1:
# Input: [[1,1],[2,2],[3,3]]
# Output: 3
# Explanation:
# ^
# |
# |        o
# |     o
# |  o  
# +------------->
# 0  1  2  3  4

# Example 2:
# Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4
# Explanation:
# ^
# |
# |  o
# |     o        o
# |        o
# |  o        o
# +------------------->
# 0  1  2  3  4  5  6
# NOTE: input types have been changed on April 15, 2019. 
# Please reset to default code definition to get new method signature.

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # 哈希表 O(n^2)
        # 先枚举一个定点，然后将其它点按斜率分组，斜率指与定点连线的斜率，分组可以利用哈希表。
        # 由于一个定点加斜率可以唯一确定一条直线，所以被分到同一组的点都在一条直线上。组中点数的最大值就是答案。
        # 特殊情况：
        #   竖直直线不存在斜率，需要单独计数；
        #   与定点重合的点可以被分到所有组中，需要单独处理；
        # 时间复杂度分析：
        #   总共枚举 n 个定点，对于每个定点再枚举 n−1 个其余点，
        #   枚举后哈希表操作的时间复杂度是 O(1)，所以总时间复杂度是 O(n^2)。

        if len(points) < 2:
            return len(points)

        mm = {}
        for p in points:
            mm[(p[0],p[1])] = mm.get((p[0],p[1]), 0) + 1

        P = mm.keys()    
        if len(P) == 1:
            return mm[P[0]]

        maxP = 0
        for i in range(len(P)-1):
            slopes = {}
            for j in range(i+1,len(P)):
                dx = P[i][0]-P[j][0]
                dy = P[i][1]-P[j][1]
                if dx == 0:
                    slope = "#"
                elif dy == 0:
                    slope = 0
                else:
                    slope = float(dy) / dx
                slopes[slope] = slopes.get(slope,0) + mm[P[j]]
            maxP = max(maxP, mm[P[i]] + max(slopes.values()))

        return maxP     
        