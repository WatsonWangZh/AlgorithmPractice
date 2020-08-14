# Given a string which consists of lowercase or uppercase letters, 
# find the length of the longest palindromes that can be built with those letters.
# This is case sensitive, for example "Aa" is not considered a palindrome here.
# Note:
# Assume the length of given string will not exceed 1,010.

# Example:
# Input:
# "abccccdd"
# Output:
# 7
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.


from collections import defaultdict
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 统计出来所有偶数个字符的出现总和，然后如果有奇数个字符的话，我们取出其最大偶数，然后最后结果加1即可。
        freq = defaultdict(int)
        odd = False
        res = 0

        for char in s:
            freq[char] += 1 

        for val in freq.values():
            # even
            if val % 2 == 0:
                res += val
            else:
                res += val - 1
                odd = True 
        
        if odd:
            res += 1 

        return res
