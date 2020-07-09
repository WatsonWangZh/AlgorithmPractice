# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:
# Input: 123
# Output: 321

# Example 2:
# Input: -123
# Output: -321

# Example 3:
# Input: 120
# Output: 21

# Note:
# Assume we are dealing with an environment which could only store integers 
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. 
# For the purpose of this problem, assume that your function returns 0 
# when the reversed integer overflows.

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """      
        # M1. 字符串 int -> str -> int
        if x > 0:
            x = str(x)
            x = x[::-1]
            x = int(x)
        else :
            x = -x
            x = str(x)
            x = x[::-1]
            x = -int(x)
        if -2**31 <= x <= 2**31-1:
            return x
        else:
            return 0

        # M2. 模拟 
        sign = 1
        if x < 0 : 
            sign = -1
        x = x * sign

        res = 0
        while x :
            res = res * 10 + x % 10
            x //= 10
        res = res*sign
        return res if -2**31 <= res <= 2**31-1 else 0
