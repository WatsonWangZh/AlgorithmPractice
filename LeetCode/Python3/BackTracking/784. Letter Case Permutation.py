# Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  
# Return a list of all possible strings we could create.

# Examples:
# Input: S = "a1b2"
# Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

# Input: S = "3z4"
# Output: ["3z4", "3Z4"]

# Input: S = "12345"
# Output: ["12345"]

# Note:
# S will be a string with length between 1 and 12.
# S will consist only of letters or digits.

class Solution(object):

    # DFS O(n×2^n)
    # 深度优先搜索。从左到右一位一位枚举：
    # 如果遇到数字，则直接跳过当前位，枚举下一位；
    # 如果遇到字母，则分别将当前位设成小写字母和大写字母，然后递归到下一位；
    # 时间复杂度分析：最坏情况下，所有字符都是字母，则每个字符都有两种选择，一共会得到 2^n个字符串，
    # 最后将每个字符串记录在答案中还需要 O(n) 的计算量，所以总时间复杂度是 O(n×2^n)。
    
    def dfs(self, pos, S, s, ans):
        if pos == len(S):
            ans.append(s)
        elif S[pos].isdigit():
            self.dfs(pos + 1, S, s + S[pos], ans)
        else:
            self.dfs(pos + 1, S, s + S[pos].upper(), ans)
            self.dfs(pos + 1, S, s + S[pos].lower(), ans)

    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = []
        self.dfs(0, S, "", res)
        return res
    