# Write a program to solve a Sudoku puzzle by filling the empty cells.
# A sudoku solution must satisfy all of the following rules:
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# Empty cells are indicated by the character '.'.

# _____________________________________
# |_5_|_3_|___|___|_7_|___|___|___|___|
# |_6_|___|___|_1_|_9_|_5_|___|___|___|
# |___|_9_|_8_|___|___|___|___|_6_|___|
# |_8_|___|___|___|_6_|___|___|___|_3_|
# |_4_|___|___|_8_|___|_3_|___|___|_1_|
# |_7_|___|___|___|_2_|___|___|___|_6_|
# |___|_6_|___|___|___|___|_2_|_8_|___|
# |___|___|___|_4_|_1_|_9_|___|___|_5_|
# |___|___|___|___|_8_|___|___|_7_|_9_|
# A sudoku puzzle...
# _____________________________________
# |_5_|_3_|_4_|_6_|_7_|_8_|_9_|_1_|_2_|
# |_6_|_7_|_2_|_1_|_9_|_5_|_3_|_4_|_8_|
# |_1_|_9_|_8_|_3_|_4_|_2_|_5_|_6_|_7_|
# |_8_|_5_|_9_|_7_|_6_|_1_|_4_|_2_|_3_|
# |_4_|_2_|_6_|_8_|_5_|_3_|_7_|_9_|_1_|
# |_7_|_1_|_3_|_9_|_2_|_4_|_8_|_5_|_6_|
# |_9_|_6_|_1_|_5_|_3_|_7_|_2_|_8_|_4_|
# |_2_|_8_|_7_|_4_|_1_|_9_|_6_|_3_|_5_|
# |_3_|_4_|_5_|_2_|_8_|_6_|_1_|_7_|_9_|
# ...and its solution.

# Note:
# The given board contain only digits 1-9 and the character '.'.
# You may assume that the given Sudoku puzzle will have a single unique solution.
# The given board size is always 9x9.

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # 思想
        # 停止填充条件为，board中所有元素都不是”.” - findEmpty()。
        # 遍历填充数字1-9，检查行冲突、列冲突和 3×3 冲突。checkRow、checkCol和checkCube。
        self.board = board
        self.solve()

    def findEmpty(self):
        for r in range(len(self.board)):
            for c in range(len(self.board[0])):
                if self.board[r][c] == '.':
                    return r, c
        return -1, -1

    def solve(self):
        r, c = self.findEmpty()
        if r == -1:    # r==-1 and c==-1
            return True
        for num in '123456789':
            if self.checkRow(num, r) and self.checkCol(num, c) and self.checkCube(num, r, c):
                self.board[r][c] = num
                if self.solve():
                    return True
                self.board[r][c] = '.'

    def checkRow(self, num, r):
        return num not in self.board[r]

    def checkCol(self, num, c):
        for r in range(9):
            if self.board[r][c] == num:
                return False
        return True

    def checkCube(self, num, r, c):
        # minRow：r//3 * 3
        r = r // 3 * 3
        c = c // 3 * 3
        for i in range(r, r+3):
            for j in range(c, c+3):
                if self.board[i][j] == num:
                    return False
        return True
