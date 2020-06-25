# You are playing the following Flip Game with your friend: 
# Given a string that contains only these two characters: + and -, 
# you and your friend take turns to flip two consecutive "++" into "--". 
# The game ends when a person can no longer make a move and therefore the other person will be the winner.
# Write a function to compute all possible states of the string after one valid move.

# Example:
# Input: s = "++++"
# Output: 
# [
#   "--++",
#   "+--+",
#   "++--"
# ]

# Note: If there is no valid move, return an empty list [].

class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # 数组遍历 O(n)
        # 从第二个字母开始遍历，每次判断当前字母是否为+，和之前那个字母是否为+，如果都为+，则将翻转后的字符串存入结果中即可。
        
        res = []
        if not s:
            return res

        for i in range(1, len(s)):
            if s[i] == '+' and s[i-1] == '+':
                res.append(s[:i-1] + '--' + s[i+1:])

        return res