# Given two integers representing the numerator and denominator of a fraction, 
# return the fraction in string format.
# If the fractional part is repeating, enclose the repeating part in parentheses.

# Example 1:
# Input: numerator = 1, denominator = 2
# Output: "0.5"

# Example 2:
# Input: numerator = 2, denominator = 1
# Output: "2"

# Example 3:
# Input: numerator = 2, denominator = 3
# Output: "0.(6)"

# Hints:
# No scary math, just apply elementary math knowledge. Still remember how to perform a long division?
# Try a long division on 4/9, the repeating part is obvious. Now try 4/333. Do you see a pattern?
# Notice that once the remainder starts repeating, so does the divided result.
# Be wary of edge cases! List out as many test cases as you can think of and test your code thoroughly.

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        if numerator == 0:
            return '0'
        
        res = ''
        #decide sign of the res
        res += '-' if (numerator > 0) ^ (denominator > 0) else ''

        numerator = abs(numerator)
        denominator = abs(denominator)

        #calculate the integral part
        res += str((numerator // denominator))
        numerator %= denominator
        if numerator == 0:
            return res

        #calcualte the decimal part
        res += '.'
        numerators = {}
        while numerator != 0:
            if numerator in numerators:
                idx = numerators[numerator]
                res = res[:idx]+'('+res[idx:]+')'
                return res

            numerators[numerator] = len(res)
            numerator *= 10
            res += str((numerator // denominator))
            numerator %= denominator

        return res
