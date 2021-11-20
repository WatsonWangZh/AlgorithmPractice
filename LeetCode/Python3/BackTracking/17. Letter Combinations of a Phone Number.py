# Given a string containing digits from 2-9 inclusive, 
# return all possible letter combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) is given below. 
# Note that 1 does not map to any letters.

# Example:
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:
# Although the above answer is in lexicographical order, 
# your answer could be in any order you want.

class Solution(object):
    def letterCombinations(self, digits):
        # 递归 O(4^l)
        # 可以通过手工或者循环的方式预处理每个数字可以代表哪些字母。
        # 通过递归尝试拼接一个新字母。
        # 递归到目标长度，将当前字母串加入到答案中。
        # 注意，有可能数字串是空串，需要特判。
        # 时间复杂度
        # 由于使用了递归的方式，时间复杂度与答案个数相同。
        # 设数字串长度为 l，则最坏时间复杂度为 O(4^l)。

        if len(digits) < 1:
            return []
        dic = {"1":"","2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res = [""]
        for digit in digits:
            candidates = dic.get(digit)
            temp_res = []
            for candidate in candidates:
                for element in res:
                    temp_res.append(element + candidate)
            res = temp_res
            # print(len(res))
        return res
