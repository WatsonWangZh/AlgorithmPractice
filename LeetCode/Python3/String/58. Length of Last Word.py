# Given a string s consists of upper/lower-case alphabets and 
# empty space characters ' ', return the length of last word in the string.
# If the last word does not exist, return 0.
# Note: A word is defined as a character sequence consists of non-space characters only.

# Example:
# Input: "Hello World"
# Output: 5

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # M1.手写统计实现
        # index = len(s) - 1
        # while index >= 0 and s[index] == " ":
        #     index -= 1
        # temp = index
        # while index >= 0 and s[index] != " ":
        #     index -= 1
        # return temp - index

        # M2.调库
        return len(s.split()[-1]) if len(s.split()) else 0
