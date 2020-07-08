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

class Solution(object):
    def lengthOfLongestSubstring(self, s):

            #M1. 滑动窗口 + flag数组
            if not s:
                return 0

            res, start = 1, 0
            visited = [False for _ in range(256)]

            for i, char in enumerate(s):

                if visited[ord(char)]:
                    while char != s[start]:
                        visited[ord(s[start])] = False
                        start += 1

                    start += 1
                else:
                    visited[ord(char)] = True

                res = max(res, i - start + 1)

            return res

            # M2. 滑动窗口 + temp list
            if not s:
                return 0

            from collections import deque
            res = 1
            rec = deque(s[0])

            for c in s[1:]:

                if c in rec:
                    res = max(res, len(rec))
                    watch = rec.popleft()
                    while(watch != c):
                        watch = rec.popleft()
                    rec.append(c)

                else:
                    rec.append(c)

            res = max(res, len(rec))

            return res


            # M3. 滑动窗口 + hash count
            if not s:
                return 0

            from collections import defaultdict
            count = defaultdict(int)
            res =  1
            l, r = 0, 0

            while r < len(s):
                count[s[r]] += 1
                while count[s[r]] > 1:
                    count[s[l]] -= 1
                    l += 1
                res = max(res, r-l+1)
                r += 1

            return res
