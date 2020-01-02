# Given a non-negative integer num, Return its encoding string.
# The encoding is done by converting the integer to a string using a secret function that you should deduce from the following table:
# n     f(n)
# 0     ""
# 1     "0"
# 2     "1"
# 3     "00"
# 4     "01"
# 5     "10"
# 6     "11"
# 7     "0000"

# Example 1:
# Input: num = 23
# Output: "1000"

# Example 2:
# Input: num = 107
# Output: "101100"

class Solution(object):
    def encode(self, num):
        """
        :type num: int
        :rtype: str
        """
        l = 0
        while num >= 1<<l:
            # print(num, l)
            num -= 1<<l
            # print(num, l)
            l += 1
            
        res = ""
        for i in range(l):
            # print(num)
            if num & 1:
                res += "1"
            else:
                res += "0"
            num >>= 1
        return res[::-1]