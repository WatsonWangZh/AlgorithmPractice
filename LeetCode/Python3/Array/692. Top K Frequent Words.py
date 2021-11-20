# Given a non-empty list of words, return the k most frequent elements.
# Your answer should be sorted by frequency from highest to lowest. 
# If two words have the same frequency, then the word with the lower alphabetical order comes first.

# Example 1:
# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]
# Explanation: "i" and "love" are the two most frequent words.
#     Note that "i" comes before "love" due to a lower alphabetical order.

# Example 2:
# Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
# Output: ["the", "is", "sunny", "day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
#     with the number of occurrence being 4, 3, 2 and 1 respectively.

# Note:
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Input words contain only lowercase letters.

# Follow up:
# Try to solve it in O(n log k) time and O(n) extra space.

import heapq
class item:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
        
    def __eq__(self, other):
        if self.freq == other.freq and self.word == other.word:
            return True
        else:
            return False
    
    def __lt__(self, other):
        if self.freq < other.freq or self.freq == other.freq and self.word > other.word:
            return True
        else:
            return False

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """

        # M1. Official Solution: 
        # Count and Sort

        # import collections
        # count = collections.Counter(words)
        # candidates = count.keys()
        # candidates.sort(key = lambda w: (-count[w], w))
        # return candidates[:k]

        # M2. 优先队列 O(nlogk)
        # 因为要求是O(nlogk)的时间复杂度，提示我们使用优先队列（堆）这个数据结构来解决问题。
        # 首先我们使用一个hash表预先统计出每个单词出现的次数，
        # 然后我们定一个item的结构体存储每个单词以及出现次数。
        # 再使用一个容量为K的优先队列（小顶堆序）。
        # 先将前k个单词塞进去，然后遍历剩余单词，如果当前单词比堆顶元素大，那么我们就弹出堆顶元素，将当前单词加入队列。
        # 遍历完所有单词后，优先队列中存储的就是最大的k个单词，然后依次弹出，
        # 因为是小顶堆所以弹出的单词是从小到大的，我们再做一次反转就可以了。

        h = []
        dic = {}

        for word in words:
            if word not in dic:
                dic[word] = 0
            dic[word] += 1
        
        for word, freq in dic.items():
            heapq.heappush(h, item(word, freq))
            if len(h) > k:
                heapq.heappop(h)

        result = []
        while len(h) != 0:
            result.append(heapq.heappop(h).word)
            
        result.reverse()

        return result
        