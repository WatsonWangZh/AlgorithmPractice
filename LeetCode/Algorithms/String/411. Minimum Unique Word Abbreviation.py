# A string such as "word" contains the following abbreviations:
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
# Given a target string and a set of strings in a dictionary, 
# find an abbreviation of this target string with the smallest possible length such that 
# it does not conflict with abbreviations of the strings in the dictionary.
# Each number or letter in the abbreviation is considered length = 1. 
# For example, the abbreviation "a32bc" has length = 4.

# Note:
# In the case of multiple answers as shown in the second example below, you may return any one of them.
# Assume length of target string = m, and dictionary size = n. 
# You may assume that m ≤ 21, n ≤ 1000, and log2(n) + m ≤ 20.

# Examples:
# "apple", ["blade"] -> "a4" (because "5" or "4e" conflicts with "blade")
# "apple", ["plain", "amber", "blade"] -> "1p3" (other valid answers include "ap3", "a3e", "2p2", "3le", "3l1").

from collections import defaultdict
class Solution(object):
    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """
        # http://bookshadow.com/weblog/2016/10/02/leetcode-minimum-unique-word-abbreviation/
        # https://www.cnblogs.com/grandyang/p/5935836.html

        self.target = target
        self.size = len(target)

        # 过滤掉字典中长度不同的word，减少无谓比较。
        self.filtered_list = [d for d in dictionary if len(d) == self.size]

        # 最短长度答案暂定为自身，在dfs过程中更新。
        self.ans = target
        self.length = self.size

        self.dfs('', 0, 0)

        return self.ans

    def dfs(self, abbr, length, depth):
        
        # "apple", ["blade"] -> "a4" (because "5" or "4e" conflicts with "blade")
        print(abbr)
        # 找不到缩写解或比已知的缩写解还要长
        if length >= self.length:
            return

        if depth == self.size:
            for word in self.filtered_list:
                if self.validWordAbbreviation(word, abbr):
                    return

            # 得到最短的一个候选解
            self.ans = abbr
            self.length = length
            return

        # 不缩写当前字符
        self.dfs(abbr + self.target[depth], length + 1, depth + 1)

        # 缩写当前字符，且最少缩写两个，以达到减少长度的目的。
        if depth == 0 or not abbr[-1].isdigit():
            for x in range(2, self.size - depth + 1):
                self.dfs(abbr + str(x), length + 1, depth + x)

    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        size = len(word)
        cnt = loc = 0
        for w in abbr:
            if w.isdigit():
                if w == '0' and cnt == 0:
                    return False
                cnt = cnt * 10 + int(w)
            else:
                loc += cnt
                cnt = 0
                if loc >= size or word[loc] != w:
                    return False
                loc += 1
        return loc + cnt == size
