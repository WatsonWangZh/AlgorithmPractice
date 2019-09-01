# Given an input string (s) and a pattern (p), 
# implement regular expression matching with support for '.' and '*'.
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).
# Note:
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like . or *.

# Example 1:
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".

# Example 2:
# Input:
# s = "aa"
# p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. 
# Therefore, by repeating 'a' once, it becomes "aa".

# Example 3:
# Input:
# s = "ab"
# p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".

# Example 4:
# Input:
# s = "aab"
# p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. 
# Therefore, it matches "aab".

# Example 5:
# Input:
# s = "mississippi"
# p = "mis*is*p*."
# Output: false
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # M1.递归 
        # if not s and not p:
        #     return True
        # if not p and s:
        #     return False

        # # 首先判断第2位是不是*
        # if len(p) > 1 and p[1] == '*':
        #     if self.isMatch(s, p[2:]):    # 重复0次
        #         return True
        #     if s and (p[0] == '.' or p[0] == s[0]):    # 第一位已经匹配, 重复多次/1次
        #         return self.isMatch(s[1:], p)


        # if s and (p[0] == '.' or p[0] == s[0]):
        #     return self.isMatch(s[1:], p[1:])

        # return False


        # 动态规划 O(nm)
        # 设状态 f(i,j) 表示字符串 s 的前 i 个字符和字符串 p 的前 j 个字符能否匹配。这里假设 s 和 p 的下标均从 1 开始。
        # 初始时，f(0,0) = true。
        # 平凡转移 f(i,j) = f(i,j) or f(i−1,j−1)，当 i> 0 且 s(i) == p(j) || p(j) == '.'。
            # 当 p(j) == '*' 时，此时 f(i,j) 可以从 f(i,j−2) 转移，表示丢弃这一次的 '*' 和它之前的那个字符。
            # 此时若 i > 0 且 s(i) == p(j - 1)，表示这个字符可以利用这个 '*'，则一方面可以从 f(i−1,j−2) 转移，表示利用 '*' 一次；
            # 另一方面也可以从 f(i−1,j) 转移，表示两次或者多次利用 '*'。这里的转移即取 or 操作。
        # 初始状态 f(0,0)=true；循环枚举 i 从 0 到 n；j 从 1 到 m。
        # 最终答案为 f(n,m)。
        
        # 时间复杂度
        # 状态数为 O(nm)，每次转移仅需常数时间，故总时间复杂度为 O(nm)。

        # M2. DP Top-Down Variation
        # memo = {}
        # def dp(i, j):
        #     if (i, j) not in memo:
        #         # check if we've reached end of patterns
        #         # it's a match if we've also reached end of string
        #         if j == len(p):
        #             memo[i,j] = i == len(s)
        #         else:
        #             # test if first char matches or is wild char
        #             first_match = i < len(s) and p[j] in {s[i],'.'}
        #             # next char is an asterisk
        #             if j+1 < len(p) and p[j+1] == "*":
        #                 # 2 outcomes:
        #                 # string repeats next char, so we increment i
        #                 # string doesn't repeat next char, so we increment j by 2
        #                 memo[i, j] = (first_match and dp(i+1, j)) or dp(i, j+2)
        #             else:
        #                 # if the first char matched, we increment both i and j
        #                 memo[i,j] = first_match and dp[i+1, j+1]
        #     return memo[i, j]

        # return dp[0, 0]

        # M3. DP Bottom-Up Variation
        dp = [[False for i in range(len(p)+1)] for j in range(len(s)+1)]   # dp[i][j] - s[:i] and p[:j]
        dp[0][0] = True
        
        # Base cases for comparing against empty string
        for i in range(1, len(p)+1):
            if p[i-1] == '*':
                if i >= 2:
                    dp[0][i] = dp[0][i-2]

        # fill out 2d array with recurrance relation
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    # 0 times/1 times/multiple times
                    dp[i][j] = dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.'))
                else:
                    # zero times
                    dp[i][j] = dp[i-1][j-1] and s[i-1] == p[j-1]

        return dp[len(s)][len(p)]
