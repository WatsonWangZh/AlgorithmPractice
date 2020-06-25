# Given a pattern and a string str, find if str follows the same pattern.
# Here follow means a full match, 
# such that there is a bijection between a letter in pattern and a non-empty substring in str.

# Example 1:
# Input: pattern = "abab", str = "redblueredblue"
# Output: true

# Example 2:
# Input: pattern = "aaaa", str = "asdasdasdasd"
# Output: true

# Example 3:
# Input: pattern = "aabb", str = "xyzabcxzyabc"
# Output: false

# Notes:
# You may assume both pattern and str contains only lowercase letters.

class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        # 递归回溯
        def helper(p, s, d):
            if not p or not s:
                if not p and not s:
                    return True
                return False

            if p[0] in d:
                if not s.startswith(d[p[0]]):
                    return False
                return helper(p[1:], s[len(d[p[0]]):], d)

            for e in range(1, len(s) - len(p) + 2): # +2 is the last position to compare
                if s[:e] in d.values():
                    continue
                d[p[0]] = s[:e]
                if helper(p[1:], s[e:], d):
                    return True
                del d[p[0]]

            return False

        return helper(pattern, str, {})