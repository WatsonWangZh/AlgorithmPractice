# Given a string S, return the number of substrings that have only one distinct letter.

# Example 1:
# Input: S = "aaaba"
# Output: 8
# Explanation: The substrings with one distinct letter are "aaa", "aa", "a", "b".
# "aaa" occurs 1 time.
# "aa" occurs 2 times.
# "a" occurs 4 times.
# "b" occurs 1 time.
# So the answer is 1 + 2 + 4 + 1 = 8.

# Example 2:
# Input: S = "aaaaaaaaaa"
# Output: 55

# Constraints:
# 1 <= S.length <= 1000
# S[i] consists of only lowercase English letters.

# Hints:
# What if we divide the string into substrings containing only one distinct character with maximal lengths?
# Now that you have sub-strings with only one distinct character, 
# Try to come up with a formula that counts the number of its sub-strings.
# Alternatively, Observe that the constraints are small so you can use brute force.

class Solution(object):
    def countLetters(self, S):
        """
        :type S: str
        :rtype: int
        """
        # 从一段长度为n的单一字母字符串中，分别选择出长度为1,2,3,…,n的子串，共有n * (n + 1) / 2个结果。
        # 因此，遍历字符串，分别统计出单一字母字符串的长度，累加所有结果即可。
        
        count = 1
        i = 0
        res = 0
        for i in range(1, len(S)):
            if S[i] == S[i-1]:
                count += 1
            else:
                res += (count) * (count+1) // 2
                count = 1
            i += 1
            
        return res + ((count) * (count+1) // 2)