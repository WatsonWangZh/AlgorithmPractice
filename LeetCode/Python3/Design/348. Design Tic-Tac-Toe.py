# Design a Tic-tac-toe game that is played between two players on a n x n grid.
# You may assume the following rules:
# A move is guaranteed to be valid and is placed on an empty block.
# Once a winning condition is reached, no more moves is allowed.
# A player who succeeds in 
# placing n of their marks in a horizontal, vertical, or diagonal row wins the game.

# Example:
# Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.
# TicTacToe toe = new TicTacToe(3);

# toe.move(0, 0, 1); -> Returns 0 (no one wins)
# |X| | |
# | | | |    // Player 1 makes a move at (0, 0).
# | | | |

# toe.move(0, 2, 2); -> Returns 0 (no one wins)
# |X| |O|
# | | | |    // Player 2 makes a move at (0, 2).
# | | | |

# toe.move(2, 2, 1); -> Returns 0 (no one wins)
# |X| |O|
# | | | |    // Player 1 makes a move at (2, 2).
# | | |X|

# toe.move(1, 1, 2); -> Returns 0 (no one wins)
# |X| |O|
# | |O| |    // Player 2 makes a move at (1, 1).
# | | |X|

# toe.move(2, 0, 1); -> Returns 0 (no one wins)
# |X| |O|
# | |O| |    // Player 1 makes a move at (2, 0).
# |X| |X|

# toe.move(1, 0, 2); -> Returns 0 (no one wins)
# |X| |O|
# |O|O| |    // Player 2 makes a move at (1, 0).
# |X| |X|

# toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
# |X| |O|
# |O|O| |    // Player 1 makes a move at (2, 1).
# |X|X|X|

# Follow up:
# Could you do better than O(n^2) per move() operation?

# Hints:
# Could you trade extra space such that move() operation can be done in O(1)?
# You need two arrays: int rows[n], int cols[n], plus two variables: diagonal, anti_diagonal.

# M1. 直观想法
# 构造n*n的网格, 每次下棋时, 检查棋子所在的行/ 列 /对角线是否连成一条线. 
# 检查的条件是计算行/ 列 /对角线棋子标记的个数是否等于n.

# class TicTacToe(object):

#     def __init__(self, n):
#         """
#         Initialize your data structure here.
#         :type n: int
#         """
#         self.grid = [[""] * n for i in range(n)]

#     def move(self, row, col, player):
#         """
#         Player {player} makes a move at ({row}, {col}).
#         @param row The row of the board.
#         @param col The column of the board.
#         @param player The player, can be either 1 or 2.
#         @return The current winning condition, can be either:
#                 0: No one wins.
#                 1: Player 1 wins.
#                 2: Player 2 wins.
#         :type row: int
#         :type col: int
#         :type player: int
#         :rtype: int
#         """
#         if player == 1:
#             mark = 'X'
#         else:
#             mark = 'O'
            
#         self.grid[row][col] = mark
#         # check wining condition
#         # check if the row has the same mark
#         n = len(self.grid)
#         sum_of_row = sum([self.grid[row][c] == mark for c in range(n)])
#         sum_of_col = sum([self.grid[r][col]== mark for r in range(n)])
#         sum_of_left_d = sum([self.grid[i][i] == mark for i in range(n)])
#         sum_of_right_d = sum([self.grid[i][n-1-i] == mark for i in range(n)])
#         if sum_of_row == n or sum_of_col == n or sum_of_left_d== n or sum_of_right_d == n:
#             return player        
#         else:
#             return 0

# M2. Follow Up Case
# Follow up中让我们用更高效的方法，那么根据提示，
# 我们建立一个大小为n的一维数组rows和cols，还有变量对角线diag和逆对角线rev_diag，
# 这种方法的思路是，如果玩家1在第一行某一列放了一个子，那么rows[0]自增1，
# 如果玩家2在第一行某一列放了一个子，则rows[0]自减1，
# 那么只有当rows[0]等于n或者-n的时候，表示第一行的子都是一个玩家放的，
# 则游戏结束返回该玩家即可，其他各行各列，对角线和逆对角线都是这种思路。

class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.rows = [0]*n
        self.columns = [0]*n
        self.diagonal = 0
        self.antidiagonal = 0

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        toAdd = 1 if player == 1 else -1
        self.rows[row] += toAdd
        self.columns[col] += toAdd
        
        if row == col: 
            self.diagonal += toAdd
        if (row + col) == (len(self.rows) - 1):
            self.antidiagonal += toAdd
        
        n = len(self.rows)
        if abs(self.rows[row]) == n or abs(self.columns[col]) == n \
            or abs(self.diagonal) == n or abs(self.antidiagonal) == n:
                return player

        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)