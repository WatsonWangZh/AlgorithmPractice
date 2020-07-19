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

        a, b = a[::-1], b[::-1]
        la, lb = len(a), len(b)
        res = ''

        carry = 0
        i = 0
        while i < la or i < lb or carry:
            if i < la:
                carry += int(a[i])
            if i < lb:
                carry += int(b[i])
            res += str(carry%2)
            carry = carry // 2
            i += 1
        
        return res[::-1]
