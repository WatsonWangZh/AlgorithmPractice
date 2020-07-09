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
        if not p:
            return not s

        first_match = bool(s) and p[0] in {s[0], '.'}

        if len(p) >= 2 and p[1] == '*':
            return (self.isMatch(s, p[2:]) or
                    first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])

        # M2. DP O(nm)
        n, m = len(s), len(p)
        s, p = ' ' + s, ' ' + p
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True
        
        for i in range(n+1):
            for j in range(1, m+1):

                if j + 1 <= m and p[j + 1] == '*':
                    continue

                if i>0 and p[j] != '*':
                    dp[i][j] = dp[i-1][j-1] and (s[i] == p[j] or p[j] == '.')
                    
                elif p[j] == '*':
                    dp[i][j] = dp[i][j-2] or i != 0 and dp[i-1][j] and (s[i] == p[j - 1] or p[j-1] == '.')

        return dp[n][m]
