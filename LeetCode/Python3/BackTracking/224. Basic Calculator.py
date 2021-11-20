# Implement a basic calculator to evaluate a simple expression string.
# The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, 
# non-negative integers and empty spaces .

# Example 1:
# Input: "1 + 1"
# Output: 2

# Example 2:
# Input: " 2-1 + 2 "
# Output: 3

# Example 3:
# Input: "(1+(4+5+2)-3)+(6+8)"
# Output: 23
# Note:
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        val_stack, sign_stack = [0], []
        digit, sign = 0, 1

        for c in s:
            if c.isdigit():
                digit = digit * 10 + ord(c) - ord('0')
            elif c == '+' or c == '-':
                val_stack[-1] += digit * sign
                digit = 0
                sign = 1 if c == '+' else -1
            elif c == '(':
                sign_stack.append(sign)
                val_stack.append(0)
                sign = 1
            elif c == ')':
                val_stack[-1] += digit * sign
                digit, sign = val_stack.pop(), sign_stack.pop()
                val_stack[-1] += digit * sign
                digit, sign = 0, 1

        ans = digit * sign
        while val_stack:
            ans += val_stack.pop()
        return ans
