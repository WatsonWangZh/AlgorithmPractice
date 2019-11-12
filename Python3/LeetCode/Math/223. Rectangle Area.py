# Find the total area covered by two rectilinear rectangles in a 2D plane.
# Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

# Example:
# Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
# Output: 45

# Note:
# Assume that the total area is never beyond the maximum possible value of int.

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        # 计算几何 O(1)
        # 两个矩形并集的面积 = 两个矩形的总面积 - 两个矩形交集的面积。
        # 两个矩形如果有交集，那么交集一定是矩形，剩下的问题是求出交集的长和宽。
        # 求交集的长和宽是一个一维问题，即在数轴上给出线段 [A,B] 和 [C,D]，求它们交集的长度。
        # 其交集的长度：L=min(B,D)−max(A,C)，如果 L<0，说明两个线段不重合。
        total_area = (C-A)*(D-B) + (G-E)*(H-F) 

        overlap_height = max(min(H,D) - max(B,F),0)
        overlap_width = max(min(C,G) - max(A,E),0)
        overlap_area = overlap_height * overlap_width
        
        return total_area -  overlap_area