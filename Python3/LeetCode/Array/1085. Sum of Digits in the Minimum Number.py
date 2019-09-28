# Given an array A of positive integers, let S be the sum of the digits of the minimal element of A.
# Return 0 if S is odd, otherwise return 1.

# Example 1:
# Input: [34,23,1,24,75,33,54,8]
# Output: 0
# Explanation: 
# The minimal element is 1, and the sum of those digits is S = 1 which is odd, so the answer is 0.

# Example 2:
# Input: [99,77,33,66,55]
# Output: 1
# Explanation: 
# The minimal element is 33, and the sum of those digits is S = 3 + 3 = 6 which is even, so the answer is 1.
 
# Note:
# 1 <= A.length <= 100
# 1 <= A[i].length <= 100

# Hints:
# How to find the minimum number in an array?
# Loop over the array and compare each one of the numbers.
# How to find the sum of digits?
# Divide the number consecutively and get their remainder modulus 10. 
# Sum those remainders and return the answer as the problem asks.

class Solution(object):
    def sumOfDigits(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # 找最小，求数位和，判断结果
        mini = float('inf')
        for a in A:
            if a < mini:
                mini = a
        res = 0
        while mini:
            digit = mini % 10
            mini /= 10
            res += digit
        return 0 if res%2 else 1

        # 调库
        # return 0 if sum(map(int,list(str(min(A))))) % 2 else 1