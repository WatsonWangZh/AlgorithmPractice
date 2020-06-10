# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

# Note:
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        # 逐位相加模拟 int()
        res = ""
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            cur = tmp % 10
            carry = tmp // 10
            res = str(cur) + res
            i, j = i - 1, j - 1
        return "1" + res if carry else res


        # 逐位相加模拟 ord()
        res = ""
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        while i >= 0 or j >= 0:
            n1 = num1[i] if i >= 0 else '0'
            n2 = num2[j] if j >= 0 else '0'
            tmp = ord(n1) + ord(n2) -2*ord('0') + carry
            cur = tmp % 10
            carry = tmp // 10
            res = chr(cur+48) + res
            i, j = i - 1, j - 1
        return "1" + res if carry else res