# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).
# Note:
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like ? or *.

# Example 1:
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".

# Example 2:
# Input:
# s = "aa"
# p = "*"
# Output: true
# Explanation: '*' matches any sequence.

# Example 3:
# Input:
# s = "cb"
# p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

# Example 4:
# Input:
# s = "adceb"
# p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".

# Example 5:
# Input:
# s = "acdcb"
# p = "a*c?b"
# Output: false

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # M1. 记忆化递归  Memory Limit Exceeded
        p = self.remove_duplicate_stars(p)
        # memorization hashmap to be used during the recursion
        self.dp = {}
        return self.helper(s, p)
    
    def remove_duplicate_stars(self, p):
        if p == '':
            return p
        p1 = [p[0],]
        for x in p[1:]:
            if p1[-1] != '*' or p1[-1] == '*' and x != '*':
                p1.append(x)
        return ''.join(p1) 

    def helper(self, s, p):
        dp = self.dp
        if (s, p) in dp:
            return dp[(s, p)]

        if p == s or p == '*':
            dp[(s, p)] = True
        elif p == '' or s == '':
            dp[(s, p)] = False
        elif p[0] == s[0] or p[0] == '?':
            dp[(s, p)] = self.helper(s[1:], p[1:])
        elif p[0] == '*':
            dp[(s, p)] = self.helper(s, p[1:]) or self.helper(s[1:], p)
        else:
            dp[(s, p)] = False

        return dp[(s, p)]


        # M2. 动态规划 O(mn) O(mn)
        # 设计状态 f(i,j) 表示 s 串的前 i 个字符与 p 串的前 j 个字符是否匹配。
        # 初始化 f(0,0)=true。
        # 转移方程，假设 s 串的第i个字符为变量 x，p 串的第 j 个字符为变量 y。
        # (1) f(i, j) = f(i, j) | f(i - 1, j - 1) 当且仅当 x == y 或 y == '?'。
        # (2) f(i, j) = f(i, j) | f(i - 1, j) | f(i, j - 1)当且仅当 y == '*'。
        # 解释：
        # (1) 的含义是 s 串的第 i 个字符与 p 串的第 j 个字符匹配对应，所以 f(i,j) 的值可以由 f(i−1,j−1) 的值来转移。
        # (2) 的含义是，特别地，如果 p 串的第 j 个字符为 *，
        # 则可以让 s 串的第 i 个字符同之前的字符串一起（之前的字符串可以为空）与这个 * 对应，
        # 或者是 s 串的第 i 个字符与 p 串的第 j−1 个字符对应（* 匹配零个字符）。
        # 最终 f(n,m) 的值表示字符串是否匹配。
        # 时间复杂度
        # 状态数量为 O(nm)，决策数为 O(1)，转移时间为 O(1)。故总时间复杂度为 O(nm)。
        m, n = len(s), len(p)
        f = [[False] * (n + 1) for _ in range(m+1)]
        f[0][0] = True
        for i in range(m+1):
            for j in range(1, n+1):
                y = p[j-1]
                if i > 0:
                    x = s[i-1]
                    if x == y or y == '?':
                        f[i][j] = f[i][j] or f[i-1][j-1]
                if y == '*':
                    f[i][j] = f[i][j] or f[i][j-1]
                    if i > 0:
                        f[i][j] = f[i][j] or f[i-1][j]
        return f[m][n]

        # M3. 双指针扫描 O(nm) O(1)
        # 使用i,j分别代表匹配串和模式串当前匹配位置。
        # 如果s[i] == p[j] || p[j] == '?'，代表精准匹配，这时候双指针后移
        # 如果不能匹配，查看当前是否是*，如果是那么记录当前*号位置，以及当前匹配串指针位置，模式串指针后移。
        # 如果不能匹配且不是*，说明这个时候失配了，
        # 需要尝试恢复当上一个星号的状态，将模式串指针指向上一个星号的下一个字符，
        # 匹配串指针也指向上一次失配的下一个位置，尝试重新匹配。
        # 如果不能恢复现场，返回false。
        # 最后去除模式串末尾多余的星号，再判断当字符串匹配完了之后，模式串是否也匹配完了。
        # 最坏的时间复杂度也是O(nm)的，但是平均的时间复杂度会稍微好一点。

        i, j, match, starIdx = 0, 0, 0, -1
        m, n = len(s), len(p)
        while i < m:
            if j < n and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            elif j < n and p[j] == '*':
                starIdx = j
                match = i
                j += 1
            elif starIdx != -1:
                j = starIdx + 1
                match += 1
                i = match
            else:
                return False
        while j < n and p[j] == '*':
            j += 1
        return j == n