# The n-queens puzzle is the problem of placing n queens on an n×n chessboard 
# such that no two queens attack each other.
# Given an integer n, return the number of distinct solutions to the n-queens puzzle.

# Example:
# Input: 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],

#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]

class Solution(object):
    # 思路与 51 N-Queens 一样，不过把原先用来最后拼装的参数之类都去掉了，换了一个计数器来记录数量。
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # 用三个数组来表示列、正反对角线的占用情况。一行行的遍历，如果没有冲突就把相应的位置置为占用，继续处理下一行，
        # 并记录改行的皇后放在了哪一列，当皇后都放完后，根据记录的列号来拼出结果。进行回溯时要把占用的位置还回去。
        # 对角线位置的计算要小心（尤其是反对角线），可以把顶点带进去计算验证一下。
        self.col = [False] * n
        # 对于对角线冲突，包含两种情况：
        # 主对角线冲突x-y相同；辅对角线冲突x+y相同。
        # x和y取值范围均为0-n，故x+y取值范围为0-2n；
        # x-y范围为-n-n → x-y+n范围为0-2n
        self.diag = [False] * (2 * n)
        self.anti_diag = [False] * (2 * n)
        self.result = 0
        self.recursive(0, n)
        return self.result

    def recursive(self, row, n):

        if row == n:
            self.result += 1
        else:
            for i in range(n):
                if not self.col[i] and not self.diag[row + i] and not self.anti_diag[n - i + row]:
                    self.col[i] = self.diag[row + i] = self.anti_diag[n - i + row] = True
                    self.recursive(row + 1, n)
                    self.col[i] = self.diag[row + i] = self.anti_diag[n - i + row] = False
