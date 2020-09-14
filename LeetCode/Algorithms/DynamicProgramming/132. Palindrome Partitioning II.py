# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return the minimum cuts needed for a palindrome partitioning of s.

# Example 1:
# Input: s = "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

# Example 2:
# Input: s = "a"
# Output: 0

# Example 3:
# Input: s = "ab"
# Output: 1
 
# Constraints:
# 1 <= s.length <= 2000
# s consists of lower-case English letters only.

class Solution:
    def minCut(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        s = " " + s
        g = [[False] * (n+1) for _ in range(n+1)]

        for j in range(1, n+1):
            for i in range(j+1):
                if i == j:
                    g[i][j] = True
                elif s[i] == s[j]:
                    if i + 1 > j - 1 or g[i+1][j-1]:
                        g[i][j] = True


        f = [float('inf')] * (n+1)
        f[0] = 0
        for i in range(1, n+1):
            for j in range(1, i+1):
                if g[j][i]:
                    f[i] = min(f[i], f[j-1] + 1)

        return f[n] - 1
