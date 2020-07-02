# Given a 2D board and a list of words from the dictionary, find all words in the board.
# Each word must be constructed from letters of sequentially adjacent cell, 
# where "adjacent" cells are those horizontally or vertically neighboring. 
# The same letter cell may not be used more than once in a word.

# Example:
# Input: 
# board = [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
 
# Note:
# All inputs are consist of lowercase letters a-z.
# The values of words are distinct.

# Hints:
# You would need to optimize your backtracking to pass the larger test. 
# Could you stop backtracking earlier?
# If the current candidate does not exist in all words' prefix, 
# you could stop backtracking immediately. 
# What kind of data structure could answer such query efficiently? 
# Does a hash table work? Why or why not? How about a Trie? 
# If you would like to learn how to implement a basic trie, 
# please work on this problem: Implement Trie (Prefix Tree) first.

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # M1. 普通DFS Time Limit Exceeded
        rows, cols = len(board), len(board[0])
        res = set()
        
        def dfs(start, word):
            if not word: 
                return True
            n, m = start[0], start[1]
            # 枚举单词的起点
            if 0<= n <= rows-1 and 0 <= m <= cols-1 and board[n][m] == word[0]:
                temp = board[n][m]
                board[n][m] = '#'
                res = dfs([n, m+1], word[1:]) or dfs([n, m-1], word[1:]) or dfs([n+1, m], word[1:]) or dfs([n-1, m], word[1:])
                # 遍历完恢复
                board[n][m] = temp
                return res
            else:
                return False
            
        for word in words:
            for i in range(rows):
                for j in range(cols):
                    flag = dfs([i,j], word)
                    if flag:
                        res.add(word)
        return res


        # M2. 递归回溯 + Trie 优化 Accepted
        rows, cols = len(board), len(board[0])
        res = set()

        # 建立 Trie树
        root = {}
        for word in words:
            tmp = root
            for ch in word:
                if ch not in tmp:
                    tmp[ch] = {}
                tmp = tmp[ch]
            tmp['#'] = word
            
        
        def dfs(start, trie):

            i, j = start[0], start[1]
            char = board[i][j]
            if char not in trie:
                return

            board[i][j] = '#'
            trie = trie[char]

            if '#' in trie:
                res.add(trie.pop('#'))

            if i > 0 and board[i-1][j] != '#':
                dfs([i-1, j], trie)
            if j > 0 and board[i][j-1] != '#':
                dfs([i, j-1], trie)
            if i < (rows-1) and board[i+1][j] != '#':
                dfs([i+1, j], trie)
            if j < (cols-1) and board[i][j+1] != '#':
                dfs([i, j+1], trie)

            board[i][j] = char
               
        for i in range(rows):
            for j in range(cols):
                dfs([i,j], root)

        return res