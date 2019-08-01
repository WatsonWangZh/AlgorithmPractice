# Write an efficient algorithm that searches for a value in an m x n matrix. 
# This matrix has the following properties:
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

# Example 1:
# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# Output: true

# Example 2:
# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# Output: false

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # M1.朴素想法 
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] == target:
        #                return True
        # return False

        # M2.分行列 构造两段性 
        if not matrix or not matrix[0]:
            return False
        rl, rh, cl, ch = 0, len(matrix), 0, len(matrix[0])
        while rl + 1 < rh:
            rm = (rl + rh) // 2
            if matrix[rm][0] == target:
                return True
            elif matrix[rm][0] > target:
                rh = rm
            else:
                rl = rm
        while cl < ch:
            cm = (cl + ch) // 2
            if matrix[rl][cm] == target:
                return True
            elif matrix[rl][cm] > target:
                ch = cm
            else:
                cl = cm + 1
        return False
