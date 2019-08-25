# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:
# Input: "A man, a plan, a canal: Panama"
# Output: true

# Example 2:
# Input: "race a car"
# Output: false

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # M1. 正则表达式 O(n)

        # import re
        # s = re.compile('[^a-zA-Z0-9]').sub('',s).lower()
        # if s == s[::-1]:
        #     return True
        # else:
        #     return False

        # M2. 双指针线性扫描 O(n)
        # 用两个指针分别从前后开始，往中间扫描。
        # 每次迭代两个指针分别向中间靠近一步，靠近的过程中忽略除了字母和数字的其他字符。
        # 然后判断两个指针所指的字符是否相等，如果不相等，说明不是回文串。
        # 当两个指针相遇时，说明原字符串是回文串。
        # 时间复杂度分析：
        # 每个字符仅会被扫描一次，所以时间复杂度是 O(n)。

        def check(char):
            return char.isdigit() or char.isalpha()
            
        s = s.lower()
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not check(s[left]):
                left += 1
            while left < right and not check(s[right]):
                right -= 1
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True
