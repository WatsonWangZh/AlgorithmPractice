# Given two integers dividend and divisor, divide two integers 
# without using multiplication, division and mod operator.
# Return the quotient after dividing dividend by divisor.
# The integer division should truncate toward zero.

# Example 1:
# Input: dividend = 10, divisor = 3
# Output: 3

# Example 2:
# Input: dividend = 7, divisor = -3
# Output: -2

# Note:
# Both dividend and divisor will be 32-bit signed integers.
# The divisor will never be 0.
# Assume we are dealing with an environment 
# which could only store integers within the 32-bit signed integer range: 
# [−231,  231 − 1]. For the purpose of this problem, assume that 
# your function returns 231 − 1 when the division result overflows.
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 先把符号抽取出来，只考虑两个正数相除的情况。除法其实就是被减数不断减去减数的操作，
        # 但直接不断进行减法会超时，应尽量减去大的数字，通过位移操作来快速找到
        # 比被减数小一些的减数的倍数current。不断减去且缩小current。
        # 溢出只可能是向上溢出，通过min操作进行过滤。
        MAX_INT = 2147483647
        sign = 1
        if dividend >= 0 and divisor < 0 or dividend <= 0 and divisor > 0:
            sign = -1
        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0
        current = divisor
        currentResult = 1
        while current <= dividend:
            current <<= 1
            currentResult <<= 1
        while divisor <= dividend:
            current >>= 1
            currentResult >>= 1
            if current <= dividend:
                dividend -= current
                result += currentResult
        return min(sign * result, MAX_INT)
        
