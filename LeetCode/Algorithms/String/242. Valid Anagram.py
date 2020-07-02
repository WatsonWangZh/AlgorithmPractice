# Given two strings s and t , write a function to determine if t is an anagram of s.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Note:
# You may assume the string contains only lowercase alphabets.
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?

# 所谓 anagram, 就是两个词所用的字母及其个数都是一样的，但是，字母的位置不一样。比如 abcc 和 cbca 就是 anagram.
from collections import Counter 
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict_s = Counter(s)
        dict_t = Counter(t)
        return dict_s == dict_t
