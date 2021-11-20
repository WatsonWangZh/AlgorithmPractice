# Given a string s , find the length of the longest substring t that contains at most 2 distinct characters.

# Example 1:
# Input: "eceba"
# Output: 3
# Explanation: t is "ece" which its length is 3.

# Example 2:
# Input: "ccaabbb"
# Output: 5
# Explanation: t is "aabbb" which its length is 5.

import collections
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        # M1. 滑动窗口 实现之一 O(n)
        # n = len(s) 
        # if n < 3:
        #     return n
        
        # # sliding window left and right pointers
        # left, right = 0, 0
        # # hashmap character -> its rightmost position 
        # # in the sliding window
        # hashmap = collections.defaultdict()

        # max_len = 2
        
        # while right < n:
        #     # slidewindow contains less than 3 characters
        #     if len(hashmap) < 3:
        #         hashmap[s[right]] = right
        #         right += 1

        #     # slidewindow contains 3 characters
        #     if len(hashmap) == 3:
        #         # delete the leftmost character
        #         del_idx = min(hashmap.values())
        #         del hashmap[s[del_idx]]
        #         # move left pointer of the slidewindow
        #         left = del_idx + 1

        #     max_len = max(max_len, right - left)

        # return max_len

        # M2. 滑动窗口 实现之二 O(n)
        # d = collections.Counter()
        # # same as collections.defaultdic(int)
        # q = collections.deque([])
        # max_len = 0

        # for c in s:
        #     q.append(c)
        #     d[c] += 1
        #     while len(d)>2:
        #         old_c = q.popleft()
        #         d[old_c] -= 1
        #         if d[old_c] == 0:
        #             del d[old_c]
        #     max_len = max(max_len, len(q))
            
        # return max_len

        # 二刷
        dic = {}
        startIdx, maxLen = 0, 0
        
        for i, c in enumerate(s):
            dic[c] = i
            if len(dic) > 2:
                startIdx = min(dic.values())
                del dic[s[startIdx]]
                startIdx += 1
            maxLen = max(maxLen, i - startIdx + 1)
        return maxLen