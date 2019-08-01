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
        # M1.递归 Time Limit Exceeded
        # if not s and not p:
        #     return True
        # if not p:
        #     return False
        # if len(p) > 1 and p[1] == "*":
        #     if s and (s[0] == p[0] or p[0] == "."):
        #         return self.isMatch(s, p[2:]) or self.isMatch(s[1:],p[2:]) or self.isMatch(s[1:], p)
        #     else:
        #         return self.isMatch(s, p[2:])
        # if s and (p[0] == "." or p[0] == s[0]):
        #     return self.isMatch(s[1:], p[1:])
        # return False

        # M2. 动态规划 
        # Top-Down Variation
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
        #             if j+1 < len(p) and p[j+1] =="*":
        #                 # 2 outcomes:
        #                 # string repeats next char, so we increment i
        #                 # string doesn't repeat next char, so we increment j by 2
        #                 memo[i, j] = (first_match and dp(i+1, j)) or dp(i, j+2)
        #             else:
        #                 # if the first char matched, we increment both i and j
        #                 memo[i,j] = first_match and dp[i+1, j+1]
        #     return memo[i, j]

        # return dp[0, 0]

        # M3. 动态规划 
        # Bottom-Up Variation
        dp=[[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        dp[0][0]=True
        # Base cases for comparing against empty string
        for i in range(1,len(p)+1):
            if p[i-1]=='*':
                if i>=2:
                    dp[0][i]=dp[0][i-2]
        # fill out 2d array with recurrance relation
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1]=='.':
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=='*':
                    dp[i][j]=dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=='.'))
                else:
                    dp[i][j]=dp[i-1][j-1] and s[i-1]==p[j-1]
        return dp[len(s)][len(p)]