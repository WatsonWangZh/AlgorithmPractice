# Given a string s, find the longest palindromic substring in s. 
# You may assume that the maximum length of s is 1000.

# Example 1:
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Example 2:
# Input: "cbbd"
# Output: "bb"

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 暴力枚举 O(n^2)
        # 由于字符串长度小于1000，因此我们可以用 O(n^2) 的算法枚举所有可能的情况。
        # 首先枚举回文串的中心 i，然后分两种情况向两边扩展边界，直到遇到不同字符为止:
            # 回文串长度是奇数，则依次判断 s[i−k]==s[i+k],k=1,2,3,…s[i−k]==s[i+k],k=1,2,3,…
            # 回文串长度是偶数，则依次判断 s[i−k]==s[i+k−1],k=1,2,3,…s[i−k]==s[i+k−1],k=1,2,3,…
        # 如果遇到不同字符，则我们就找到了以 i 为中心的回文串边界。
        # 时间复杂度分析：一共两重循环，所以时间复杂度是 O(n^2)。

        # M1. 暴力枚举 中心扩散法
        n = len(s)
        res = ""
        for i in range(0, n):
            temp_odd = str(s[i])
            k = 1
            while (i-k) >= 0 and (i+k) < n and s[i-k] == s[i+k]:
                temp_odd = str(s[i-k]) + temp_odd + str(s[i+k])
                k += 1
            temp_even = ''
            k = 1
            while (i-k) >= 0 and (i+k-1) < n and s[i-k] == s[i+k-1]:
                temp_even = str(s[i-k]) + temp_even + str(s[i+k-1])
                k += 1
            temp = temp_odd if (len(temp_odd) > len(temp_even)) else temp_even
            res = temp if (len(temp) > len(res)) else res
        return res
        
        # M2. DP方法
        # dp = [[False] * n] * n ：为浅拷贝，
        # 例子dp = [[False] * 2] * 2，dp[0][0]=True, dp = [[True, False], [True, False]]
        # Wrong Point:
        # dp = [ [False] * n] * n

        # n = len(s)
        # maxlen = 0
        # dp = [[False for _ in range(n)] for _ in range(n)]
        # res = ""
        # for end in range(n):
        #     for start in range(end+1):
        #         dp[start][end] = s[start] == s[end] and ((end - start <= 2) or dp[start+1][end-1])
        #         if dp[start][end]:
        #             if end - start + 1 > maxlen:
        #                 maxlen = end - start + 1
        #                 res = s[start:end+1]             
        # return res
