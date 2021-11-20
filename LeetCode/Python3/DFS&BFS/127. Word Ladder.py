# Given two words (beginWord and endWord), and a dictionary's word list, 
# find the length of shortest transformation sequence from beginWord to endWord, such that:
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
# Note:
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.

# Example 1:
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.

# Example 2:
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # M1. BFS
        if endWord not in wordList:
            return 0

        # !! consider that the word list could be very long. therefore we could use set to quickly find a word
        from queue import Queue
        q = Queue()
        q.put(beginWord)
        step = 1
        found = {beginWord:1}
        wordSet = set(wordList)

        while not q.empty():
            rawWord = q.get()
            step = found[rawWord] + 1
            for i in range(len(rawWord)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    candidate = rawWord[:i] + c + rawWord[i+1:]
                    if candidate in wordSet and candidate not in found:
                        if candidate == endWord:
                            return step
                        found[candidate] = step
                        q.put(candidate)                   
        return 0

        # M2. 双向BFS

        wordSet = set(wordList)
        if endWord not in wordSet: 
            return 0
        
        l = len(beginWord)
        s1 = {beginWord}
        s2 = {endWord}
        wordSet.remove(endWord)
        step = 0
        while len(s1) > 0 and len(s2) > 0:
            step += 1
            if len(s1) > len(s2): s1, s2 = s2, s1
            s = set()   
            for w in s1:
                new_words = [
                    w[:i] + t + w[i+1:]  for t in "abcdefghijklmnopqrstuvwxyz" for i in range(l)]
                for new_word in new_words:
                    if new_word in s2: 
                        return step + 1
                    if new_word not in wordSet: 
                        continue
                    wordSet.remove(new_word)                        
                    s.add(new_word)
            s1 = s
        
        return 0
