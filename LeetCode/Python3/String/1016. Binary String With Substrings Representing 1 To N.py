# Given a binary string S (a string consisting only of '0' and '1's) and a positive integer N, 
# return true if and only if for every integer X from 1 to N, 
# the binary representation of X is a substring of S.

# Example 1:
# Input: S = "0110", N = 3
# Output: true

# Example 2:
# Input: S = "0110", N = 4
# Output: false

# Note:
# 1 <= S.length <= 1000
# 1 <= N <= 10^9

# Hints:
# We only need to check substrings of length at most 20, because 10^6 has 20 bits.

class Solution(object):
    def queryString(self, S, N):
        """
        :type S: str
        :type N: int
        :rtype: bool
        """
        # 子串枚举 O(S.length)
        # 直接枚举 S 的长度不超过 30 的子串，如果子串构成了 1 到 N 中的数字，则加到一个集合中，最后判断集合的大小是否等于 N。
        # 时间复杂度
        # 枚举子串的长度不超过 30，故时间复杂度为 O(S)。
        # 空间复杂度
        # 需要一个集合来保存出现过的数字，但数字的个数仍然不超过 30×S.length，故空间复杂度为 O(S)。
        
        result = set()
        n = len(S)
        for i in range(n):
            temp = 0
            for length in range(1, n-i+1):
                if length == 31:
                    break
                temp = temp * 2 + int(S[i+length-1])
                if temp > N:
                    break
                if 0 < temp <= N:
                    result.add(temp)
        return len(result) == N