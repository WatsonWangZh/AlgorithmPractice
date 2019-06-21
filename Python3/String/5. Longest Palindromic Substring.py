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
        # if len(s) < 2 or s == s[::-1]:
        #     return s
        
        # 1.中心扩散法
        # n = len(s)
        # start,maxlen=0,1
        # for i in range(n):
        #     odd = s[i-maxlen-1:i+1]
        #     even = s[i-maxlen:i+1]
        #     if i - maxlen - 1 >= 0 and odd == odd[::-1]:
        #         start = i - maxlen - 1
        #         maxlen += 2
        #         continue
        #     if i - maxlen >= 0 and even == even[::-1]:
        #         start = i - maxlen
        #         maxlen += 1
        # return s[start:start+maxlen]
        
        # 2.DP方法
        # dp = [[False] * n] * n ：为浅拷贝，
        # 例子dp = [[False] * 2] * 2，dp[0][0]=True, dp = [[True, False], [True, False]]
        # n = len(s)
        # maxlen = 0
        # Wrong Point:
        # dp = [ [False] * n] * n
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

        if len(s)<2 or s == s[::-1]:
            return s
        lens=len(s)
        maxlen=0
        start=0
        # 长度为奇数
        for i in range(lens):
            j = i - 1
            k = i + 1
            while j >= 0 and k < lens and s[j] == s[k]:
                if k - j + 1 > maxlen:
                    maxlen = k - j + 1
                    start = j
                j -= 1
                k += 1
        # 长度为偶数
        for i in range(lens):
            j = i
            k = i + 1
            while j >= 0 and k < lens and s[j] == s[k]:
                if k - j + 1 > maxlen:
                    maxlen = k - j + 1
                    start = j
                j -= 1
                k += 1

        if maxlen>0:
            return s[start:start+maxlen]
        return s[0]

def main():
    s = Solution()
    print(s.longestPalindrome("babad"))
    print(s.longestPalindrome("cbbd"))

if __name__ == "__main__":
    main()