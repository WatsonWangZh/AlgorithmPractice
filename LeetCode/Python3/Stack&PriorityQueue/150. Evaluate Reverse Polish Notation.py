# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
# Note:
# Division between two integers should truncate toward zero.
# The given RPN expression is always valid. 
# That means the expression would always evaluate to a result 
# and there won't be any divide by zero operation.

# Example 1:
# Input: ["2", "1", "+", "3", "*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

# Example 2:
# Input: ["4", "13", "5", "/", "+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6

# Example 3:
# Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# Output: 22
# Explanation: 
#   ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        # 栈模拟
        stack = []
        for token in tokens:
            # print(stack,token)
            if token.isdigit() or len(token) > 1: # len(token)>1 for negative numbers, eg -11.
                stack.append(int(token))
            else:
                num2, num1 = stack.pop(), stack.pop()
                output = 0
                if token == '+':
                    output = num1 + num2
                elif token == '-':
                    output = num1 - num2
                elif token == '*':
                    output = num1 * num2
                else:
                    output = int(num1*1. / num2)
                stack.append(output)
        return stack.pop()