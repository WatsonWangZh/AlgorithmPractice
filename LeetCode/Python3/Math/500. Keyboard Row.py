# Given a List of words, return the words that can be typed using letters of alphabet 
# on only one row's of American keyboard like the image below.

# Example:
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]
 
# Note:
# You may use one character in the keyboard more than once.
# You may assume the input string will only contain letters of alphabet.

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # M1. 字符串in操作
        # row1 = 'qwertyuiop'
        # row2 = 'asdfghjkl'
        # row3 = 'zxcvbnm'
        # res = []

        # for word in words:
        #     w = word.lower()
        #     if (w[0] in row1): 
        #         tar = row1
        #     elif (w[0] in row2): 
        #         tar = row2
        #     else: 
        #         tar = row3
        #     for i in w: 
        #         if (i not in tar): break
        #     else: res.append(word)
        # return res

        # M2. 集合元素求交集
        row1 = set(['q','w','e','r','t','y','u','i','o','p'])
        row2 = set(['a','s','d','f','g','h','j','k','l'])
        row3 = set(['z','x','c','v','b','n','m'])
        res = []

        for word in words:
            t = set(word.lower())
            if t & row1 == t or t & row2 == t or t & row3 == t:
                res.append(word)
        return res