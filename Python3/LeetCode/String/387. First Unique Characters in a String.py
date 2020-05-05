# Given a string, find the first non-repeating character in it and return it's index. 
# If it doesn't exist, return -1.

# Examples:
# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.

# Note: You may assume the string contain only lowercase letters.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        res = -1
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        for i, c in enumerate(s):
            if d[c] == 1:
                res = i
                break
        return res