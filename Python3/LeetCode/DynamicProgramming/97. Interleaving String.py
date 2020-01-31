# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

# Example 1:
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true

# Example 2:
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
            
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        # 动态规划 O(n^2)
        # 状态表示：f[i][j] 表示 s1 的前 i 个字符和 s2 的前 j 个字符是否可以交错组成 s3 的前 i+j 个字符。
        # 状态转移：
        # 如果 s3[i+j] 匹配 s1[i]，则问题就转化成了 f[i−1][j]；
        # 如果 s3[i+j] 匹配 s2[j]，则问题就转化成了 f[i][j−1]。
        # 两种情况只要有一种为真，则 f[i] 就为真。
        # 时间复杂度分析：状态总共有 n^2 个，状态转移复杂度是 O(1)。所以总时间复杂度是 O(n^2)。
                                                                    
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3:
            return False
        dp = [[False] * (l2 + 1) for _ in range(l1 + 1)]
        for i in range(l1 + 1):
            for j in range(l2 + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j-1] and (s2[j-1] == s3[j-1])
                elif j == 0:
                    dp[i][j] = dp[i-1][j] and (s1[i-1] == s3[i-1])
                else:
                    dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i + j - 1]) or (dp[i][j-1] and s2[j-1]== s3[i+j-1])
        return dp[l1][l2]
 