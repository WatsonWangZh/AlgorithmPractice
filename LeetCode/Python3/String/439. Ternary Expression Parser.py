# Given a string representing arbitrarily nested ternary expressions, calculate the result of the expression. 
# You can always assume that the given expression is valid and only consists of digits 0-9, ?, :, T and F 
# (T and F represent True and False respectively).

# Note:
# The length of the given string is ≤ 10000.
# Each number will contain only one digit.
# The conditional expressions group right-to-left (as usual in most languages).
# The condition will always be either T or F. That is, the condition will never be a digit.
# The result of the expression will always evaluate to either a digit 0-9, T or F.

# Example 1:
# Input: "T?2:3"
# Output: "2"
# Explanation: If true, then result is 2; otherwise result is 3.

# Example 2:
# Input: "F?1:T?4:5"
# Output: "4"
# Explanation: The conditional expressions group right-to-left. Using parenthesis, it is read/evaluated as:
#              "(F ? 1 : (T ? 4 : 5))"                   "(F ? 1 : (T ? 4 : 5))"
#           -> "(F ? 1 : 4)"                 or       -> "(T ? 4 : 5)"
#           -> "4"                                    -> "4"

# Example 3:
# Input: "T?T?F:5:3"
# Output: "F"
# Explanation: The conditional expressions group right-to-left. Using parenthesis, it is read/evaluated as:
#              "(T ? (T ? F : 5) : 3)"                   "(T ? (T ? F : 5) : 3)"
#           -> "(T ? F : 3)"                 or       -> "(T ? F : 5)"
#           -> "F"                                    -> "F"

class Solution(object):
    def parseTernary(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        # 从右边开始找到第一个问号，然后先处理这个三元表达式，然后再一步一步向左推。
        if not expression:
            return ""
        stack = []
        for c in expression[::-1]:
            if stack and stack[-1] == "?":
                stack.pop()
                x = stack.pop()
                stack.pop()
                y = stack.pop()
                stack.append(x if c == "T" else y)
            else:
                stack.append(c)
        return stack.pop()