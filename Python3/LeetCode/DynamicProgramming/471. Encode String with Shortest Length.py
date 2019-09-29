# Given a non-empty string, encode the string such that its encoded length is the shortest.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets 
# is being repeated exactly k times.
# Note:
# k will be a positive integer and encoded string will not be empty or have extra space.
# You may assume that the input string contains only lowercase English letters. 
# The string's length is at most 160.
# If an encoding process does not make the string shorter, then do not encode it. 
# If there are several solutions, return any of them is fine.

# Example 1:
# Input: "aaa"
# Output: "aaa"
# Explanation: There is no way to encode it such that it is shorter than the input string, 
# so we do not encode it.
 
# Example 2:
# Input: "aaaaa"
# Output: "5[a]"
# Explanation: "5[a]" is shorter than "aaaaa" by 1 character.
 
# Example 3:
# Input: "aaaaaaaaaa"
# Output: "10[a]"
# Explanation: "a9[a]" or "9[a]a" are also valid solutions, both of them have the same length = 5, which is the same as "10[a]".
 
# Example 4:
# Input: "aabcaabcd"
# Output: "2[aabc]d"
# Explanation: "aabc" occurs twice, so one answer can be "2[aabc]d".
 
# Example 5:
# Input: "abbbabbbcabbbabbbc"
# Output: "2[2[abbb]c]"
# Explanation: "abbbabbbc" occurs twice, but "abbbabbbc" can also be encoded to "2[abbb]c", 
# so one answer can be "2[2[abbb]c]".

class Solution(object):
    def encode(self, s):
        """
        :type s: str
        :rtype: str
        """
        # https://www.cnblogs.com/grandyang/p/6194403.html
        # 建立一个二维的DP数组，其中dp[i][j]表示s在[i, j]范围内的字符串的缩写形式
        # (如果缩写形式长度大于子字符串，那么还是保留子字符串)，
        # 那么如果s字符串的长度是n，最终我们需要的结果就保存在dp[0][n-1]中，
        # 然后我们需要遍历s的所有子字符串，对于任意一段子字符串[i, j]，
        # 我们以中间任意位置k来拆分成两段，比较dp[i][k]加上dp[k+1][j]的总长度和dp[i][j]的长度，
        # 将长度较小的字符串赋给dp[i][j]，然后我们要做的就是在s中取出[i, j]范围内的子字符串t进行合并。
        # 合并的方法是我们在取出的字符串t后面再加上一个t，然后在这里面寻找子字符串t的第二个起始位置，
        # 如果第二个起始位置小于t的长度的话，说明t包含重复字符串，
        # 举个例子吧，比如 t = "abab", 那么t+t = "abababab"，我们在里面找第二个t出现的位置为2，小于t的长度4，
        # 说明t中有重复出现，重复的个数为t.size()/pos = 2个，
        # 那么我们就要把重复的地方放入中括号中，注意中括号里不能直接放这个子字符串，
        # 而是应该从dp中取出对应位置的字符串，因为重复的部分有可能已经写成缩写形式了，
        # 比如题目中的例子5。再看一个例子，如果t = "abc"，那么t+t = "abcabc"，
        # 我们在里面找第二个t出现的位置为3，等于t的长度3，说明t中没有重复出现，那么replace就还是t。
        # 然后我们比较我们得到的replace和dp[i][j]中的字符串长度，把长度较小的赋给dp[i][j]即可，
        # 时间复杂度为O(n^3)，空间复杂度为O(n^2)。

        n = len(s)
        dp = [['' for j in range(n)] for i in range(n)]

        for j in range(n):
            dp[j][j] = s[j]
            for p in range(j):
                dp[p][j] = dp[p][j-1] + dp[j][j]
            i = j - 1
            
            while i + 1 >= j - i:
                sub = s[i+1:j+1]
                k = i - (j - i) + 1
                while k >= 0 and sub == s[k:j-i+k]:
                    dst = ('%d' % ((j + 1 - k) / (j - i))) + '[' + dp[i+1][j] + ']'
                    if len(dst) < len(dp[k][j]):
                        dp[k][j] = dst
                        for p in range(k):
                            if len(dp[p][k-1]) + len(dst) < len(dp[p][j]):
                                dp[p][j] = dp[p][k-1] + dst
                    k -= j - i
                i -= 1
        return dp[0][n-1]