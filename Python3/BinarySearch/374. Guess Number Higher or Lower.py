# We are playing the Guess Game. The game is as follows:
# I pick a number from 1 to n. You have to guess which number I picked.
# Every time you guess wrong, I'll tell you whether the number is higher or lower.
# You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):
# -1 : My number is lower
#  1 : My number is higher
#  0 : Congrats! You got it!

# Example :
# Input: n = 10, pick = 6
# Output: 6

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # M1.线性查找 MemoryError
        # for i in range(n+1):
        #     if guess(i) == 0:
        #         return i

        # M2.折半查找
        lower_bound, upper_bound = 1, n
        while True:
            cur_guess = (lower_bound + upper_bound) / 2
            res = guess(cur_guess)
            if res == 0:
                return cur_guess
            elif res == 1:
                lower_bound = cur_guess + 1
            else:
                upper_bound = cur_guess
                