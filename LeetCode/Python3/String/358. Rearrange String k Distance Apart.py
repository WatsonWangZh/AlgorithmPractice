# Given a non-empty string s and an integer k, 
# rearrange the string such that the same characters are at least distance k from each other.
# All input strings are given in lowercase letters. 
# If it is not possible to rearrange the string, return an empty string "".

# Example 1:
# Input: s = "aabbcc", k = 3
# Output: "abcabc" 
# Explanation: The same letters are at least distance 3 from each other.

# Example 2:
# Input: s = "aaabc", k = 3
# Output: "" 
# Explanation: It is not possible to rearrange the string.

# Example 3:
# Input: s = "aaadbbcc", k = 2
# Output: "abacabcd"
# Explanation: The same letters are at least distance 2 from each other.

import heapq
from collections import Counter
class Solution(object):
    def rearrangeString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # 贪心排序，按出现元素最多数，分桶填充
        # Edge Case
        if k <= 1:
            return s
        
        arr = []
        # heapq默认为小根堆，取频率相反数实现大根堆。
        for char, freq in Counter(s).items():
            heapq.heappush(arr, (-freq, char))
        
        cnt = -arr[0][0]

        # 所有字符都是唯一的
        if cnt == 1:
            return s

        res = [[] for _ in range(cnt)]
        ptr = 0

        # Input: s = "aaabc", k = 3
        # 按出现元素最多数，分桶填充
        while arr:
            freq, char = heapq.heappop(arr)
            if -freq == cnt:
                for i in range(cnt):
                    res[i].append(char)
            else:
                for i in range(-freq):
                    res[ptr%(cnt-1)].append(char)
                    ptr += 1

        # 判断各独立桶中的元素个数，小于k说明无法完成
        if any(len(res[i]) < k for i in range(cnt-1)):
            return ""
        
        return "".join("".join(x) for x in res)