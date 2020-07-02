# Given a string s and a list of strings dict, 
# you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict. 
# If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. 
# Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.

# Example 1:
# Input: 
# s = "abcxyz123"
# dict = ["abc","123"]
# Output:
# "<b>abc</b>xyz<b>123</b>"

# Example 2:
# Input: 
# s = "aaabbcc"
# dict = ["aaa","aab","bc"]
# Output:
# "<b>aaabbc</b>c"

# Note:
# The given dict won't contain duplicates, and its length won't exceed 100.
# All the strings in input have length in range [1, 1000].

class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        bold = [False] * len(s)
        for word in dict:
            for i in range(len(s)-len(word)+1):
                if s[i:i+len(word)] == word:
                    for index in range(i,i+len(word)):
                        bold[index] = True
        index = 0
        result = ''
        while index < len(s):
            if not bold[index] :
                result += s[index]
                index += 1
            else:
                tmp = ''
                while index < len(s) and bold[index]:
                    tmp += s[index]
                    index += 1
                tmp = '<b>' + tmp + '</b>'
                result += tmp
        return result
