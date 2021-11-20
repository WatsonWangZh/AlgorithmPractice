# A message containing letters from A-Z is being encoded to numbers using the following mapping:
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given a non-empty string containing only digits, determine the total number of ways to decode it.

# Example 1:
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).

# Example 2:
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # DP O(n)
        # 状态表示：dp[i] 表示前 i 个数字共有多少种解码方式。
        # 初始化：0个数字解码的方案数1，即 dp[0]=1。
        # 状态转移：dp[i] 可以表示成如下两部分的和：
        # 如果第 i 个数字不是0，则 i 个数字可以单独解码成一个字母，此时的方案数等于用前 i−1 个数字解码的方案数，即 dp[i−1]；
        # 如果第 i−1个数字和第 i 个数字组成的两位数在 10 到 26 之间，
        # 则可以将这两位数字解码成一个字符，此时的方案数等于用前 i−2 个数字解码的方案数，即 dp[i−2]；
        # 时间复杂度分析：
        # 状态数是 n 个，状态转移的时间复杂度是 O(1)，所以总时间复杂度是 O(n)。

        if not s:
            return 0

        dp = [0 for i in range(len(s)+1)]
        dp[0] = 1

        for i in range(1, len(s)+1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]   #one step per time 
            if i != 1 and s[i-2:i] > '09' and s[i-2:i] < '27':
                dp[i] += dp[i-2]   #two step per time with some condition
                
        return dp[len(s)]
