# Implement strStr().
# Return the index of the first occurrence of needle in haystack, 
# or -1 if needle is not part of haystack.

# Example 1:
# Input: haystack = "hello", needle = "ll"
# Output: 2

# Example 2:
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

# Clarification:
# What should we return when needle is an empty string? 
# This is a great question to ask during an interview.
# For the purpose of this problem, we will return 0 
# when needle is an empty string. This is consistent to C's strstr() 
# and Java's indexOf().

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # M1. 枚举朴素算法
        if not needle:
            return 0
        
        if len(needle) > len(haystack):
            return -1
        
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

        # M2. KMP算法
        if not needle:
            return 0
        _next = [0] * len(needle)

        def getNext(needle, next):
            _next[0] = -1
            i, j = 0, -1
            while i < len(needle) - 1:
                if j == -1 or needle[i] == needle[j]:
                    i += 1
                    j += 1
                    _next[i] = j
                else:
                    j = _next[j]
        
        getNext(needle, _next)

        i, j = 0, 0
        while i < len(haystack) and j < len(needle):
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = _next[j]

        if j == len(needle):
            return i - j

        return -1 