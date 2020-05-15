# Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) 
# and lower right corner (row2, col2).
# Range Sum Query 2D
# The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), 
# which contains sum = 8.

# Example:
# Given matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]
# sumRegion(2, 1, 4, 3) -> 8
# update(3, 2, 2)
# sumRegion(2, 1, 4, 3) -> 10

# Note:
# The matrix is only modifiable by the update function.
# You may assume the number of calls to update and sumRegion function is distributed evenly.
# You may assume that row1 ≤ row2 and col1 ≤ col2.

class NumMatrix(object):

    # 行之和 前缀数组
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        self.rows = []
        for row in matrix:
            acc = []
            curr_acc = 0
            for ele in row:
                curr_acc += ele
                acc.append(curr_acc)
            self.rows.append(acc)

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: None
        """
        target_row = self.rows[row]
        dif = val - self.matrix[row][col]
        self.matrix[row][col] = val
        for i in range(col, len(self.rows[row])):
            target_row[i] += dif

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if col1 != 0:
            return sum([self.rows[i][col2] - self.rows[i][col1 - 1] for i in range(row1, row2 + 1)])
        else:
            return sum([self.rows[i][col2] for i in range(row1, row2 + 1)])


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)