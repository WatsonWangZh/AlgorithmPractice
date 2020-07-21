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
            return not word
        row, col = len(board), len(board[0])
        
        def dfs(start, word):
            if not word:
                return True
            r, c = start
            if 0 <= r <= row-1 and 0 <= c <= col-1 and board[r][c] == word[0]:
                tmp = board[r][c]
                board[r][c] = '#'
                res = dfs([r-1, c], word[1:]) or dfs([r+1, c], word[1:]) or dfs([r, c-1], word[1:]) or dfs([r, c+1], word[1:]) 
                board[r][c] = tmp
                return res
            else:
                return False
            
        
        for i in range(row):
            for j in range(col):
                res = dfs([i, j], word)
                if res:
                    return True
        return False
