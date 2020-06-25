# Alice and Bob take turns playing a game, with Alice starting first.
# Initially, there is a number N on the chalkboard.  
# On each player's turn, that player makes a move consisting of:
# Choosing any x with 0 < x < N and N % x == 0.
# Replacing the number N on the chalkboard with N - x.
# Also, if a player cannot make a move, they lose the game.
# Return True if and only if Alice wins the game, assuming both players play optimally.

# Example 1:
# Input: 2
# Output: true
# Explanation: Alice chooses 1, and Bob has no more moves.

# Example 2:
# Input: 3
# Output: false
# Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.

# Note:
# 1 <= N <= 1000

# Hints:
# If the current number is even, we can always subtract a 1 to make it odd. 
# If the current number is odd, we must subtract an odd number to make it even.

class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        # 数学推导 O(1)
        # 这道题我们发现如果黑板上写的是奇数，那么下一个人改完之后肯定会变成偶数，
        # 因为奇数没有偶数因子并且奇数减去奇数差为偶数。
        # 我们还发现谁先在黑板上写出3谁就赢了，因为3之后另外一个人只能写2，然后你再写1，
        # 另外一个人就没办法写了。所以如果想赢，必须让自己每次写完之后黑板上都是奇数，
        # 因为这样对方就只能写偶数，那么3肯定就会是自己写的了。
        # 时间复杂度分析：O(1)

        return N % 2 == 0