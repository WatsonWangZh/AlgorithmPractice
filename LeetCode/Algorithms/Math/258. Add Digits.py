# Given a non-negative integer num, 
# repeatedly add all its digits until the result has only one digit.

# Example:
# Input: 38
# Output: 2 
# Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
#              Since 2 has only one digit, return it.

# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?

# Hints:
# A naive implementation of the above process is trivial. Could you come up with other methods?
# What are all the possible results?
# How do they occur, periodically or randomly?
# You may find this Wikipedia(https://en.wikipedia.org/wiki/Digital_root) article useful.

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # M1. 模拟
        while num > 9:
            tmp = 0
            while num:
                tmp += num%10
                num /= 10
            num = tmp
        return num

        # M2. 公式法
        # https://en.wikipedia.org/wiki/Digital_root
        if num < 10:
            return num
        return 1 + (num - 1) % (10 - 1)