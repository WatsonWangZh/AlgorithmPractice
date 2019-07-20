# Given an array of scores that are non-negative integers. 
# Player 1 picks one of the numbers from either end of the array followed by the player 2 
# and then player 1 and so on. Each time a player picks a number, 
# that number will not be available for the next player. 
# This continues until all the scores have been chosen. The player with the maximum score wins.
# Given an array of scores, predict whether player 1 is the winner. 
# You can assume each player plays to maximize his score.

# Example 1:
# Input: [1, 5, 2]
# Output: False
# Explanation: Initially, player 1 can choose between 1 and 2. 
# If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). 
# So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
# Hence, player 1 will never be the winner and you need to return False.

# Example 2:
# Input: [1, 5, 233, 7]
# Output: True
# Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
# Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.
# Note:
# 1 <= length of the array <= 20.
# Any scores in the given array are non-negative integers and will not exceed 10,000,000.
# If the scores of both players are equal, then player 1 is still the winner.

class Solution:
    def PredictTheWinner(self, nums):
        # M1.Recursive Time Limit Exceeded
        # def helper(l, r, nums, t):
        #     if l == r:
        #         return t * nums[l]
        #     elif t == 1:
        #         return max((helper(l+1, r, nums, -t) + nums[l]),(helper(l, r-1, nums, -t) + nums[r]))
        #     elif t == -1:
        #         return min((helper(l+1, r, nums, -t) - nums[l]),(helper(l, r-1, nums, -t) - nums[r]))
        # return helper(0, len(nums)-1, nums, 1) >= 0

        # M2.dp
        return self.predictWinner(nums, 0, len(nums)-1, dict()) >= 0

    def predictWinner(self, nums, start, end, winDict):
        if start == end:
            return nums[start]
        if (start, end) in winDict:
            return winDict[(start, end)]
        else:
            winDict[(start, end)] = max(nums[start] - self.predictWinner(nums, start+1, end, winDict),
                                        nums[end] - self.predictWinner(nums, start, end-1, winDict))
            return winDict[(start, end)]

def main():
    pass

if __name__ == "__main__":
    main()