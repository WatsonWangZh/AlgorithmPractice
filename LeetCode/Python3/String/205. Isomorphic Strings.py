# Given two strings s and t, determine if they are isomorphic.
# Two strings are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced 
# with another character while preserving the order of characters. 
# No two characters may map to the same character but a character may map to itself.

# Example 1:
# Input: s = "egg", t = "add"
# Output: true

# Example 2:
# Input: s = "foo", t = "bar"
# Output: false

# Example 3:
# Input: s = "paper", t = "title"
# Output: true

# Note:
# You may assume both s and t have the same length.

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # M1. One Line Solution
        return len(set(zip(s,t))) == len(set(s)) == len(set(t))

        # M2. 哈希表映射 O(n)
        # 我们要判断字母之间是否一一对应，即判断 s 中的相同字母是否对应到 t 中的相同字母，
        # 且 t 中的相同字母是否对应到 s 中的相同字母。
        # 我们用两个哈希表分别存储 s 到 t 和 t 到 s 的映射关系。
        # 然后从前往后扫描字符串，判断相同字符是否都映射到相同字符。
        # 时间复杂度分析：
        # 哈希表的插入、查找操作的时间复杂度是 O(1)，两个字符串均只扫描一遍，
        # 所以总时间复杂度是 O(n)。

        if len(s) != len(t):
            return False
        
        st = {}
        ts = {}
        for i in range(len(s)):
            if not st.get(s[i]):
                st[s[i]] = t[i]
            else:
                if st[s[i]] == t[i]:
                    continue
                else:
                    return False
                    
            if not ts.get(t[i]):
                ts[t[i]] = s[i]
            else:
                if ts[t[i]] == s[i]:
                    continue
                else:
                    return False
        return True