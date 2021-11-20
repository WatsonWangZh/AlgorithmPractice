# Given a string, find the length of the longest substring T that contains at most k distinct characters.

# Example 1:
# Input: s = "eceba", k = 2
# Output: 3
# Explanation: T is "ece" which its length is 3.

# Example 2:
# Input: s = "aa", k = 1
# Output: 2
# Explanation: T is "aa" which its length is 2.

import collections
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # 滑动窗口 O(n)
        dic = {}
        startIdx, maxLen = 0, 0
        
        for i, c in enumerate(s):
            dic[c] = i
            if len(dic) > k:
                startIdx = min(dic.values())
                del dic[s[startIdx]]
                startIdx += 1
            maxLen = max(maxLen, i - startIdx + 1)
        return maxLen