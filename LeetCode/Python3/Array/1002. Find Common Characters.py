# Given an array A of strings made only from lowercase letters, 
# return a list of all characters that show up in all strings within the list (including duplicates).  
# For example, if a character occurs 3 times in all strings but not 4 times, 
# you need to include that character three times in the final answer.
# You may return the answer in any order.

# Example 1:
# Input: ["bella","label","roller"]
# Output: ["e","l","l"]

# Example 2:
# Input: ["cool","lock","cook"]
# Output: ["c","o"]
# Note:
# 1 <= A.length <= 100
# 1 <= A[i].length <= 100
# A[i][j] is a lowercase letter
import collections
class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        # 直接统计 O(A.length * A[i].length)
        # 用Counter类来统计每个单词中字母的数量，然后取交集即可
        # 时间复杂度分析：
        # 每个单词中的每个字母遍历一遍，所以总的时间复杂度是全部字母个数 O(A.length * A[i].length)
        if len(A) == 1:
            return list(A[0])
        c = collections.Counter(A[0])
        for i in range(1, len(A)):
            t = collections.Counter(A[i])
            c = c & t
        res = []
        for i in c:
            res += i * c[i]
        return res
