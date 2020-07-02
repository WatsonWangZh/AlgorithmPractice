# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
# add spaces in s to construct a sentence where each word is a valid dictionary word. 
# Return all such possible sentences.
# Note:
# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.

# Example 1:
# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
#   "cats and dog",
#   "cat sand dog"
# ]

# Example 2:
# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.

# Example 3:
# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []

class Solution(object):

    # M1. DFS 
    # 定义一个函数check - DP判断子字符串是否可以由wordDict中的词汇组成；
    # def wordBreak(self, s, wordDict):
    #     """
    #     :type s: str
    #     :type wordDict: List[str]
    #     :rtype: List[str]
    #     """
    #     wordDict = set(wordDict)
    #     res = []
    #     self.dfs(s, wordDict, 0, '', res)
    #     return res

    # def check(self, s, wordDict):
    #     n = len(s)
    #     dp = [False] * (n + 1)    # s[:i]
    #     dp[0] = True
    #     for i in range(1, n+1):
    #         for j in range(i-1, -1, -1):
    #             if dp[j] and s[j:i] in wordDict:
    #                 dp[i] = True
    #                 break
    #     return dp[-1]

    # def dfs(self, s, wordDict, i, temp, res):
    #     if i == len(s):
    #         # 越过结尾空格
    #         res.append(temp[:-1])
    #     if self.check(s[i:], wordDict):
    #         for j in range(i+1, len(s)+1):
    #             if s[i:j] in wordDict:
    #                 self.dfs(s, wordDict, j, temp + s[i:j] + ' ', res)

    # M1改进. dp已经统计了截止当前位置的字符串是否可以由wordDict中的词汇组成。
    # def wordBreak(self, s, wordDict):
    #     """
    #     :type s: str
    #     :type wordDict: List[str]
    #     :rtype: List[str]
    #     """
    #     wordDict = set(wordDict)
    #     dp = self.check(s, wordDict)
    #     res = []
    #     self.dfs(s, wordDict, dp, '', res)
    #     return res

    # def check(self, s, wordDict):
    #     n = len(s)
    #     dp = [False] * (n+1)
    #     dp[0] = True
    #     for i in range(1, n+1):
    #         for j in range(i-1, -1, -1):
    #             if dp[j] and s[j:i] in wordDict:
    #                 dp[i] = True
    #                 break
    #     return dp

    # def dfs(self, s, wordDict, dp, temp, res):
    #     if not s:
    #         res.append(temp[:-1])
    #     for i in range(len(s)):
    #         if dp[i] and s[i:] in wordDict:
    #             self.dfs(s[:i], wordDict, dp, s[i:] + ' ' + temp, res)

    # M2. 带记忆DP 存储截止s[:i], 满足题意的所有可能组合
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordDict = set(wordDict)
        n = len(s)
        dp = [[] for _ in range(n+1)]    # 截止s[:i], 满足题意的所有可能组合
        dp[0] = ['']

        if self.check(s, wordDict):
            for i in range(1, n+1):
                temp = []
                for j in range(i):
                    if dp[j] and s[j:i] in wordDict:
                        for prev in dp[j]:
                            space = ' ' if prev else ''
                            temp.append(prev + space + s[j:i])
                dp[i] = temp
        return dp[-1]

    def check(self, s, wordDict):
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for i in range(1, n+1):
            for j in range(i-1, -1, -1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]
