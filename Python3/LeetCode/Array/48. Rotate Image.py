# You are given an n x n 2D matrix representing an image.
# Rotate the image by 90 degrees (clockwise).
# Note:
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
# DO NOT allocate another 2D matrix and do the rotation.

# Example 1:
# Given input matrix = 
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],
# rotate the input matrix in-place such that it becomes:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]

# Example 2:
# Given input matrix =
# [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ], 
# rotate the input matrix in-place such that it becomes:
# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # (操作分解) O(n^2)
        # 直接操作旋转 90度 比较困难，我们可以将它分解成两个操作：
        # 先以主对角条线为轴做翻转；
        # 再以每行中心的竖线为轴做翻转；
        # 时间复杂度：O(n^2)， 额外空间：O(1)

        n = len(matrix)
        # 以主对角条线为轴做翻转
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # 以每行中心的竖线为轴做翻转
        for i in range(n):
            matrix[i].reverse()