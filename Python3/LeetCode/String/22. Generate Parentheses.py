# Given n pairs of parentheses, 
# write a function to generate all combinations of well-formed parentheses.

# For example, given n = 3, a solution set is:
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

class Solution(object):
    def generateParenthesis(self, n: int):
        res = []  
        self.generate(n, n, "", res)  
        return res  

    def generate(self, left, right, str, res):  
        if left == 0 and right == 0:  
            res.append(str)  
            return  
        if left > 0:  
            self.generate(left - 1, right, str + '(', res)  
        if right > left:  
            self.generate(left, right - 1, str + ')', res)

def main():
    s = Solution()
    print(s.generateParenthesis(n=3))

if __name__ == "__main__":
    main()