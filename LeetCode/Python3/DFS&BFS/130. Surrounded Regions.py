# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# Example:
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:
# X X X X
# X X X X
# X X X X
# X O X X
# Explanation:
# Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. 
# Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. 
# Two cells are connected if they are adjacent cells connected horizontally or vertically.

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # BFS + 逆向
        # 直接查找出所有应该变化的O的位置比较困难，逆向考虑，从边界入手，找出所有不发生变化的O的位置
        # 剩余的O位置即为需要变化的位置，进行对应变化即可

        if not board or not board[0]:
            return
        rows, cols = len(board), len(board[0])
        for row in range(rows):
            if row == 0 or row == rows - 1:
                for col in range(cols):
                    if board[row][col] == 'O':
                        self.helper(row, col, board)
            else:
                for col in [0, cols - 1]:
                    if board[row][col] == 'O':
                        self.helper(row, col, board)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                if board[row][col] == 'T':
                    board[row][col] = 'O'

    def helper(self, row, col, board):
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            return
        
        if board[row][col] == 'O':
            board[row][col] = 'T'
            self.helper(row+1, col, board)
            self.helper(row-1, col, board)
            self.helper(row, col+1, board)
            self.helper(row, col-1, board)