# Given a set of keywords words and a string S, make all appearances of all keywords in S bold. 
# Any letters between <b> and </b> tags become bold.
# The returned string should use the least number of tags possible, 
# and of course the tags should form a valid combination.
# For example, given that words = ["ab", "bc"] and S = "aabcd", 
# we should return "a<b>abc</b>d". Note that returning "a<b>a<b>b</b>c</b>d" would use more tags, 
# so it is incorrect.

# Note:
# words has length in range [0, 50].
# words[i] has length in range [1, 10].
# S has length in range [0, 500].
# All characters in words[i] and S are lowercase letters.

# Hints:
# First, determine which letters are bold and store that information in 
# mask[i] = if i-th character is bold. Then, insert the tags at the beginning and end of groups. 
# The start of a group is if and only if (mask[i] and (i == 0 or not mask[i-1])), 
# and the end of a group is similar.

import itertools
class Solution(object):
    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        bold = [False] * len(S)
        for word in words:
            for i in range(len(S)-len(word)+1):
                if S[i:i+len(word)] == word:
                    for index in range(i,i+len(word)):
                        bold[index] = True
        index = 0
        result = ''
        while index < len(S):
            if not bold[index] :
                result += S[index]
                index += 1
            else:
                tmp = ''
                while index < len(S) and bold[index]:
                    tmp += S[index]
                    index += 1
                tmp = '<b>' + tmp + '</b>'
                result += tmp
        return result
