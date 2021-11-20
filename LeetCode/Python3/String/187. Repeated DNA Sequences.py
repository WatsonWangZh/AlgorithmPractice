# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, 
# for example: "ACGAATTCCG". 
# When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
# Write a function to find all the 10-letter-long sequences (substrings) 
# that occur more than once in a DNA molecule.

# Example:
# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC", "CCCCCAAAAA"]

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # 哈希表 O(n)
        # 用哈希表记录所有长度是10的子串的个数。
        # 从前往后扫描，当子串出现第二次时，将其记录在答案中。
        # 时间复杂度分析：
        # 总共约 n 个长度是10的子串，所以总共有 10n 个字符。
        # 计算量与字符数量成正比，所以时间复杂度是 O(n)。

        memo = {}
        result = set() #avoid replicate 
        for i in range(len(s)-9):
                if s[i: i+10] not in memo:
                        memo[s[i:i+10]] = True
                else:
                        result.add(s[i:i+10])
        return result
        