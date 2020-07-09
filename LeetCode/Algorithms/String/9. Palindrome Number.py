# Determine whether an integer is a palindrome. 
# An integer is a palindrome when it reads the same backward as forward.

# Example 1:
# Input: 121
# Output: true

# Example 2:
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. 
# Therefore it is not a palindrome.

# Example 3:
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# Follow up:
# Coud you solve it without converting the integer to a string?

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # M1. int -> str -> int
        return x >= 0 and x == int(str(x)[::-1])
        
        # M2. str
        a = str(x)
        if a == a[::-1]:
            return True
        else:
            return False
        
        # M3. 模拟
        if x < 0:
            return False
        # 记录原始x值，x在循环中会变化
        y = x
        res = 0
        while x:
            res = res * 10 + x % 10
            x = x // 10
        return res == y