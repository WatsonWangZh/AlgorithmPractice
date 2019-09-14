# Given an Android 3x3 key lock screen and two integers m and n, 
# where 1 ≤ m ≤ n ≤ 9, count the total number of unlock patterns of the Android lock screen, 
# which consist of minimum of m keys and maximum n keys.

# Rules for a valid pattern:
# Each pattern must connect at least m keys and at most n keys.
# All the keys must be distinct.
# If the line connecting two consecutive keys in the pattern passes through any other keys, 
# the other keys must have previously selected in the pattern. 
# No jumps through non selected key is allowed.
# The order of keys used matters.
 
# Explanation:
# | 1 | 2 | 3 |
# | 4 | 5 | 6 |
# | 7 | 8 | 9 |
# Invalid move: 4 - 1 - 3 - 6
# Line 1 - 3 passes through key 2 which had not been selected in the pattern.

# Invalid move: 4 - 1 - 9 - 2
# Line 1 - 9 passes through key 5 which had not been selected in the pattern.

# Valid move: 2 - 4 - 1 - 3 - 6
# Line 1 - 3 is valid because it passes through key 2, which had been selected in the pattern

# Valid move: 6 - 5 - 4 - 1 - 9 - 2
# Line 1 - 9 is valid because it passes through key 5, which had been selected in the pattern.

# Example:
# Input: m = 1, n = 1
# Output: 9

class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # M1. 递归回溯
        # https://www.cnblogs.com/grandyang/p/5541012.html
        if m > n:
            return 0

        memo, res, needSkip = {}, [], [[0] * 10 for _ in range(10)]
        needSkip[1][3], needSkip[3][1], needSkip[1][7], needSkip[7][1], needSkip[1][9], needSkip[9][1] = 2, 2, 4, 4, 5, 5
        needSkip[2][8], needSkip[8][2], needSkip[3][9], needSkip[9][3], needSkip[3][7], needSkip[7][3] = 5, 5, 6, 6, 5, 5
        needSkip[4][6], needSkip[6][4], needSkip[7][9], needSkip[9][7] = 5, 5, 8, 8
        return self.helper(needSkip, memo, m, n, 1, 1, [0] * 10) * 4    \
                + self.helper(needSkip, memo, m, n, 1, 2, [0] * 10) * 4 \
                + self.helper(needSkip, memo, m, n, 1, 5, [0] * 10)
    
    def helper(self, needSkip, memo, m, n, curLen, curLast, visited):

        visitedKey = self.constructKey(visited)

        if (curLen, visitedKey, curLast) not in memo: 
            if curLen > n:
                return 0

            res = 0
            if m <= curLen <= n:
                res += 1

            visited[curLast] = True

            for i in range(1, 10):
                if not visited[i] and (needSkip[curLast][i] == 0 or visited[needSkip[curLast][i]]):
                    res += self.helper(needSkip, memo, m, n, curLen + 1, i, visited)

            visited[curLast] = False
                
            memo[(curLen, visitedKey, curLast)] = res

        return memo[(curLen, visitedKey, curLast)]
    
    def constructKey(self, visited):

        res = 0
        for val in visited:
            res = (res << 1) + val

        return res