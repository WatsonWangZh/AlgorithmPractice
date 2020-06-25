# Given a string containing just the characters '(' and ')', 
# find the length of the longest valid (well-formed) parentheses substring.

# Example 1:
# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"

# Example 2:
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # M1. 暴力枚举 O(n^2)  [Time Limit Exceeded]
        # 遍历所有的’(‘，往后开始扫描字符串，找到最长的合法括号序列。
        # 时间复杂度O(n^2)。

        # result = 0 
        # for i in range(len(s)):
        #     if s[i] == '(':
        #         curr_length, bal = 0, 1 
        #         for j in range(i+1, len(s)):
        #             if s[j] == '(':
        #                 bal += 1
        #             elif s[j] == ')':
        #                 bal -= 1 
        #             if bal == 0:
        #                 curr_length = j - i + 1
        #             if bal < 0:
        #                 break
        #         result = max(result, curr_length)
        # return result

        # M2. 使用栈来模拟操作  O(n)
        # 栈顶保存当前扫描时，当前合法序列起始位置下标。
        # 初始时栈中元素为-1。然后遍历整个字符串
        #   如果s[i] =='('，那么把i进栈。
        #   如果s[i] == ')',那么弹出栈顶元素 （代表栈顶的左括号匹配到了右括号）
        #   如果此时栈为空，将i进栈。说明之前没有与之匹配的左括号，那么就将当前的位置入栈。
        #   否则，i - stack[-1]就是当前右括号对应的合法括号序列的长度。

        # result = 0
        # stack = []
        # stack.append(-1)
        # for i in range(len(s)):
        #     if s[i] == '(':
        #         stack.append(i)
        #     else:
        #         stack.pop()
        #         if not stack:
        #             stack.append(i)
        #         else:
        #             result = max(result, i - stack[-1])
        # return result

        # M3. 动态规划 O(n)
        # 状态表示：dp[i]表示以下标i结尾的最长合法括号序列长度，
        # 所有以左括号结尾的序列都不是合法括号序列，
        # 所以我们从前往后扫描，如果遇到了右括号s[i],那么有两种情况
        #   s[i - 1] = '('，那么很明显dp[i] = dp[i - 2] + 2
        #   s[i - 1] = ')'，我们需要判断i - dp[i - 1] - 1的位置是否是左括号， 它是以s[i - 1]结尾的最长合法序列的前一个字符。
        #       如果不是左括号，说明当前右括号没有合法匹配。
        #       如果是左括号，那么dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]。
        #       分别代表以s[i - 1]结尾的最长合法括号长度，s[i]的右括号和对应的左括号，
        #       s[i]对应的左括号前面一个位置结尾的最长合法括号序列。

        # result = 0 
        # dp = [0 for _ in range(len(s))]
        # for i in range(1, len(s)):
        #     if s[i] == ')':
        #         if s[i-1] == '(':
        #             dp[i] = dp[i-2] + 2 if i >= 2 else 2
        #         elif i > dp[i - 1] and s[i - dp[i - 1] - 1] == '(':
        #             dp[i] = dp[i - 1] + 2 + (dp[i - dp[i - 1] - 2] \
        #                     if i > dp[i - 1] + 2 else 0)
        #     result = max(result, dp[i])
        # return result

        # M4. 双向扫描 O(n) 不需要使用额外空间
        # 第一遍从左往右扫描，left和right分别代表当前合法的左括号个数和右括号个数。
        # 遇到左括号left ++，遇到右括号right ++，
        # 如果left = right，说明找到了一个合法的括号对，更新答案，
        # 如果left < right，说明后面怎么匹配都不可能合法了，此时把left和right置为0。
        # 但是这样对于((())的括号序列，得不到正确解，因此我们继续从右往左匹配一次。

        # 第二遍第一遍从右往左扫描，left和right分别代表当前合法的左括号个数和右括号个数。
        # 遇到左括号left ++，遇到右括号right ++，
        # 如果left = right，说明找到了一个合法的括号对，更新答案，
        # 如果left > right，说明前面怎么匹配都不可能合法了，此时把left和right置为0。

        result = left = right = 0
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                result = max(result, 2*right)
            if left < right:
                left = right = 0

        left = right = 0

        for i in range(len(s)-1, -1, -1):
            if s[i] == ')':
                right += 1
            else:
                left += 1
            if left == right:
                result = max(result, 2 * right)
            if right < left:
                left = right = 0

        return result
