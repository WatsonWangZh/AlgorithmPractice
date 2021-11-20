# On an 8 x 8 chessboard, there is one white rook.  
# There also may be empty squares, white bishops, and black pawns.  
# These are given as characters 'R', '.', 'B', and 'p' respectively. 
# Uppercase characters represent white pieces, and lowercase characters represent black pieces.

# The rook moves as in the rules of Chess: 
# it chooses one of four cardinal directions (north, east, west, and south), 
# then moves in that direction until it chooses to stop, reaches the edge of the board, 
# or captures an opposite colored pawn by moving to the same square it occupies.  
# Also, rooks cannot move into the same square as other friendly bishops.

# Return the number of pawns the rook can capture in one move.

# Example 1:
# Input: 
# [
#   [".",".",".",".",".",".",".","."],
#   [".",".",".","p",".",".",".","."],
#   [".",".",".","R",".",".",".","p"],
#   [".",".",".",".",".",".",".","."],
#   [".",".",".",".",".",".",".","."],
#   [".",".",".","p",".",".",".","."],
#   [".",".",".",".",".",".",".","."],
#   [".",".",".",".",".",".",".","."]
# ]
# Output: 3
# Explanation: 
# In this example the rook is able to capture all the pawns.

# Example 2:
# Input: 
# [
#   [".",".",".",".",".",".",".","."],
#   [".","p","p","p","p","p",".","."],
#   [".","p","p","B","p","p",".","."],
#   [".","p","B","R","B","p",".","."],
#   [".","p","p","B","p","p",".","."],
#   [".","p","p","p","p","p",".","."],
#   [".",".",".",".",".",".",".","."],
#   [".",".",".",".",".",".",".","."]
# ]
# Output: 0
# Explanation: 
# Bishops are blocking the rook to capture any pawn.

# Example 3:
# Input: 
# [
#   [".",".",".",".",".",".",".","."],
#   [".",".",".","p",".",".",".","."],
#   [".",".",".","p",".",".",".","."],
#   ["p","p",".","R",".","p","B","."],
#   [".",".",".",".",".",".",".","."],
#   [".",".",".","B",".",".",".","."],
#   [".",".",".","p",".",".",".","."],
#   [".",".",".",".",".",".",".","."]
# ]
# Output: 3
# Explanation: 
# The rook can capture the pawns at positions b5, d6 and f5.

# Note:
# board.length == board[i].length == 8
# board[i][j] is either 'R', '.', 'B', or 'p'
# There is exactly one cell with board[i][j] == 'R'

class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        # 暴力枚举 O(n)
        # 首先找到车的位置，然后分别向四个方向枚举即可
        # 时间复杂度
            # 每个方向最多需要遍历一行或一列，故时间复杂度为O(n)。
        # 空间复杂度
            # 仅需要常数的额外空间。

        # 找到rook位置
        rook = [-1,-1]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'R':
                    rook = [i,j]
        # 四个方向依次分析
        res = 0
        for directions in [[0,-1], [-1,0], [0,1], [1,0]]:
            x, y = directions
            i,j = rook
            while 0<=i<8 and 0<=j<8 and board[i][j] in 'R.':
                i += x; j += y
            # 如果是碰到障碍物，判断障碍物是否为地方小兵
            if 0<=i<8 and 0<=j<8 and board[i][j] == 'p':
                res += 1
        return res
