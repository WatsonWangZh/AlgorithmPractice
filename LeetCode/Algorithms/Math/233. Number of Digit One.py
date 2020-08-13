# Given an integer n, 
# count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

# Example:
# Input: 13
# Output: 6 
# Explanation: Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.

# Hints:
# Beware of overflow.

class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 蛮力 TLE
        res = 0
        for i in range(n):
            res += str(i).count('1')
        return res

        # 找规律
        # https://leetcode-cn.com/problems/number-of-digit-one/solution/shu-zi-1-de-ge-shu-by-leetcode/
        res = 0
        i = 1
        while i <= n:
            divider = i * 10
            res += (n // divider) * i + min(max(n % divider - i + 1, 0), i)
            i *= 10
        return res