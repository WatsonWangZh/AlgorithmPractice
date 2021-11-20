# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. 
# In other words, one of the first string's permutations is the substring of the second string.

# Example 1:
# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:
# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
 
# Note:
# The input strings only contain lower case letters.
# The length of both given strings is in range [1, 10,000].

# Hints:
# Obviously, brute force will result in TLE. Think of something else.
# How will you check whether one string is a permutation of another string?
# One way is to sort the string and then compare. But, Is there a better way?
# If one string is a permutation of another string then they must one common metric. What is that?
# Both strings must have same character frequencies, if one is permutation of another. 
# Which data structure should be used to store frequencies?
# What about hash table? An array of size 26?

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 滑动窗口
        left, right, match = 0, 0, 0
        need, have = {}, {}

        for c in s1:
            need[c] = need.get(c, 0) + 1

        pset = set(s1)
        plen = len(pset)
        window = len(s1)
        res = []

        while right < len(s2):
            # 先移动right
            if s2[right] in pset:
                have[s2[right]] = have.get(s2[right], 0) + 1
                if have[s2[right]] == need[s2[right]]:
                    match += 1
            right += 1
            # 再移动left
            while match == plen:
                if right - left == window:
                    return True
                if s2[left] in pset:
                    have[s2[left]] = have.get(s2[left], 0) - 1
                    if have[s2[left]] < need[s2[left]]:
                        match -= 1
                left += 1
        return False