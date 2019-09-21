# Given a text string and words (a list of strings), 
# return all index pairs [i, j] so that the substring text[i]...text[j] is in the list of words.

# Example 1:
# Input: text = "thestoryofleetcodeandme", words = ["story","fleet","leetcode"]
# Output: [[3,7],[9,13],[10,17]]

# Example 2:
# Input: text = "ababa", words = ["aba","ab"]
# Output: [[0,1],[0,2],[2,3],[2,4]]
# Explanation: 
# Notice that matches can overlap, see "aba" is found in [0,2] and [2,4].

# Note:
# All strings contains only lowercase English letters.
# It's guaranteed that all strings in words are different.
# 1 <= text.length <= 100
# 1 <= words.length <= 20
# 1 <= words[i].length <= 50
# Return the pairs [i,j] in sorted order (i.e. 
# sort them by their first coordinate in case of ties sort them by their second coordinate).

# Hints:
# For each string of the set, look for matches and store those matches indices.

class Solution(object):
    def indexPairs(self, text, words):
        """
        :type text: str
        :type words: List[str]
        :rtype: List[List[int]]
        """
        # find index and sort
        res = []
        for word in words:
            index = 0
            while True:
                index = text.find(word, index)
                if index != -1:
                    res.append([index, index+len(word)-1])
                    index += 1
                else:
                    break
        res.sort(key=lambda x:(x[0],x[1]))
        return res