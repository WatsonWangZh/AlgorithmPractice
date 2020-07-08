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
        # M1. 中心扩散法 O(n^2)
        res = ""
        for i in range(len(s)):

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
        
        # M2. DP 

        n = len(s)
        maxlen = 0
        dp = [[False for _ in range(n)] for _ in range(n)]

        res = ""
        for end in range(n):
            for start in range(end+1):
                dp[start][end] = s[start] == s[end] and ((end - start <= 2) or dp[start+1][end-1])
                if dp[start][end]:
                    if end - start + 1 > maxlen:
                        maxlen = end - start + 1
                        res = s[start:end+1]             
        return res


        # M3, Manacher's Algorithm, non-trivial algorithm. 
        s = "#".join("^{}$".format(s))
        res = ""

        for center in range(len(s)):
            r = 1
            while 0 <= center - r and center + r <= len(s) - 1:                
                if s[center - r] != s[center + r] : break
                if len(res) < 2 * r + 1:
                    res = s[center - r : center + r + 1]
                r += 1

        return res.replace("#", "")
