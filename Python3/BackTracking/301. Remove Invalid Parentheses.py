# Remove the minimum number of invalid parentheses in order to make the input string valid. 
# Return all possible results.
# Note: The input string may contain letters other than the parentheses ( and ).

# Example 1:
# Input: "()())()"
# Output: ["()()()", "(())()"]

# Example 2:
# Input: "(a)())()"
# Output: ["(a)()()", "(a())()"]

# Example 3:
# Input: ")("
# Output: [""]

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # DFS+括号序列 O(n2^n)
        # 这是一道有关括号序列的问题。那么如何判断一个括号序列是否合法呢？
        # 判断方法：从前往后扫描字符串，维护一个计数器，遇到(就加一，遇到)就减一，如果过程中计数器的值都是非负数，
        # 且最终计数器的值是零，则括号序列是合法的。
        # 暴力dfs搜索空间比较高，我们要想办法进行剪枝。
        # 剪枝方法：对于连续的)，不论删除哪一个，得到的方案都是相同的，所以我们对于所有连续的)，只枚举删除多少个。
        # 时间复杂度分析：我们先来考虑搜索空间有多大，最坏情况下，对于每个括号都有删或不删两种选择，所以共有 2^n 种不同方案。
        # 对于每种方案，最后还需要 O(n) 的计算量来记录答案，所以总时间复杂度是 O(n2^n)。

        self.res=[]
        left = 0
        right = 0

        # Calculate the number of unable to match "(" and ")" in the string
        for item in s:
            if item == ")":
                if left != 0:
                    left -= 1
                else:
                    right += 1
            if item == "(":
                left += 1

        def isValid(exp):
            count = 0
            for item in exp:
                if item == "(":
                    count += 1
                if item == ")":
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        def dfs(s, pos, left, right):
            # Base case
            if left == 0 and right == 0 and isValid(s):
                self.res.append(s)
                return
            for i in range(pos,len(s)):
                # Avoid the duplicate removals
                if i != pos and s[i] == s[i-1]:
                    continue
                if s[i] == ")" and right>0:
                    curr = s[0:i] + s[i+1:len(s)]
                    dfs(curr, i, left, right-1)
                if s[i] == "(" and left>0:
                    curr = s[0:i] + s[i+1:len(s)]
                    dfs(curr, i, left-1, right)
        dfs(s, 0, left, right)
        return self.res
