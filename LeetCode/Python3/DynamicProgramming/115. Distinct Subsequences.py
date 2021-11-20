# Given a string S and a string T, count the number of distinct subsequences of S which equals T.
# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing 
# the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

# Example 1:
# Input: S = "rabbbit", T = "rabbit"
# Output: 3
# Explanation:
# As shown below, there are 3 ways you can generate "rabbit" from S.
# (The caret symbol ^ means the chosen letters)
# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^

# Example 2:
# Input: S = "babgbag", T = "bag"
# Output: 5
# Explanation:
# As shown below, there are 5 ways you can generate "bag" from S.
# (The caret symbol ^ means the chosen letters)
# babgbag
# ^^ ^
# babgbag
# ^^    ^
# babgbag
# ^    ^^
# babgbag
#   ^  ^^
# babgbag
#     ^^^

class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # 动态规划 O(nm)
        # 可以换一种考虑问题的方式：用 S 中的字符，按顺序匹配 T 中的字符，问有多少种方式可以匹配完 T 中的所有字符。
        # 可以用动态规划来做：
        # f[i][j] 表示用 S 的前 i 个字符，能匹配完 T 的前 j 个字符的方案数。
        # 初始化：因为 S 可以从任意一个字符开始匹配，所以 f[i][0]=1,∀i∈[0,len(S)]。
        # 状态转移：
        # 如果 S[i−1]≠T[j−1]，则 S[i−1] 不能匹配 T[j−1]，所以 f[i][j]=f[i−1][j]；
        # 如果 S[i−1]=T[j−1]，则 S[i−1] 既可以匹配 T[j−1]，也可以不匹配 T[j−1]，所以 f[i][j]=f[i−1][j]+f[i−1][j−1]；
        # 时间复杂度分析：假设 S 的长度是 n，T 的长度是 m，则共有 nm 个状态，状态转移的复杂度是 O(1)，所以总时间复杂度是 O(nm)。

        ns = len(s)
        nt = len(t)
        dp = [[0 for i in range(nt+1)] for j in range(ns+1)]
        for i in range(0,ns+1):
            dp[i][0] = 1
        for i in range(1,ns+1):
            for j in range(1,nt+1):
                dp[i][j] = dp[i-1][j]
                if s[i-1] == t[j-1]:
                    dp[i][j] += dp[i-1][j-1]

        return dp[ns][nt]
