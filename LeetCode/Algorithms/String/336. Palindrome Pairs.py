# Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, 
# so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

# Example 1:
# Input: ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]] 
# Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]

# Example 2:
# Input: ["bat","tab","cat"]
# Output: [[0,1],[1,0]] 
# Explanation: The palindromes are ["battab","tabbat"]

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        # 回文串，哈希表 O(nL^2) O(n)
        # 首先，我们先来分析一下两个单词组成的回文串有什么性质。如下图所示：
        # -----------------------
        # a       b    c        d
        # ac和cd分别表示两个单词，不妨假设cd较短。我们在线段中找到b点，使得 lab=lcdlab=lcd。
        # 则ad为回文串，等价于ab和cd的逆序相等，且bc是回文串。
        # 所以我们可以将所有单词的逆序存入哈希表，然后先枚举每个单词，再枚举每个单词的b点的位置，
        # 然后在哈希表中查找是否存在一个单词和ab相等，且bc是回文串，如果是 true，则找到了一组解。
        # 时间复杂度分析：令 n 表示单词个数，L 表示单词的平均长度。枚举单词的计算量是 O(n)，
        # 对每个单词枚举b点的位置的计算量是 O(L)，判断回文串的计算量是 O(L)，所以总时间复杂度是 O(nL^2)。

        d = {}
        for i, word in enumerate(words):
            d[word[::-1]] = i
        
        res = []
        for idx, word in enumerate(words):
            for i in range(len(word)):
                l, r = word[:i], word[i:]
                if l in d and idx != d[l] and r[::-1] == r:
                    res.append([idx, d[l]])
                    if not l:
                        res.append([d[l], idx])
                if r in d and idx != d[r] and l[::-1] == l:
                    res.append([d[r], idx])
                    if not r:
                        res.append([idx, d[r]])
        return res 

