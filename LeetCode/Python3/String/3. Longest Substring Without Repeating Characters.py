# Given a string, find the length of the longest substring without repeating characters.

# Example 1:
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 

# Example 2:
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

from collections import deque
class Solution(object):
    def lengthOfLongestSubstring(self, s):

            # M1. HashTable
            # longest, start, visited = 0, 0, [False for _ in range(256)]
            # for i, char in enumerate(s):
            #     if visited[ord(char)]:
            #         while char != s[start]:
            #             visited[ord(s[start])] = False
            #             start += 1
            #         start += 1
            #     else:
            #         visited[ord(char)] = True
            #     longest = max(longest, i - start + 1)
            # return longest

            # if not s:
            # return 0

            # M2. 双端队列（deque，全名double-ended queue）
            if not s:
                return 0

            maxlen = 1
            rec = deque()
            rec.append(s[0])

            for c in s[1:]:
                if c in rec:
                    maxlen = max(maxlen, len(rec))
                    watch = rec.popleft()
                    while(watch!=c):
                        watch = rec.popleft()
                    rec.append(c)
                else:
                    rec.append(c)
            maxlen = max(maxlen, len(rec))
            return maxlen
