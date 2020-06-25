# In the "100 game," two players take turns adding, to a running total, any integer from 1..10. 
# The player who first causes the running total to reach or exceed 100 wins.
# What if we change the game so that players cannot re-use integers?
# For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.
# Given an integer maxChoosableInteger and another integer desiredTotal, determine if the first player to move can force a win, 
# assuming both players play optimally.
# You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger than 300.

# Example
# Input:
# maxChoosableInteger = 10
# desiredTotal = 11
# Output:
# false

# Explanation:
# No matter which integer the first player choose, the first player will lose.
# The first player can choose an integer from 1 up to 10.
# If the first player choose 1, the second player can only choose integers from 2 up to 10.
# The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
# Same with other integers chosen by the first player, the second player will always win.

class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if maxChoosableInteger >= desiredTotal or desiredTotal <= 0:
            return True
        totalSum = (1+ maxChoosableInteger) * maxChoosableInteger / 2
        if totalSum < desiredTotal:
            return False
        if totalSum == desiredTotal and maxChoosableInteger % 2 == 1:
            return True
        
        memo = [0] * (1 << maxChoosableInteger)
        
        def canWin(maxChoosableInteger, desiredTotal, memo, state):
            # memo: record state:
            #       0 hasn't explore; 1 user1 can win; -1 user2 can win
            # state: sum until now
            
            if desiredTotal <= 0:
                return False
            if memo[state] != 0:
                return memo[state] == 1
            
            i = 0
            while i < maxChoosableInteger:
                # current i has added
                if state & (1 << i) > 0:
                    i += 1
                    continue
                # the other can not win
                if not canWin(maxChoosableInteger, desiredTotal - i - 1, memo, state | 1 << i):
                    memo[state] = 1
                    return True
                i += 1
                
            memo[state] = -1
            return False
    
        return canWin(maxChoosableInteger, desiredTotal, memo, 0)
