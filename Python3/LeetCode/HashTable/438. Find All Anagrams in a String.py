# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
# Strings consists of lowercase English letters only 
# and the length of both strings s and p will not be larger than 20,100.
# The order of output does not matter.

# Example 1:
# Input:
# s: "cbaebabacd" p: "abc"
# Output:
# [0, 6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

# Example 2:
# Input:
# s: "abab" p: "ab"
# Output:
# [0, 1, 2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 滑动窗口
        left, right, match = 0, 0, 0
        need, have = {}, {}

        for c in p:
            need[c] = need.get(c, 0) + 1

        pset = set(p)
        plen = len(pset)
        window = len(p)
        res = []

        while right < len(s):
            # 先移动right
            if s[right] in pset:
                have[s[right]] = have.get(s[right], 0) + 1
                if have[s[right]] == need[s[right]]:
                    match += 1
            right += 1
            # 再移动left
            while match == plen:
                if right - left == window:
                    res.append(left)
                if s[left] in pset:
                    have[s[left]] = have.get(s[left], 0) - 1
                    if have[s[left]] < need[s[left]]:
                        match -= 1
                left += 1
        return res 