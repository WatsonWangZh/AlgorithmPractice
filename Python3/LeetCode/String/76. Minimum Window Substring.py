# Given a string S and a string T, 
# find the minimum window in S which will contain all the characters in T in complexity O(n).

# Example:
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"

# Note:
# If there is no such window in S that covers all characters in T, return the empty string "".
# If there is such window, 
# you are guaranteed that there will always be only one unique minimum window in S.

# Hints:
# Use two pointers to create a window of letters in S, which would have all the characters from T.
# Since you have to find the minimum window in S which has all the characters from T, 
# you need to expand and contract the window using the two pointers and 
# keep checking the window for all the characters. 
# This approach is also called Sliding Window Approach. 

# L ------------------------ R , Suppose this is the window that contains all characters of T 
                          
#         L----------------- R , this is the contracted window. 
# We found a smaller window that still contains all the characters in T
# When the window is no longer valid, start expanding again using the right pointer. 

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # 滑动窗口 O(n)
        # 首先用哈希表统计出 T 中所有字符出现的次数，
        # 然后用两个指针 left,right(right≥left)来扫描整个字符串，
        # 同时用一个哈希表统计 left, right 之间每种字符出现的次数，每次遍历需要的操作如下：
            # 加入 s[right]，同时更新哈希表；
            # 检查 s[left] 是否多余，如果是，则移除 s[left]；
        # 检查当前窗口是否已经满足 T 中所有字符，如果是，则更新答案；
        # 时间复杂度分析：
        #   两个指针都严格递增，最多移动 n 次，所以总时间复杂度是 O(n)。

        d = {}
        cnt = 0
        for i in t:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
                cnt += 1

        result = "" 

        left = 0
        for right in range(len(s)):
            if s[right] in d:
                d[s[right]] -= 1
                if d[s[right]] == 0:
                    cnt -= 1

                if cnt == 0:
                    while left < right and (s[left] not in d or d[s[left]] < 0):    
                        if s[left] in d:
                            d[s[left]]+=1
                        left += 1
                    result = s[left:right+1] if (not result or len(result) > right-left+1) else result
        return result
