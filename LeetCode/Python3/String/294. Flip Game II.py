# You are playing the following Flip Game with your friend: 
# Given a string that contains only these two characters: + and -, 
# you and your friend take turns to flip two consecutive "++" into "--". 
# The game ends when a person can no longer make a move and therefore the other person will be the winner.
# Write a function to determine if the starting player can guarantee a win.

# Example:
# Input: s = "++++"
# Output: true 

# Explanation: The starting player can guarantee a win by flipping the middle "++" to become "+--+".

# Follow up:
# Derive your algorithm's runtime complexity.

class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 遍历递归 O(n)
        # 从第二个字母开始遍历整个字符串，如果当前字母和之前那个字母都是+，
        # 那么我们递归调用将这两个位置变为--的字符串，
        # 如果返回false，说明当前玩家可以赢，
        # 结束循环返回false。

        for i in range(1, len(s)):
            if s[i] == '+' and s[i-1] == '+' and not self.canWin(s[:i-1] + '--' + s[i+1:]):
                return True

        return False