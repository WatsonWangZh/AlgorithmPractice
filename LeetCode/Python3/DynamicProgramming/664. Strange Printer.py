# There is a strange printer with the following two special requirements:
# The printer can only print a sequence of the same character each time.
# At each turn, the printer can print new characters starting from and ending at any places, 
# and will cover the original existing characters.
# Given a string consists of lower English letters only, 
# your job is to count the minimum number of turns the printer needed in order to print it.

# Example 1:
# Input: "aaabbb"
# Output: 2
# Explanation: Print "aaa" first and then print "bbb".

# Example 2:
# Input: "aba"
# Output: 2
# Explanation: Print "aaa" first and then print "b" from the second place of the string, 
# which will cover the existing character 'a'.

# Hints:
# Length of the given string will not exceed 100.

class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 动态规划 O(n^3)
        # -状态表示：dp[i][j]表示s[i:j]最少需要打印多少次。
        # -状态初始化：dp[i][i] = 1,其余初始化为0。
        # -状态转移：首先考虑初始化将dp[i][j] = dp[i][i] + dp[i + 1][j]，代表s[i]单独打印。
        # 考虑所有的i < k < j，将区间s[i:j]拆分成s[i:k]和s[k + 1:j]两个部分。
        # 如果s[i] == s[k]，说明区间s[k]可以和s[i]同时打印，所以s[i][k] = s[i][k - 1]，
        # 那么dp[i][j] = min(dp[i][j],dp[i][k - 1] + dp[k + 1][j])。
        # 最后考虑如果s[i] = s[j]，说明s[j]可以和s[i]一起打印，
        # 那么dp[i][j] = min(dp[i][j],dp[i + 1][j])
        # 最后结果为dp[0][n - 1]

        if not s:
            return 0
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for length in range(1, n):
            for i in range(n-length):
                j = i + length
                dp[i][j] = 1 + dp[i+1][j]
                
                for k in range(i+1, j):
                    if s[i] == s[k]:
                        dp[i][j] = min(dp[i][j], dp[i][k-1] + dp[k+1][j])

                if s[i] == s[j]:
                    dp[i][j] = min(dp[i][j], dp[i+1][j])
                    
        return dp[0][n-1]