# Given a 2D board and a word, find if the word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cell, 
# where "adjacent" cells are those horizontally or vertically neighboring. 
# The same letter cell may not be used more than once.

# Example:
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # DFS O(n^2*3^k)
        # 在深度优先搜索中，最重要的就是考虑好搜索顺序。
        # 我们先枚举单词的起点，然后依次枚举单词的每个字母。
        # 过程中需要将已经使用过的字母改成一个特殊字母，以避免重复使用字符。
        # 时间复杂度分析：单词起点一共有 n^2 个，单词的每个字母一共有上下左右四个方向可以选择，
        # 但由于不能走回头路，所以除了单词首字母外，仅有三种选择。所以总时间复杂度是 O(n^2*3^k)。

        if not board: 
            return False
        if not word: 
            return True
        directions = [[-1,0],[1,0],[0,1],[0,-1]]

        row = len(board)
        col = len(board[0])

        def dfs(start, word):
            if not word: 
                return True
            n, m = start[0], start[1]
            # 枚举单词的起点
            if 0<= n <= row-1 and 0 <= m <= col-1 and board[n][m] == word[0]:
                temp = board[n][m]
                board[n][m] = '#'
                res = dfs([n, m+1], word[1:]) or dfs([n, m-1], word[1:]) or dfs([n+1, m], word[1:]) or dfs([n-1, m], word[1:])
                # 遍历完了进行恢复
                board[n][m] = temp
                return res
            else:
                return False

        for i in range(row):
            for j in range(col):
                res = dfs([i,j], word)
                if res:
                    return True
        return False
