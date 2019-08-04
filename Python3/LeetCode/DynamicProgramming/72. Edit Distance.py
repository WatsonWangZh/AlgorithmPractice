# Given two words word1 and word2, find the minimum number 
# of operations required to convert word1 to word2.
# You have the following 3 operations permitted on a word:
# Insert a character
# Delete a character
# Replace a character

# Example 1:
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')

# Example 2:
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # 动态规划 O(n^2)
        # 经典的编辑距离问题。
        # 状态表示：f[i,j] 表示将 word1 的前 i 个字符变成 word2 的前 j 个字符，最少需要进行多少次操作。
        # 状态转移，一共有四种情况：
            # 将 word1[i] 删除或在 word2[j] 后面添加 word1[i]，则其操作次数等于 f[i−1,j]+1；
            # 将 word2[j] 删除或在 word1[i]word1[i] 后面添加 word2[j]，则其操作次数等于 f[i,j−1]+1；
            # 如果 word1[i] = word2[j]，则其操作次数等于 f[i−1,j−1]；
            # 如果 word1[i] ≠ word2[j]，则其操作次数等于 f[i−1,j−1]+1；
        # 时间复杂度分析：状态数 O(n^2)，状态转移复杂度是 O(1)，所以总时间复杂度是 O(n^2)。
        # 样例讲解: https://www.youtube.com/watch?v=We3YDTzNXEk
        lenth1 = len(word1) + 1
        lenth2 = len(word2) + 1
        matrix = [[0] * lenth2 for i in range(lenth1)]
        for i in range(1, lenth1):
            matrix[i][0] = matrix[i - 1][0] + 1
        for i in range(1, lenth2):
            matrix[0][i] = matrix[0][i - 1] + 1
        for i in range(1, lenth1):
            for j in range(1, lenth2):
                cost = 1
                if word1[i - 1] == word2[j - 1]:
                    cost = 0
                matrix[i][j] = min(matrix[i - 1][j] + 1, matrix[i][j - 1] + 1, matrix[i - 1][j - 1] + cost)
        return matrix[lenth1 - 1][lenth2 - 1]
        