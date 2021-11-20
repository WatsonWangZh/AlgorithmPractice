# Given an input string , reverse the string word by word. 

# Example:
# Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
# Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]

# Note: 
# A word is defined as a sequence of non-space characters.
# The input string does not contain leading or trailing spaces.
# The words are always separated by a single space.
# Follow up: Could you do it in-place without allocating extra space?

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # 模拟，数组扫描 O(n)
        # 先整体逆序，然后逐个单词逆序。
        # 时间复杂度分析:
        # 数组中的每个字符遍历两遍，所以时间复杂度为 O(n)。

        str.reverse()
        pre = 0
        for idx in range(len(str)+1):
            if idx == len(str) or str[idx] == ' ':
                str[pre:idx] = str[pre:idx][::-1]
                pre = idx + 1
        