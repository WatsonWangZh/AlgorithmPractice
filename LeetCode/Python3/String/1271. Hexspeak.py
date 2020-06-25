# A decimal number can be converted to its Hexspeak representation by 
# first converting it to an uppercase hexadecimal string, 
# then replacing all occurrences of the digit 0 with the letter O, 
# and the digit 1 with the letter I.  
# Such a representation is valid if and only if it consists only of the letters 
# in the set {"A", "B", "C", "D", "E", "F", "I", "O"}.
# Given a string num representing a decimal integer N, 
# return the Hexspeak representation of N if it is valid, otherwise return "ERROR".

# Example 1:
# Input: num = "257"
# Output: "IOI"
# Explanation:  257 is 101 in hexadecimal.

# Example 2:
# Input: num = "3"
# Output: "ERROR"
 
# Constraints:
# 1 <= N <= 10^12
# There are no leading zeros in the given string.
# All answers must be in uppercase letters.

# Hints:
# Convert the given number to hexadecimal.
# Replace all 0 and 1 with 'O' and 'I'.
# Check if the final string has any numerical digits.

class Solution(object):
    def toHexspeak(self, num):
        """
        :type num: str
        :rtype: str
        """
        # M1. 模拟 手写
        valid_digits = {0: "O", 1:"I", 10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
        num_in_int = int(num)
        res = ""
        while num_in_int:
            q, r = divmod(num_i n_int, 16)
            if r not in valid_digits:
                return "ERROR"
            else:
                res = valid_digits[r] + res
            num_in_int = q
        return res

        # M2. 模拟 使用内置函数
        num = hex(int(num))[2:]
        num = num.upper()
        num = num.replace('0','O')
        num = num.replace('1', 'I')
        valid = ["A", "B", "C", "D", "E", "F", "I", "O"]
        for i in num:
            if i not in valid:
                return "ERROR"
        return num