# Given a set of words (without duplicates), find all word squares you can build from them.
# A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).
# For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.
# b a l l
# a r e a
# l e a d
# l a d y

# Note:
# There are at least 1 and at most 1000 words.
# All words will have the exact same length.
# Word length is at least 1 and at most 5.
# Each word contains only lowercase English alphabet a-z.

# Example 1:
# Input:
# ["area","lead","wall","lady","ball"]
# Output:
# [
#   [ "wall",
#     "area",
#     "lead",
#     "lady"
#   ],
#   [ "ball",
#     "area",
#     "lead",
#     "lady"
#   ]
# ]
# Explanation:
# The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).

# Example 2:
# Input:
# ["abat","baba","atan","atal"]
# Output:
# [
#   [ "baba",
#     "abat",
#     "baba",
#     "atan"
#   ],
#   [ "baba",
#     "abat",
#     "baba",
#     "atal"
#   ]
# ]
# Explanation:
# The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).

# https://www.cnblogs.com/grandyang/p/6006000.html
# M1. 前缀字典
class Solution(object):
    
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        if not words:
            return []
        
        prefix_dict = {}
        size = len(words[0])
        for word in words:
            for i in range(1, size):
                key = word[:i]
                if key not in prefix_dict:
                    prefix_dict[key] = []
                prefix_dict[key].append(word)
        
        res = []
        for word in words:
            sol = [word]
            total_sol = []
            self.helper(prefix_dict, 1, sol, size, total_sol)
            
            if len(total_sol) != 0:
                res.extend(total_sol)
        
        return res
    
    def helper(self, prefix_dict, index, sol, size, total_sol):
        #print(index, size)
        if index == size:
            total_sol.append(sol)
            return
                
        prefix = ""
        for w in sol:
            #print(w, index)
            prefix += w[index]

        if prefix not in prefix_dict:
            return
        
        new_list = prefix_dict[prefix]
        
        for word in new_list:
            self.helper(prefix_dict, index + 1, sol + [word], size, total_sol)

# M2. 前缀树
class TrieNode():
    def __init__(self, val):
        self.val = val
        self.sons = {}
        self.words = []

class Solution(object):
    
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        root = TrieNode("*")
        
        for word in words:
            curr = root
            for c in word:
                curr.words.append(word)
                if not c in curr.sons:
                    curr.sons[c] = TrieNode(c)
                curr = curr.sons[c]
            curr.words.append(word)
        
        ans = []
        def search(squares, root, n):
            if len(squares) == n:
                ans.append(squares)
                return
            
            l = len(squares)
            curr = root
            for word in squares:
                if word[l] not in curr.sons:
                    return
                curr = curr.sons[word[l]]
            
            for word in curr.words:
                #if word in squares:
                #    continue
                search(squares + [word], root, n)
            
            return
    
        search([], root, len(words[0]))
        return ans