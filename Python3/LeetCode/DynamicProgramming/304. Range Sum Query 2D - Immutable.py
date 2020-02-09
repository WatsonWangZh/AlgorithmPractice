# Given a 2D matrix matrix, 
# find the sum of the elements inside the rectangle 
# defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

# Example:
# Given matrix = [
#   [3, 0, 1, 4, 2],
#   [5, 6, 3, 2, 1],
#   [1, 2, 0, 1, 5],
#   [4, 1, 0, 1, 7],
#   [1, 0, 3, 0, 5]
# ]
# sumRegion(2, 1, 4, 3) -> 8
# sumRegion(1, 1, 2, 2) -> 11
# sumRegion(1, 2, 2, 4) -> 12

# Note:
# You may assume that the matrix does not change.
# There are many calls to sumRegion function.
# You may assume that row1 ≤ row2 and col1 ≤ col2.

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]: return 
        rows, cols = len(matrix), len(matrix[0])
        self.cumsum2d = [[0] * (cols + 1) for _ in range(rows+1)]
        for row in range(1, rows+1):
            for col in range(1, cols+1):
                self.cumsum2d[row][col] = self.cumsum2d[row][col-1] + self.cumsum2d[row-1][col] - self.cumsum2d[row-1][col-1] + matrix[row-1][col-1]


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.cumsum2d[row2+1][col2+1] - self.cumsum2d[row1][col2+1] - self.cumsum2d[row2+1][col1] + self.cumsum2d[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)