# Given a string which contains only lowercase letters, 
# remove duplicate letters so that every letter appears once and only once. 
# You must make sure your result is the smallest in lexicographical order among all possible results.

# Example 1:
# Input: "bcabc"
# Output: "abc"

# Example 2:
# Input: "cbacdcbc"
# Output: "acdb"
# Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        remain_counter = Counter(s)

        for c in s:
            if c not in stack:
                while stack and c < stack[-1] and  remain_counter[stack[-1]] > 0:
                    stack.pop()
                stack.append(c)
            remain_counter[c] -= 1
        return ''.join(stack)
