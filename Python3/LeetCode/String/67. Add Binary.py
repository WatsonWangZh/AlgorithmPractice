# Given two binary strings, return their sum (also a binary string).
# The input strings are both non-empty and contains only characters 1 or 0.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # M1.逐位处理
        idxa, idxb = len(a)-1, len(b)-1
        carry = 0
        res = ""
        while idxa >= 0 or idxb >= 0 or carry > 0:
            if idxa >= 0 and idxb >= 0:
                temp = int(a[idxa]) + int(b[idxb]) + carry
                idxa -= 1
                idxb -= 1
            elif idxa >= 0:
                temp = int(a[idxa]) + carry
                idxa -= 1
            elif idxb>=0:
                temp = int(b[idxb]) + carry
                idxb -= 1
            else:
                temp = carry
            carry = temp // 2
            temp %= 2
            res += str(temp)
        return res[::-1]

        # M2.调库
        #return bin(int(a,2)+int(b,2))[2:]
