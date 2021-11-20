# Design a class which receives a list of words in the constructor, 
# and implements a method that takes two words word1 and word2 
# and return the shortest distance between these two words in the list.
# Your method will be called repeatedly many times with different parameters. 

# Example:
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
# Input: word1 = “coding”, word2 = “practice”
# Output: 3
# Input: word1 = "makes", word2 = "coding"
# Output: 1

# Note:
# You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

import collections
class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.words = words
        self.idx = collections.defaultdict(list)
        for i, w in enumerate(words):
            self.idx[w].append(i)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        min_dist = float('inf')
        i = j = 0
        w1 = self.idx[word1]
        w2 = self.idx[word2]

        # 模拟，数组扫描 最坏可达 O(n^2)
        # 直接遍历一遍数组，把两个给定单词所有出现的位置分别存到两个数组里，
        # 然后对两个数组进行两两比较更新结果。

        for i in range(len(w1)):
            for j in range(len(w2)):
                min_dist = min(min_dist, abs(w1[i]-w2[j]))

        # 优化 O(n)
        # while i < len(w1) and j < len(w2):
        #     min_dist = min(min_dist, abs(w1[i]-w2[j]))
        #     if w1[i] > w2[j]:
        #         j += 1
        #     else:
        #         i += 1

        return min_dist


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
