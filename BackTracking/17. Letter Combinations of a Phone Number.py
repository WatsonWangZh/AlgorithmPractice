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

def main():
    s = Solution()
    print(s.letterCombinations("23"))

if __name__ == "__main__":
    main()