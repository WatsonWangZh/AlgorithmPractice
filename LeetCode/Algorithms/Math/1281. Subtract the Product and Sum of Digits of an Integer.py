# Given an integer number n, 
# return the difference between the product of its digits and the sum of its digits.
 
# Example 1:
# Input: n = 234
# Output: 15 
# Explanation: 
# Product of digits = 2 * 3 * 4 = 24 
# Sum of digits = 2 + 3 + 4 = 9 
# Result = 24 - 9 = 15

# Example 2:
# Input: n = 4421
# Output: 21
# Explanation: 
# Product of digits = 4 * 4 * 2 * 1 = 32 
# Sum of digits = 4 + 4 + 2 + 1 = 11 
# Result = 32 - 11 = 21

# Constraints:
# 1 <= n <= 10^5
# Hints:
# How to compute all digits of the number ?
# Use modulus operator (%) to compute the last digit.
# Generalise modulus operator idea to compute all digits.

class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 模拟
        Product, Sum = 1, 0
        while n:
            Product *= n % 10
            Sum += n % 10
            n /= 10
        return Product - Sum