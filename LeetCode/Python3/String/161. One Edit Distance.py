# Given two strings s and t, determine if they are both one edit distance apart.
# Note: 
# There are 3 possiblities to satisify one edit distance apart:
# Insert a character into s to get t
# Delete a character from s to get t
# Replace a character of s to get t

# Example 1:
# Input: s = "ab", t = "acb"
# Output: true
# Explanation: We can insert 'c' into s to get t.

# Example 2:
# Input: s = "cab", t = "ad"
# Output: false
# Explanation: We cannot get t from s by only one step.

# Example 3:
# Input: s = "1203", t = "1213"
# Output: true
# Explanation: We can replace '0' with '1' to get t.

class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 数组扫描 O(n)
        # 分三种情况考虑：
        # 字符串长度之差大于1，则编辑距离一定大于1，返回false；
        # 字符串长度相等，则有且只有一个字符不同时，才返回true；
        # 字符串长度差1，则只需判断短字符串是否是长字符串的子序列即可。
        # 时间复杂度分析：
        # 三种情况都只需将两个字符串遍历一次，所以时间复杂度是 O(n)。

        diff = abs(len(s) - len(t))
        if diff > 1:
            return False
        
        if len(s) > len(t):
            return self.isOneEditDistance(t, s)
        
        n = len(s)
        m = len(t)
        if diff == 0:
            cnt = 0
            for i in range(n):
                if s[i] != t[i]:
                    cnt += 1
            return cnt == 1
        
        else:
            for i in range(n):
                if s[i] != t[i]:
                    return s[i:] == t[i+1:]
            return True