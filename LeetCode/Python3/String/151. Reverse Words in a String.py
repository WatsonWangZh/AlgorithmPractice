# Given an input string, reverse the string word by word.

# Example 1:
# Input: "the sky is blue"
# Output: "blue is sky the"

# Example 2:
# Input: "  hello world!  "
# Output: "world! hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.

# Example 3:
# Input: "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # M1. One line solution
        
        # return ' '.join(reversed(s.split()))
        # return " ".join(s.split()[::-1])

        # M2. 数组翻转拼接 O(n)

        if not s:
            return ""
        words = self.splitWords(s)
        reversedWords =  self.reverseString(words)
        reversedString = self.joinString(reversedWords)
        return reversedString

    def splitWords(self, s):
        words = []
        i = 0
        while i < len(s):
            if s[i] == " ":
                i += 1
            else:
                j = i
                while j< len(s) and s[j] != " ":
                    j += 1
                words.append(s[i:j])
                i = j + 1
        return words

    def reverseString(self, words):
        l = 0
        r = len(words) - 1
        while l < r:
            words[l], words[r] = words[r], words[l]
            l += 1
            r -= 1
        return words

    def joinString(self, words):
        d = " "
        res = ""
        for i, word in enumerate(words):
            if i == (len(words) - 1):
                return res + word
            res += word + d
        return res
