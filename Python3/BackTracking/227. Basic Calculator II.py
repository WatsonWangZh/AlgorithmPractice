# Implement a basic calculator to evaluate a simple expression string.
# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . 
# The integer division should truncate toward zero.

# Example 1:
# Input: "3+2*2"
# Output: 7

# Example 2:
# Input: " 3/2 "
# Output: 1

# Example 3:
# Input: " 3+5 / 2 "
# Output: 5
# Note:
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        sign = "+"
        res = 0
        stack = []
        s += "+"
        for c in s:
           if c == " ": continue
           if c.isdigit():
              num *= 10
              num += ord(c)-ord('0')
           else:
              if sign == "+":
                stack.append(num)
              elif sign == "-":
                stack.append(-num)
              elif sign == "*":
                stack[-1] *= num
              elif sign == "/":
                if stack[-1] <= 0:
                    stack[-1] = -1*(-stack[-1]/num)
                else:
                    stack[-1] /= num
              sign = c
              num = 0
        for c in stack:
            res += c
        return res 
        