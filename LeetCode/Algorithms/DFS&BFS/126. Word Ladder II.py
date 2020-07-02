# Given two words (beginWord and endWord), and a dictionary's word list, 
# find all shortest transformation sequence(s) from beginWord to endWord, such that:
# Only one letter can be changed at a time
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

# Note:
# Return an empty list if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.

# Example 1:
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# Output:
# [
#   ["hit","hot","dot","dog","cog"],
#   ["hit","hot","lot","log","cog"]
# ]

# Example 2:
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# Output: []
# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        # https://leetcode-cn.com/problems/word-ladder-ii/solution/cong-bfssi-xiang-kai-shi-de-jin-hua-zhi-lu-2400msy/#comment
        # M1. 单向BFS 
        # Runtime: 3068 ms
        # Memory Usage: 17.2 MB

        if endWord not in wordList:
            return []
        ws = set(wordList)
        
        def edges(word):
            arr=list(word)
            for i in range(len(arr)):
                c = arr[i]
                for j in range(97,123):
                    arr[i] = chr(j)
                    newWord = ''.join(arr)
                    if newWord in ws and newWord not in marked:
                        yield newWord
                arr[i]=c

        res=[]
        marked=set()
        queue=[[beginWord]]

        while queue:
            temp=[]
            found=False
            for words in queue:
                marked.add(words[-1])

            for words in queue:
                for w in edges(words[-1]):
                    v = words+[w]
                    if w == endWord:
                        res.append(v)
                        found = True
                    temp.append(v)

            if found:          #找到就不再遍历了，即使再有endWord，路径也会更长
                break
            queue=temp
        return res


        # M2. 优化 双向BFS + hash
        # Runtime: 96 ms
        # Memory Usage: 17.7 MB
        
        from collections import defaultdict
        if not endWord in wordList:
            return []

        ha = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                ha[word[:i]+"*"+word[i+1:]].append(word)

        def edges(word):
            for i in range(len(word)):
                for newWord in ha[word[:i]+'*'+word[i+1:]]:
                    if not newWord in marked:
                        yield newWord

        def findPath(end):
            res=[]
            for curr in end:
                for parent in path[curr[0]]:
                    res.append([parent]+curr)
            return res

        marked = set()
        path = defaultdict(set)
        begin = set([beginWord])
        end = set([endWord])
        forward = True

        while begin and end:
            if len(begin)>len(end):
                begin,end = end,begin
                forward = not forward

            temp = set()
            for word in begin:
                marked.add(word)

            for word in begin:
                for w in edges(word):
                    temp.add(w)
                    if forward:
                        path[w].add(word)
                    else:
                        path[word].add(w)
            begin = temp

            if begin&end:
                res = [[endWord]]
                while res[0][0] != beginWord:
                    res = findPath(res)
                return res

        return []

