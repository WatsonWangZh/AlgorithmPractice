# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

# Example:
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
# Input: word1 = “coding”, word2 = “practice”
# Output: 3
# Input: word1 = "makes", word2 = "coding"
# Output: 1
# Note:
# You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # 模拟，数组扫描 最坏可达 O(n^2)
        # 直接遍历一遍数组，把两个给定单词所有出现的位置分别存到两个数组里，
        # 然后对两个数组进行两两比较更新结果。
        # w1 = []
        # w2 = []
        
        # for index, word in enumerate(words):
        #     if word == word1:
        #         w1.append(index)
        #     if word == word2:
        #         w2.append(index)
                
        # min_dist = float('inf')
        
        # for i1 in w1:
        #     for i2 in w2:
        #         min_dist = min(min_dist, abs(i1-i2))
                
        # return min_dist

        # 模拟优化 O(n)
        # 上面的那种方法并不高效，其实需要遍历一次数组就可以了，用两个变量p1,p2初始化为-1，
        # 然后遍历数组，遇到单词1，就将其位置存在p1里，遇到单词2，就将其位置存在p2里，
        # 如果此时p1, p2都不为-1了，那么我们更新结果。

        p1, p2, min_dist = -1, -1, float('inf')

        for i in range(len(words)):
            if words[i] == word1:
                p1 = i
            elif words[i] == word2:
                p2 = i

            if p1 != -1 and p2 != -1:
                min_dist = min(min_dist, abs(p1 - p2))

        return min_dist
