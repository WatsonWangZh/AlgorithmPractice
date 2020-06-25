# Given an array of n distinct non-empty strings, 
# you need to generate minimal possible abbreviations for every word following rules below.
# Begin with the first character and then the number of characters abbreviated, which followed by the last character.
# If there are any conflict, that is more than one words share the same abbreviation, 
# a longer prefix is used instead of only the first character until making the map from word to abbreviation become unique. 
# In other words, a final abbreviation cannot map to more than one original words.
# If the abbreviation doesn't make the word shorter, then keep it as original.

# Example:
# Input: ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
# Output: ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]

# Note:
# Both n and the length of each word will not exceed 400.
# The length of each word is greater than 1.
# The words consist of lowercase English letters only.
# The return answers should be in the same order as the original array.

import collections
class Solution(object):
    def wordsAbbreviation(self, dict):
        """
        :type dict: List[str]
        :rtype: List[str]
        """
        # 规则分桶，最长前缀长度，消除冲突
        
        def longest_common_prefix(a, b):
            i = 0
            while i < len(a) and i < len(b) and a[i] == b[i]:
                i += 1
            return i
    
        ans = [None for _ in dict]
    
        groups = collections.defaultdict(list)
        for index, word in enumerate(dict):
            groups[len(word), word[0], word[-1]].append((word, index))
    
        for (size, first, last), enum_words in groups.items():
            enum_words.sort()
            lcp = [0] * len(enum_words)
            for i, (word, _) in enumerate(enum_words):
                if i:
                    word2, _ = enum_words[i-1]
                    p = longest_common_prefix(word, word2)
                    lcp[i] = max(lcp[i], p)
                    lcp[i-1] = max(lcp[i-1], p)
                
            for (word, index), p in zip(enum_words, lcp):
                # 判断缩写是否会变短
                delta = size - 2 - p
                if delta <= max(1, len(str(delta)) - 1):
                    ans[index] = word
                else:
                    ans[index] = word[:p+1] + str(delta) + last
    
        return ans