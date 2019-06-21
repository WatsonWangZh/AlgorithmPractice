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
            longest, start, visited = 0, 0, [False for _ in range(256)]
            for i, char in enumerate(s):
                if visited[ord(char)]:
                    while char != s[start]:
                        visited[ord(s[start])] = False
                        start += 1
                    start += 1
                else:
                    visited[ord(char)] = True
                longest = max(longest, i - start + 1)
            return longest

def main():
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("bbbbb"))
    print(s.lengthOfLongestSubstring("pwwkew"))

if __name__ == "__main__":
    main()

