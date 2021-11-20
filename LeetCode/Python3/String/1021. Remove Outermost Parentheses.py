# A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, 
# and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
# A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, 
# with A and B nonempty valid parentheses strings.
# Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.
# Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

# Example 1:
# Input: "(()())(())"
# Output: "()()()"
# Explanation: 
# The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
# After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

# Example 2:
# Input: "(()())(())(()(()))"
# Output: "()()()()(())"
# Explanation: 
# The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
# After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".

# Example 3:
# Input: "()()"
# Output: ""
# Explanation: 
# The input string is "()()", with primitive decomposition "()" + "()".
# After removing outer parentheses of each part, this is "" + "" = "".
 
# Note:
# S.length <= 10000
# S[i] is "(" or ")"
# S is a valid parentheses string

class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        # 栈 O(n)
        # 与判断括号对是否合法一样，用栈结构，遇到左括号入栈，遇到右括号出栈。
        # 题目要求去除最外层的括号，那么记录答案的时候只需要判断一下栈是否为空，如果为空，则说明该括号是最外层括号，不记录即可。
        # 时间复杂度
        # 每个字符入栈一次或出栈一次，所以时间复杂度是 O(n)。

        stack = []
        result = ""

        for char in S:
            if char == ")":
                stack.pop()
            if stack:
                result += char
            if char == "(":
                stack.append(char)

        return result