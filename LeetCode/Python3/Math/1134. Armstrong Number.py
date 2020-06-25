# The k-digit number N is an Armstrong number if and only if the k-th power of each digit sums to N.
# Given a positive integer N, return true if and only if it is an Armstrong number. 

# Example 1:
# Input: 153
# Output: true
# Explanation: 
# 153 is a 3-digit number, and 153 = 1^3 + 5^3 + 3^3.

# Example 2:
# Input: 123
# Output: false
# Explanation: 
# 123 is a 3-digit number, and 123 != 1^3 + 2^3 + 3^3 = 36.
 
# Note:
# 1 <= N <= 10^8

# Hints:
# Check if the given k-digit number equals the sum of the k-th power of it's digits.
# How to compute the sum of the k-th power of the digits of a number ? 
# Can you divide the number into digits using division and modulus operations ?
# You can find the least significant digit of a number by taking it modulus 10. 
# And you can remove it by dividing the number by 10 (integer division). 
# Once you have a digit, you can raise it to the power of k and add it to the sum.

class Solution(object):
    def isArmstrong(self, N):
        """
        :type N: int
        :rtype: bool
        """
        # 依题意验证即可
        n = str(N)
        temp = 0
        for i in n:
            temp += int(i) ** len(n)
        return temp == N
