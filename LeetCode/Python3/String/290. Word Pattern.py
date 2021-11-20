# Given a pattern and a string str, find if str follows the same pattern.
# Here follow means a full match, such that there is a bijection 
# between a letter in pattern and a non-empty word in str.

# Example 1:
# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true

# Example 2:
# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false

# Example 3:
# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false

# Example 4:
# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false

# Notes:
# You may assume pattern contains only lowercase letters, 
# and str contains lowercase letters that may be separated by a single space.

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        # 在 205 题基础上增加 split 操作。
        # 哈希表映射 O(n)
        # 假设pattern有 n 个字母，str有 n 个单词。
        # 相当于给了我们 n 组字母和单词的对应关系，然后问字母和单词是否一一对应，
        # 即相同字母对应相同单词，且不同字母对应不同单词。
        # 所以我们可以用两个哈希表，分别存储单词对应的字母，以及字母对应的单词。
        # 然后从前往后扫描，判断相同元素对应的值，是否是相同的。
        # 时间复杂度分析：
        # 哈希表的插入、查找操作的时间复杂度是 O(1)，两个字符串均只扫描一遍，所以总时间复杂度是 O(n)。

        ps = {}
        sp = {}
        str_s = str.split(" ")

        if len(pattern) != len(str_s):
            return False

        for i in range(len(pattern)):
            if not ps.get(pattern[i]):
                ps[pattern[i]] = str_s[i]
            else:
                if ps[pattern[i]] == str_s[i]:
                    continue
                else:
                    return False

            if not sp.get(str_s[i]):
                sp[str_s[i]] = pattern[i]
            else:
                if sp[str_s[i]] == pattern[i]:
                    continue
                else:
                    return False
        return True
