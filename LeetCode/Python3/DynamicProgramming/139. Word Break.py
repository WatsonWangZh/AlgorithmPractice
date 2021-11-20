# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
# determine if s can be segmented into a space-separated sequence of one or more dictionary words.
# Note:
# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.

# Example 1:
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".

# Example 2:
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#              Note that you are allowed to reuse a dictionary word.

# Example 3:
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # 采用动态规划的方法解决，dp[i]表示字符串s[:i]能否拆分成符合要求的子字符串。
        # 可以看出，如果s[j:i]在给定的字符串组中，且dp[j]为True（即字符串s[:j]能够拆分成符合要求的子字符串），
        # 那么此时dp[i]也就为True了。按照这种递推关系，我们就可以判断目标字符串能否成功拆分。

        n = len(s)
        dp = [False for i in range(n+1)]
        dp[0] = True
        for i in range(n):
            if dp[i]:
                for j in wordDict:
                    l = len(j)
                    if i+l <= n and s[i:i+l] == j:
                        dp[i+l] = True
        return dp[n]
