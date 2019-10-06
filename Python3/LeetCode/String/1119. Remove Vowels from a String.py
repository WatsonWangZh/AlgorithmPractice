# Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, 
# and return the new string.

# Example 1:
# Input: "leetcodeisacommunityforcoders"
# Output: "ltcdscmmntyfrcdrs"

# Example 2:
# Input: "aeiou"
# Output: ""
 
# Note:
# S consists of lowercase English letters only.
# 1 <= S.length <= 1000

# Hints:
# How to erase vowels in a string?
# Loop over the string and check every character, 
# if it is a vowel ignore it otherwise add it to the answer.

class Solution(object):
    def removeVowels(self, S):
        """
        :type S: str
        :rtype: str
        """
        res = []
        vowels = ['a','e','i','o','u']
        for ele in S:
            if ele not in vowels:
                res.append(ele)
            else:
                continue
        return ''.join(res)

        # vowels = ['a','e','i','o','u']
        # for x in S:
        #     if x in vowels:
        #         S = S.replace(x,"")
        # return S