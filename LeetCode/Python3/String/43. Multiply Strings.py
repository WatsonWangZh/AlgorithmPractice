# Given two non-negative integers num1 and num2 represented as strings, 
# return the product of num1 and num2, also represented as a string.

# Example 1:
# Input: num1 = "2", num2 = "3"
# Output: "6"

# Example 2:
# Input: num1 = "123", num2 = "456"
# Output: "56088"

# Note:
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contain only digits 0-9.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # 模拟 O(nm)
        # 模拟竖式乘法计算。
        # 乘积的最大长度为两个乘数的长度之和。
        # 时间复杂度
        # 竖式乘法为两层循环错位相乘，故时间按复杂度是O(nm)。

        num1 = [int(num) for num in num1][::-1]
        num2 = [int(num) for num in num2][::-1]
        res = [0] * len(num1 + num2)
        for i in range(len(num1)):
            for j in range(len(num2)):
                # 累加低位值
                res[i+j] += num1[i] * num2[j]
                # 更新进位
                res[i+j+1] += res[i+j]//10
                # 更新低位
                res[i+j] %= 10
        for i in range(len(num1+num2)-1, -1, -1):
            # 消除结果前缀0
            if res[i] == 0:
                continue
            else:
                return ''.join([str(c) for c in res[i::-1]])
        # 结果全为0
        return '0'
