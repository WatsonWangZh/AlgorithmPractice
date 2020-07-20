# 1513. Number of Substrings With Only 1s
# User Accepted:5130
# User Tried:6021
# Total Accepted:5252
# Total Submissions:14643
# Difficulty:Medium
# Given a binary string s (a string consisting only of '0' and '1's).
# Return the number of substrings with all characters 1's.
# Since the answer may be too large, return it modulo 10^9 + 7.

# Example 1:
# Input: s = "0110111"
# Output: 9
# Explanation: There are 9 substring in total with only 1's characters.
# "1" -> 5 times.
# "11" -> 3 times.
# "111" -> 1 time.

# Example 2:
# Input: s = "101"
# Output: 2
# Explanation: Substring "1" is shown 2 times in s.

# Example 3:
# Input: s = "111111"
# Output: 21
# Explanation: Each substring contains only 1's characters.

# Example 4:
# Input: s = "000"
# Output: 0
 
# Constraints:
# s[i] == '0' or s[i] == '1'
# 1 <= s.length <= 10^5


class Solution:
    def numSub(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            if s[i] != '0':
                j = i+1
                while j < n and s[j] == '1':
                    j += 1
                c = j - i
                res += c * (c+1) // 2
                i = j - 1

        return res
