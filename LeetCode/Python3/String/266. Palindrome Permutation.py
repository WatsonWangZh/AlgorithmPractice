# Given a string, determine if a permutation of the string could form a palindrome.

# Example 1:
# Input: "code"
# Output: false

# Example 2:
# Input: "aab"
# Output: true

# Example 3:
# Input: "carerac"
# Output: true

# Hints:
# Consider the palindromes of odd vs even length. What difference do you notice?
# Count the frequency of each character.
# If each character occurs even number of times, then it must be a palindrome. 
# How about character which occurs odd number of times?

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Set应用 O(n)
        # 根据题目中的提示，我们分字符串的个数是奇偶的情况来讨论，
        # 如果是偶数的话，由于回文字符串的特性，每个字母出现的次数一定是偶数次，
        # 当字符串是奇数长度时，只有一个字母出现的次数是奇数，其余均为偶数，
        # 那么利用这个特性我们就可以解题。

        out = []
        
        for c in set(s):
            out.append((s.count(c)) % 2)
        
        return out.count(1) <= 1