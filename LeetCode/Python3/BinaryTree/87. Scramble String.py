# Given a string s1, we may represent it as a binary tree 
# by partitioning it to two non-empty substrings recursively.
# Below is one possible representation of s1 = "great":
#     great
#    /    \
#   gr    eat
#  / \    /  \
# g   r  e   at
#            / \
#           a   t
# To scramble the string, we may choose any non-leaf node and swap its two children.
# For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".
#     rgeat
#    /    \
#   rg    eat
#  / \    /  \
# r   g  e   at
#            / \
#           a   t
# We say that "rgeat" is a scrambled string of "great".
# Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".
#     rgtae
#    /    \
#   rg    tae
#  / \    /  \
# r   g  ta  e
#        / \
#       t   a
# We say that "rgtae" is a scrambled string of "great".

# Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

# Example 1:
# Input: s1 = "great", s2 = "rgeat"
# Output: true

# Example 2:
# Input: s1 = "abcde", s2 = "caebd"
# Output: false

class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # 暴力搜索 O(5^n)
        # 递归判断两个字符串是否可以相互转化。
        # 首先判断两个字符串的字符集合是否相同，如果不同，则两个字符串一定不可以相互转化。
        # 然后枚举第一个字符串左半部分的长度，分别递归判断两种可能的情况：
            # 该节点不发生翻转，则分别判断两个字符串的左右两部分是否分别可以相互转化；
            # 该节点发生翻转，则分别判断第一个字符串的左边是否可以和第二个字符串的右边相互转化，
            # 且第一个字符串的右边可以和第二个字符串的左边相互转化；

        if len(s1) != len(s2): 
            return False
        if s1 == s2: 
            return True
        ss1 = sorted(s1)
        ss2 = sorted(s2)
        if ss1 != ss2: 
            return False

        n = len(s1)
        for i in range(1, n):
            if self.isScramble(s1[0:i], s2[0:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[0:i], s2[n-i:]) and self.isScramble(s1[i:], s2[0:n-i]):
                return True

        return False
