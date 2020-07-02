# Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

# Note:
# The given integer is guaranteed to fit within the range of a 32-bit signed integer.
# You could assume no leading zero bit in the integer’s binary representation.

# Example 1:
# Input: 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

# Example 2:
# Input: 1
# Output: 0
# Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # M1. 模拟 逐位求反 后处理
        lst = []
        while num > 0:
            res, num = num % 2, num // 2
            lst.insert(0, 1-res)
        comp = 0
        for val in lst:
            comp = comp*2+val
        return comp
        
        # M2. 位运算规律

        t = 1
        while t <= num:
            t <<= 1
        return (t-1)^num