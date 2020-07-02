# Given a list of points that form a polygon when joined sequentially, find if this polygon is convex (Convex polygon definition).

# Note:
# There are at least 3 and at most 10,000 points.
# Coordinates are in the range -10,000 to 10,000.
# You may assume the polygon formed by given points is always a simple polygon (Simple polygon definition). 
# In other words, we ensure that exactly two edges intersect at each vertex, and that edges otherwise don't intersect each other.
 
# Example 1:
# [[0,0],[0,1],[1,1],[1,0]]
# Answer: True
# Explanation: picture

# Example 2:
# [[0,0],[0,10],[10,10],[10,0],[5,5]]
# Answer: False
# Explanation: picture

class Solution(object):
    def isConvex(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        # 叉乘计算相邻点间法向量，判断是否全部同方向。
        # 若局部性质全部保证，则为True；有一局部违反，即为False。

        if len(points) < 3:
            return False

        # 二维向量叉乘公式及几何意义
        # https://www.iteye.com/blog/happyprince-2163466
        # https://www.cnblogs.com/grandyang/p/6146986.html
        
        def cross_product(a, b, c): # vec(ab) x vec(ac)
            return (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])

        if all(cross_product(points[i-2], points[i-1], points[i]) >= 0 for i in range(len(points))) \
           or all(cross_product(points[i-2], points[i-1], points[i]) <=0 for i in range(len(points))):
            return True

        return False
