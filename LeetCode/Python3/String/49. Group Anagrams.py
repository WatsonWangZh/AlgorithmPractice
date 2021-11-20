# Given an array of strings, group anagrams together.

# Example:
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:
# All inputs will be in lowercase.
# The order of your output does not matter.

import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # M1.用defaultdict来存{(‘e’, ‘a’, ‘t’): [‘eat’,’ate’]}的键值对
        # d = collections.defaultdict(list)
        # for s in strs:
        #     d[tuple(sorted(s))].append(s)
        # return d.values()

        # M2.用普通的dict, 需要注意没有key的情况。
        # d = {}
        # for s in strs:
        #     if tuple(sorted(s)) in d:
        #         d[tuple(sorted(s))].append(s)
        #     else:
        #         d[tuple(sorted(s))] = [s]
        # return d.values()

        # M3.记每个字母出现的次数，表示为{(2, 1, 0, 0, …, 0): [‘aab’, ‘aba’]}, 用ord()函数来找到字母的相对位置
        d = collections.defaultdict(list)
        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - ord('a')] +=1
            d[tuple(count)].append(word)
        return d.values()
        