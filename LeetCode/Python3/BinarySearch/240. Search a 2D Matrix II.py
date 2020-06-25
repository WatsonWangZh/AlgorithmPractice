# Write an efficient algorithm that searches for a value in an m x n matrix. 
# This matrix has the following properties:
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.

# Example:
# Consider the following matrix:

# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# Given target = 5, return true.
# Given target = 20, return false.

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # M1. 单调性扫描
        # 初始化 row = 0, col = n-1
        # 若matrix[row][col] > target, 则向左移动 col -= 1;
        # 若matrix[row][col] < target, 则向下移动 row += 1;
        # 若matrix[row][col] = target, 则返回 True;
        # 若越界, 则返回 False.
        # 时间复杂度：
        # 可以看到每次col向左移动或者row向下移动, 移动次数不超过n+m次，故时间复杂度为O(n+m)。

        # edge case  
        if not matrix or not matrix[0]:
            return False
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        # use row and col to represent the index of element in matrix, and compare it with target 
        row = 0
        col = len(matrix[0]) - 1
        while True:
            if matrix[row][col] > target:
                col -= 1
            elif matrix[row][col] < target:
                row += 1
            else:
                return True 
            # exit condition
            if col < 0 or row > len(matrix[0]) - 1: 
                return False
        