# Write a function to generate the generalized abbreviations of a word. 
# Note: The order of the output does not matter.

# Example:
# Input: "word"
# Output:
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]

class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """ 
    #    # M1. 递归回溯 O(2^n) 缩写与否
    #     res = []
    #     self.helper(res, word, 0, "", 0)
    #     return res
        
    # def helper(self, res, word, curr_index, curr_res, count):
    #     # Base Case
    #     if curr_index == len(word):
    #         res.append(curr_res + (str(count) if count > 0 else ""))
    #         return
        
    #     # Abbreviate the current letter
    #     self.helper(res, word, curr_index + 1, curr_res, count+1)

    #     # Keep the current letter
    #     self.helper(res, word, curr_index + 1, curr_res + (str(count) if count > 0 else "") + word[curr_index], 0)

       
        # M2. 位运算
        # 凡是0的地方都是原来的字母，单独的1还是1，如果是若干个1连在一起的话，就要求出1的个数，用这个数字来替换对应的字母。
        res = []
        for i in range(0, pow(2, len(word))):
            curr_res = ""
            count = 0

            for j in range(0, len(word)):
                # Abbreviate the current letter
                if i >> j & 1:
                    count += 1
                # Keep the current letter    
                else:
                    if count:
                        curr_res += str(count) 
                        count = 0
                    curr_res += word[j]
            # Base Case
            curr_res += (str(count) if count > 0 else "")
            res.append(curr_res)
        return res