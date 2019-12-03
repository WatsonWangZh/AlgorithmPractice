# Given a string s and a string t, check if s is subsequence of t.
# You may assume that there is only lower case English letters in both s and t. 
# t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).
# A subsequence of a string is a new string which is formed from the original string 
# by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. 
# (ie, "ace" is a subsequence of "abcde" while "aec" is not).

# Example 1:
# s = "abc", t = "ahbgdc"
# Return true.

# Example 2:
# s = "axc", t = "ahbgdc"
# Return false.

# Follow up:
# If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. 
# In this scenario, how would you change your code?

# Credits:
# Special thanks to @pbrother for adding this problem and creating all test cases.

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # for base
        # 扫描一遍t串即可，然后看能不能让指向s串的指针一直移动到最后
        
        if not s:
            return True
        i = 0
        for j in range(len(t)):
            if s[i] == t[j]:
                i += 1
            if i == len(s):
                return True
        return False

        # follow up
        # 扫描一遍t串，然后将每个字母的位置放入相应的26个字母的HashTable中
        # 后面就扫描s串，s串是什么字符就对应到哪个字符的HashTable中去查找，然后将代表位置的变量更新。

        memo = {}
        for i in range(len(t)):
            memo.setdefault(t[i], []).append(i)
        pre = -1
        for c in s:
            if c not in memo: 
                return False
            idxs = memo[c]
            i = 0
            while i < len(idxs) and idxs[i] <= pre: 
                i += 1
            if i == len(idxs): 
                return False
            pre = idxs[i]

        return True
