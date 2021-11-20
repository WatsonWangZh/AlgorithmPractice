# Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, 
# determine if two sentences are similar.
# For example, words1 = ["great", "acting", "skills"] and words2 = ["fine", "drama", "talent"] are similar, 
# if the similar word pairs are pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]].
# Note that the similarity relation is transitive. 
# For example, if "great" and "good" are similar, and "fine" and "good" are similar, then "great" and "fine" are similar.
# Similarity is also symmetric. 
# For example, "great" and "fine" being similar is the same as "fine" and "great" being similar. Also, a word is always similar with itself. 
# For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, 
# even though there are no specified similar word pairs.
# Finally, sentences can only be similar if they have the same number of words. 
# So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].

# Note:
# The length of words1 and words2 will not exceed 1000.
# The length of pairs will not exceed 2000.
# The length of each pairs[i] will be 2.
# The length of each words[i] and pairs[i][j] will be in the range [1, 20].

# Hints:
# Consider the graphs where each pair in "pairs" is an edge. 
# Two words are similar if they are the same, or are in the same connected component of this graph.

class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        # 并查集

        def find(word):
            # 已经连通
            if word in parents:
                tmp = find(parents[word])
                parents[word] = tmp
                return tmp
            # 尚未连通
            return word

        def union(parents, wd1, wd2):
            p1 = find(wd1)
            p2 = find(wd2)
            if p1 != p2:
                parents[p1] = p2
                
        if not pairs:
            return words1 == words2
        if len(words1) != len(words2):
            return False

        parents = {}
        # great good fine good
        for pair in pairs:
            union(parents, pair[0], pair[1])

        for i in range(len(words1)):
            if words1[i] != words2[i] and find(words1[i]) != find(words2[i]):
                return False
        return True
